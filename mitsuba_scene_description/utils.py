from __future__ import annotations
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
    """Chainable affine transform builder (translate, scale, rotate, look_at).

    Produces a ``mi.ScalarTransform4f``.
    """
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

class ProjectiveTransform(Transform):
    """Chainable projective transform builder (Mitsuba >= 3.7).

    Extends :class:`Transform` with ``perspective()`` and ``orthographic()``.
    Produces a ``mi.ScalarProjectiveTransform4f``.
    """
    __slots__ = ("_ops",)
    def perspective(self, fov: float, near: float, far: float) -> "ProjectiveTransform":
        self._ops.append({"op":"perspective","fov":fov,"near":near,"far":far}); return self
    def orthographic(self, near: float, far: float) -> "ProjectiveTransform":
        self._ops.append({"op":"orthographic","near":near,"far":far}); return self
    def to_mi(self):
        import mitsuba as mi
        T = mi.ScalarProjectiveTransform4f
        cur = T()
        for step in self._ops:
            op = step["op"]
            if op == "translate": piece = T().translate(step["value"])
            elif op == "scale": piece = T().scale(step["value"])
            elif op == "rotate": piece = T().rotate(axis=step["axis"], angle=step["angle"])
            elif op == "look_at": piece = T().look_at(origin=step["origin"], target=step["target"], up=step["up"])
            elif op == "perspective": piece = T().perspective(fov=step["fov"], near=step["near"], far=step["far"])
            elif op == "orthographic": piece = T().orthographic(near=step["near"], far=step["far"])
            elif op == "matrix": piece = T(step["matrix"])
            else: continue
            cur = piece @ cur
        return cur
