"""
Mitsuba Plugin API generator
"""

import argparse, re
from pathlib import Path
from typing import Dict, List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

UTILS = """from __future__ import annotations
from dataclasses import dataclass, field, fields, is_dataclass
from typing import Any, Dict, List, Optional

@dataclass
class Plugin:
    type: str
    id: Optional[str] = None
    def to_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {"type": self.type}
        if self.id is not None:
            out["id"] = self.id
        for f in fields(self):
            if f.name in ("type", "id"):
                continue
            v = getattr(self, f.name)
            if v is None:
                continue
            out[f.name] = serialize(v)
        return out

def serialize(obj: Any) -> Any:
    if isinstance(obj, Transform):
        return obj.to_mi()
    # already a Mitsuba Transform?
    try:
        if obj.__class__.__name__.endswith("Transform4f"):
            return obj
    except Exception:
        pass
    if is_dataclass(obj):
        return obj.to_dict() if hasattr(obj, "to_dict") else {
            k: serialize(getattr(obj, k)) for k in obj.__dataclass_fields__  # type: ignore
        }
    if isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [serialize(v) for v in obj]
    return obj

@dataclass
class RGB(Plugin):
    value: List[float] = field(default_factory=lambda: [1.0, 1.0, 1.0])
    def __init__(self, value: List[float]):
        super().__init__(type="rgb")
        self.value = value

@dataclass
class Ref(Plugin):
    def __init__(self, id: str):
        super().__init__(type="ref")
        self.id = id

class Transform:
    \"\"\"Chainable builder that composes a real mi.ScalarTransform4f and is auto-serialized.\"\"\"
    __slots__ = ("_ops",)
    def __init__(self) -> None:
        self._ops: List[Dict[str, Any]] = []
    def translate(self, x: float, y: float, z: float) -> "Transform":
        self._ops.append({"op":"translate","value":[x,y,z]}); return self
    def scale(self, x: float, y: Optional[float] = None, z: Optional[float] = None) -> "Transform":
        if y is None and z is None: self._ops.append({"op":"scale","value":[x,x,x]})
        else: self._ops.append({"op":"scale","value":[x,y,z]})
        return self
    def rotate(self, ax: float, ay: float, az: float, angle: float) -> "Transform":
        self._ops.append({"op":"rotate","axis":[ax,ay,az],"angle":angle}); return self
    def look_at(self, origin: List[float], target: List[float], up: List[float] = [0,1,0]) -> "Transform":
        self._ops.append({"op":"look_at","origin":origin,"target":target,"up":up}); return self
    def matrix(self, m4x4: List[List[float]]) -> "Transform":
        self._ops.append({"op":"matrix","matrix":m4x4}); return self
    def to_mi(self):
        import mitsuba as mi
        T = mi.ScalarTransform4f
        cur = T()
        for step in self._ops:
            op = step["op"]
            if op == "translate": piece = T().translate(step["value"])
            elif op == "scale": piece = T().scale(step["value"])
            elif op == "rotate": piece = T().rotate(axis=step["axis"], angle=step["angle"])
            elif op == "look_at": piece = T().look_at(origin=step["origin"], target=step["target"], up=step["up"])
            elif op == "matrix": piece = T(step["matrix"])
            else: continue
            cur = piece @ cur
        return cur
"""

SCENE = """from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional
from .utils import Plugin, serialize, Ref

@dataclass
class Scene(Plugin):
    integrator: Optional[Plugin] = None
    sensor: Optional[Plugin] = None
    shapes: Dict[str, Plugin] = field(default_factory=dict)
    emitters: Dict[str, Plugin] = field(default_factory=dict)
    media: Dict[str, Plugin] = field(default_factory=dict)
    assets: Dict[str, Plugin] = field(default_factory=dict)  # optional global assets

    def __init__(self, integrator: Optional[Plugin]=None, sensor: Optional[Plugin]=None,
                 shapes: Dict[str, Plugin] | None=None, emitters: Dict[str, Plugin] | None=None,
                 media: Dict[str, Plugin] | None=None, assets: Dict[str, Plugin] | None=None,
                 id: str | None=None):
        super().__init__(type="scene", id=id)
        self.integrator = integrator
        self.sensor = sensor
        self.shapes = {} if shapes is None else shapes
        self.emitters = {} if emitters is None else emitters
        self.media = {} if media is None else media
        self.assets = {} if assets is None else assets

    def add_asset(self, plugin: Plugin) -> Ref:
        if plugin.id is None:
            plugin.id = f"asset_{len(self.assets)+1}"
        self.assets[plugin.id] = plugin
        return Ref(plugin.id)

    def to_dict(self):
        d = {"type":"scene"}
        if self.integrator: d["integrator"] = serialize(self.integrator)
        if self.sensor:     d["sensor"]     = serialize(self.sensor)
        for k,v in self.shapes.items():   d[k] = serialize(v)
        for k,v in self.emitters.items(): d[k] = serialize(v)
        for k,v in self.media.items():    d[k] = serialize(v)
        for k,v in self.assets.items():   d[k] = serialize(v)
        if self.id is not None: d["id"]=self.id
        return d
"""


