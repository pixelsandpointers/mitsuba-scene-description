from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Phase


@dataclass
class IsotropicPhaseFunction(Plugin):
    """Isotropic phase function (isotropic)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_phase.html#isotropic
        Params:
            - g (float): [P | ∂ | D] This parameter must be somewhere in the range -1 to 1
    (but not equal to -1 or 1). It denotes the mean cosine of scattering
    interactions. A value greater than zero indicates that medium interactions
    predominantly scatter incident light into a similar direction (i.e. the
    medium is forward-scattering ), whereas values smaller than zero cause
    the medium to be scatter more light in the opposite direction.
    """

    g: Optional[float] = None

    def __init__(self, id: Optional[str] = None, g: Optional[float] = None):
        super().__init__(type="isotropic", id=id)
        self.id = id
        self.g = g


@dataclass
class HenyeyGreensteinPhaseFunction(Plugin):
    """Henyey-Greenstein phase function (hg)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_phase.html#hg
        Params:
            - g (float): [P | ∂ | D] This parameter must be somewhere in the range -1 to 1
    (but not equal to -1 or 1). It denotes the mean cosine of scattering
    interactions. A value greater than zero indicates that medium interactions
    predominantly scatter incident light into a similar direction (i.e. the
    medium is forward-scattering ), whereas values smaller than zero cause
    the medium to be scatter more light in the opposite direction.
    """

    g: Optional[float] = None

    def __init__(self, id: Optional[str] = None, g: Optional[float] = None):
        super().__init__(type="hg", id=id)
        self.id = id
        self.g = g


@dataclass
class SggxPhaseFunction(Plugin):
    """SGGX phase function (sggx)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_phase.html#sggx
        Params:
            - S (volume): [P | ∂] A volume containing the SGGX parameters. The phase function is parametrized
    by six values \\(S_{xx}\\) , \\(S_{yy}\\) , \\(S_{zz}\\) , \\(S_{xy}\\) , \\(S_{xz}\\) and \\(S_{yz}\\) (see below for their meaning). The parameters can either be specified as a constvolume with six values or as a gridvolume with six channels.
    """

    s: Optional[Plugin] = None

    def __init__(self, id: Optional[str] = None, s: Optional[Plugin] = None):
        super().__init__(type="sggx", id=id)
        self.id = id
        self.s = s


@dataclass
class BlendedPhaseFunction(Plugin):
    """Blended phase function (blendphase)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_phase.html#blendphase
        Params:
            - weight (float or texture): [P | ∂] A floating point value or texture with values between zero and one.
    The extreme values zero and one activate the first and second nested phase
    function respectively, and in-between values interpolate accordingly.
    (Default: 0.5)
            - (Nested plugin) (phase): [P | ∂] Two nested phase function instances that should be mixed according to the
    specified blending weight
    """

    weight: Optional[float] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        weight: Optional[float] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="blendphase", id=id)
        self.id = id
        self.weight = weight
        self.nested_plugin = nested_plugin


@dataclass
class LookupTablePhaseFunction(Plugin):
    """Lookup table phase function (tabphase)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_phase.html#tabphase
        Params:
            - values (string): [P | ∂ | D] A comma-separated list of phase function values parametrized by the
    cosine of the scattering angle.
    """

    values: Optional[str] = None

    def __init__(self, id: Optional[str] = None, values: Optional[str] = None):
        super().__init__(type="tabphase", id=id)
        self.id = id
        self.values = values
