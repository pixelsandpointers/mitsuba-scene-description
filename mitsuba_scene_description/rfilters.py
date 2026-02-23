from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform, ProjectiveTransform

# Category: Rfilters

@dataclass
class BoxFilter(Plugin):
    """Box filter (box)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_rfilters.html#box
    Params:
        - radius (float):  Specifies the radius of the tent function (Default: 1.0)
    """
    radius: Optional[float] = None

    def __init__(self, id: Optional[str] = None, radius: Optional[float] = None):
        super().__init__(type="box", id=id)
        self.id = id
        self.radius = radius

@dataclass
class TentFilter(Plugin):
    """Tent filter (tent)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_rfilters.html#tent
    Params:
        - radius (float):  Specifies the radius of the tent function (Default: 1.0)
    """
    radius: Optional[float] = None

    def __init__(self, id: Optional[str] = None, radius: Optional[float] = None):
        super().__init__(type="tent", id=id)
        self.id = id
        self.radius = radius

@dataclass
class GaussianFilter(Plugin):
    """Gaussian filter (gaussian)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_rfilters.html#gaussian
    Params:
        - stddev (float):  Specifies the standard deviation (Default: 0.5)
    """
    stddev: Optional[float] = None

    def __init__(self, id: Optional[str] = None, stddev: Optional[float] = None):
        super().__init__(type="gaussian", id=id)
        self.id = id
        self.stddev = stddev

@dataclass
class MitchellFilter(Plugin):
    """Mitchell filter (mitchell)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_rfilters.html#mitchell
    Params:
        - A (float):  A parameter in the original paper (Default: \\(1/3\\) )
        - B (float):  B parameter in the original paper (Default: \\(1/3\\) )
    """
    a: Optional[float] = None
    b: Optional[float] = None

    def __init__(self, id: Optional[str] = None, a: Optional[float] = None, b: Optional[float] = None):
        super().__init__(type="mitchell", id=id)
        self.id = id
        self.a = a
        self.b = b

@dataclass
class LanczosFilter(Plugin):
    """Lanczos filter (lanczos)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_rfilters.html#lanczos
    Params:
        - lobes (integer):  Sets the desired number of filter side-lobes. The higher, the closer the
filter will approximate an optimal low-pass filter, but this also increases
ringing. Values of 2 or 3 are common (Default: 3)
    """
    lobes: Optional[int] = None

    def __init__(self, id: Optional[str] = None, lobes: Optional[int] = None):
        super().__init__(type="lanczos", id=id)
        self.id = id
        self.lobes = lobes