def fetch(url: str) -> BeautifulSoup:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


CAT_HREF_RE = re.compile(
    r"(?:/src/)?generated/plugins_[^/]+\.html$|plugins_[^/]+\.html$"
)


def discover_category_pages(overview_url: str) -> Dict[str, str]:
    s = fetch(overview_url)
    cats: Dict[str, str] = {}
    for a in s.select("a[href]"):
        href = a.get("href", "")
        if CAT_HREF_RE.search(href):
            url = urljoin(overview_url, href)
            slug = re.sub(r"\.html$", "", href.split("/")[-1]).replace("plugins_", "")
            name = slug.replace("_", " ").title()
            cats[name] = url
    return cats


def section_has_param_table(section: Tag) -> bool:
    for table in section.select("table"):
        heads = [th.get_text(strip=True).lower() for th in table.select("th")]
        if heads and ("parameter" in " ".join(heads) and "type" in " ".join(heads)):
            return True
    return False


def split_names(name: str) -> List[str]:
    parts = [p.strip() for p in (name or "").split(",") if p.strip()]
    return parts if parts else [name]


def extract_params(section: Tag) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for table in section.select("table"):
        heads = [th.get_text(strip=True) for th in table.select("th")]
        h_lower = [h.lower() for h in heads]
        if not ("parameter" in " ".join(h_lower) and "type" in " ".join(h_lower)):
            continue
        idx_name = next((i for i, h in enumerate(h_lower) if "parameter" in h), 0)
        idx_type = next((i for i, h in enumerate(h_lower) if "type" in h), 1)
        idx_desc = next(
            (i for i, h in enumerate(h_lower) if "description" in h or "desc" in h), 2
        )
        idx_flags = next((i for i, h in enumerate(h_lower) if "flags" in h), -1)
        for tr in table.select("tbody tr"):
            tds = tr.select("td")
            if not tds:
                continue
            raw_name = (
                tds[idx_name].get_text(" ", strip=True) if idx_name < len(tds) else ""
            )
            ptype = (
                tds[idx_type].get_text(" ", strip=True) if idx_type < len(tds) else ""
            )
            desc = (
                tds[idx_desc].get_text(" ", strip=True) if idx_desc < len(tds) else ""
            )
            flags = (
                tds[idx_flags].get_text(" ", strip=True)
                if (idx_flags != -1 and idx_flags < len(tds))
                else ""
            )
            for n in split_names(raw_name):
                out.append({"name": n, "type": ptype, "desc": desc, "flags": flags})
        if out:
            break
    return out


def parse_category_page(cat_url: str) -> List[Dict[str, object]]:
    """Parse a category page and return a list of plugin specs."""
    s = fetch(cat_url)
    specs: List[Dict[str, object]] = []
    for section in s.select("div.section, section"):
        h = section.select_one("h2, h3")
        if not h:
            continue
        title_text = h.get_text(" ", strip=True)
        if not section_has_param_table(section):
            continue
        # derive slug
        m = re.search(r"\(([^)]+)\)", title_text)
        slug = None
        if m:
            slug = m.group(1).strip()
        if not slug:
            code = h.select_one("code.literal, code")
            if code:
                slug = code.get_text(strip=True)
        if not slug:
            slug = (
                (h.get("id") or section.get("id") or title_text.split()[0])
                .strip()
                .lower()
            )
        params = extract_params(section)
        specs.append(
            {
                "title": title_text.split("(")[0].strip(),
                "slug": slug,
                "url": cat_url + "#" + (h.get("id") or slug),
                "params": params,
            }
        )
    return specs


# Backward-compat alias for earlier typo
parse_gategory_page = parse_category_page
TYPE_RULES = [
    (re.compile(r"\bfloat\b|\bdouble\b|\bscalar\b", re.I), "float"),
    (re.compile(r"\bint(eger)?\b", re.I), "int"),
    (re.compile(r"\bbool(ean)?\b", re.I), "bool"),
    (re.compile(r"\bstring\b|\bfilename\b|\bpath\b", re.I), "str"),
    (re.compile(r"\brgb\b|\bcolor\b", re.I), "List[float]"),
    (re.compile(r"\bspectrum\b", re.I), "Union[List[float], Plugin]"),
    (re.compile(r"\btransform\b", re.I), "Transform"),
    (
        re.compile(
            r"\b(bsdf|texture|emitter|shape|sensor|film|sampler|medium|phase|filter|spectrum|volume)\b",
            re.I,
        ),
        "Plugin",
    ),
]


def map_type(text: str) -> str:
    t = (text or "").strip()
    for rx, out in TYPE_RULES:
        if rx.search(t):
            return out
    return "Plugin"


def normalize(name: str) -> str:
    n = re.sub(r"\W|^(?=\d)", "_", name).lower().strip("_")
    if n in {"class", "def", "from", "import", "lambda"}:
        n += "_"
    return n or "param"


def camel(title: str) -> str:
    return re.sub(r"[^0-9a-zA-Z]+", "", title.title()) or "PluginClass"


