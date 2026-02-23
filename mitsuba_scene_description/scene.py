from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Self, Union
from .utils import Plugin, serialize, Ref

@dataclass
class Scene(Plugin):
    integrator: Optional[Plugin] = None
    sensors: List[Plugin] = field(default_factory=list)
    shapes: Dict[str, Plugin] = field(default_factory=dict)
    emitters: Dict[str, Plugin] = field(default_factory=dict)
    media: Dict[str, Plugin] = field(default_factory=dict)
    assets: Dict[str, Plugin] = field(default_factory=dict)

    def __init__(self, integrator: Optional[Plugin]=None,
                 sensors: Union[List[Plugin], Plugin, None]=None,
                 shapes: Dict[str, Plugin] | None=None,
                 emitters: Dict[str, Plugin] | None=None,
                 media: Dict[str, Plugin] | None=None,
                 assets: Dict[str, Plugin] | None=None,
                 id: str | None=None):
        super().__init__(type="scene", id=id)
        self.integrator = integrator
        if sensors is None:
            self.sensors = []
        elif isinstance(sensors, list):
            self.sensors = sensors
        else:
            self.sensors = [sensors]
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
        if len(self.sensors) == 1:
            d["sensor"] = serialize(self.sensors[0])
        else:
            for i, s in enumerate(self.sensors):
                d[f"sensor_{i}"] = serialize(s)
        for k,v in self.shapes.items():   d[k] = serialize(v)
        for k,v in self.emitters.items(): d[k] = serialize(v)
        for k,v in self.media.items():    d[k] = serialize(v)
        for k,v in self.assets.items():   d[k] = serialize(v)
        if self.id is not None: d["id"]=self.id
        return d

class SceneBuilder:
    """Fluent builder for constructing a Scene step-by-step."""

    def __init__(self) -> None:
        self._integrator: Optional[Plugin] = None
        self._sensors: List[Plugin] = []
        self._shapes: Dict[str, Plugin] = {}
        self._emitters: Dict[str, Plugin] = {}
        self._media: Dict[str, Plugin] = {}
        self._assets: Dict[str, Plugin] = {}
        self._id: Optional[str] = None

    def integrator(self, plugin: Plugin) -> Self:
        self._integrator = plugin
        return self

    def sensor(self, plugin: Plugin) -> Self:
        self._sensors.append(plugin)
        return self

    def shape(self, name: str, plugin: Plugin) -> Self:
        self._shapes[name] = plugin
        return self

    def emitter(self, name: str, plugin: Plugin) -> Self:
        self._emitters[name] = plugin
        return self

    def medium(self, name: str, plugin: Plugin) -> Self:
        self._media[name] = plugin
        return self

    def asset(self, plugin: Plugin) -> Self:
        if plugin.id is None:
            plugin.id = f"asset_{len(self._assets)+1}"
        self._assets[plugin.id] = plugin
        return self

    def id(self, id: str) -> Self:
        self._id = id
        return self

    def build(self) -> Scene:
        return Scene(
            integrator=self._integrator,
            sensors=self._sensors,
            shapes=self._shapes,
            emitters=self._emitters,
            media=self._media,
            assets=self._assets,
            id=self._id,
        )
