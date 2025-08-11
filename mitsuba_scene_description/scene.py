from __future__ import annotations
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

    def __init__(
        self,
        integrator: Optional[Plugin] = None,
        sensor: Optional[Plugin] = None,
        shapes: Dict[str, Plugin] | None = None,
        emitters: Dict[str, Plugin] | None = None,
        media: Dict[str, Plugin] | None = None,
        assets: Dict[str, Plugin] | None = None,
        id: str | None = None,
    ):
        super().__init__(type="scene", id=id)
        self.integrator = integrator
        self.sensor = sensor
        self.shapes = {} if shapes is None else shapes
        self.emitters = {} if emitters is None else emitters
        self.media = {} if media is None else media
        self.assets = {} if assets is None else assets

    def add_asset(self, plugin: Plugin) -> Ref:
        if plugin.id is None:
            plugin.id = f"asset_{len(self.assets) + 1}"
        self.assets[plugin.id] = plugin
        return Ref(plugin.id)

    def to_dict(self):
        d = {"type": "scene"}
        if self.integrator:
            d["integrator"] = serialize(self.integrator)
        if self.sensor:
            d["sensor"] = serialize(self.sensor)
        for k, v in self.shapes.items():
            d[k] = serialize(v)
        for k, v in self.emitters.items():
            d[k] = serialize(v)
        for k, v in self.media.items():
            d[k] = serialize(v)
        for k, v in self.assets.items():
            d[k] = serialize(v)
        if self.id is not None:
            d["id"] = self.id
        return d