HEADER = """from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform
"""

CLASS_TMPL = """@dataclass
class {cls}(Plugin):
    \"\"\"{title} ({slug})
    {url}
    Params:
{param_docs}
    \"\"\"
{fields}

    def __init__(self, {ctor_args}):
        super().__init__(type="{slug}", id=id)
{assignments}
"""


def render_class(spec: Dict[str, object], category_name: str) -> str:
    title = str(spec["title"])
    slug = str(spec["slug"])
    url = str(spec["url"])
    params = spec.get("params", []) or []
    cls = camel(title if title else slug)

    required_fields = []
    optional_fields = []
    required_ctor = []
    optional_ctor = []
    assigns = ["        self.id = id"]
    docs = []
    seen = set()

    add_shape_bsdf = category_name.lower().startswith("shape")

    def _esc(x: str) -> str:
        x = x or ""
        x = x.replace("\\", r"\\")
        x = x.replace('"""', r"\"\"\"")
        return x

    add_shape_bsdf = category_name.lower().startswith("shape")

    def unique(name: str) -> str:
        base = name
        i = 2
        while name in seen or not name:
            name = f"{base}_{i}"
            i += 1
        seen.add(name)
        return name

    for p in params:
        flags = (p.get("flags", "") or "").lower()
        if any(tag in flags for tag in ("state", "derived", "output")):
            continue
        is_required = "required" in flags

        for raw_name in split_names(p.get("name", "param")):
            nm = normalize(raw_name)
            if nm in seen:
                continue
            base_ann = map_type(p.get("type", ""))
            ann = base_ann if is_required else f"Optional[{base_ann}]"
            nm = unique(nm)

            if is_required:
                required_fields.append(f"    {nm}: {ann}")
                required_ctor.append(f"{nm}: {ann}")
            else:
                optional_fields.append(f"    {nm}: {ann} = None")
                optional_ctor.append(f"{nm}: {ann} = None")

            assigns.append(f"        self.{nm} = {nm}")

            markers = []
            if "p" in flags:
                markers.append("P")
            if "∂" in flags:
                markers.append("∂")
            if "d" in flags:
                markers.append("D")
            marker_str = " | ".join(markers)
            marker_str = f"[{marker_str}]" if len(marker_str) != 0 else ""
            docs.append(
                f"        - {_esc(raw_name)} ({_esc(p.get('type', ''))}): {marker_str} {_esc(p.get('desc', ''))}"
            )

    # Inject optional bsdf for shapes if not already present
    if add_shape_bsdf and "bsdf" not in seen:
        seen.add("bsdf")
        optional_fields.append(f"    bsdf: Optional[Plugin] = None")
        optional_ctor.append(f"bsdf: Optional[Plugin] = None")
        assigns.append(f"        self.bsdf = bsdf")
        docs.append(
            f"        - {_esc(raw_name)} ({_esc(p.get('type', ''))}): [{marker_str}] {_esc(p.get('desc', ''))}"
        )

    # Inject optional bsdf for shapes if not already present
    if add_shape_bsdf and "bsdf" not in seen:
        seen.add("bsdf")
        optional_fields.append(f"    bsdf: Optional[Plugin] = None")
        optional_ctor.append(f"bsdf: Optional[Plugin] = None")
        assigns.append(f"        self.bsdf = bsdf")
        docs.append(f"        - bsdf (bsdf): [P] Surface scattering model")

    fields = required_fields + optional_fields
    if not fields:
        fields = ["    pass"]
        docs = ["        (no parameters documented)"]

    ctor_args = required_ctor + ["id: Optional[str] = None"] + optional_ctor

    return CLASS_TMPL.format(
        cls=cls,
        title=title,
        slug=slug,
        url=url,
        param_docs="\n".join(docs),
        fields="\n".join(fields),
        ctor_args=", ".join(ctor_args),
        assignments="\n".join(assigns),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--overview",
        default="https://mitsuba.readthedocs.io/en/latest/src/plugin_reference.html",
    )
    ap.add_argument("--out", default="./mitsuba-scene-description")
    args = ap.parse_args()

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    # write shared utils and scene
    (outdir / "utils.py").write_text(UTILS)
    (outdir / "scene.py").write_text(SCENE)
    (outdir / "__init__.py").write_text(
        "from .utils import Plugin, RGB, Ref, Transform, serialize\nfrom .scene import Scene\n"
    )

    cats = discover_category_pages(args.overview)
    for name, url in cats.items():
        specs = parse_category_page(url)
        lines = [HEADER, f"# Category: {name}\n"]
        for spec in specs:
            lines.append(render_class(spec, name))
        (outdir / (re.sub(r"\W+", "_", name.lower()) + ".py")).write_text(
            "\n".join(lines)
        )

    with open(outdir / "__init__.py", "a", encoding="utf-8") as f:
        for name in cats:
            f.write(f"from .{re.sub(r'\\W+', '_', name.lower())} import *\n")

    print("Done. Wrote:", outdir.resolve())


if __name__ == "__main__":
    main()
