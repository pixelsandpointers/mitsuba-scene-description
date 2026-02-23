from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform, ProjectiveTransform

# Category: Spectra

@dataclass
class UniformSpectrum(Plugin):
    """Uniform spectrum (uniform)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_spectra.html#uniform
    Params:
        - wavelength_min (float):  Lower bound of the wavelength sampling range in nanometers. Default: 360 nm
        - wavelength_max (float):  Upper bound of the wavelength sampling range in nanometers. Default: 830 nm
        - value (float): [P | ∂] Value of the spectral function across the specified spectral range.
    """
    wavelength_min: Optional[float] = None
    wavelength_max: Optional[float] = None
    value: Optional[float] = None

    def __init__(self, id: Optional[str] = None, wavelength_min: Optional[float] = None, wavelength_max: Optional[float] = None, value: Optional[float] = None):
        super().__init__(type="uniform", id=id)
        self.id = id
        self.wavelength_min = wavelength_min
        self.wavelength_max = wavelength_max
        self.value = value

@dataclass
class RegularSpectrum(Plugin):
    """Regular spectrum (regular)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_spectra.html#regular
    Params:
        - wavelength_min (float):  Minimum wavelength of the spectral range in nanometers.
        - wavelength_max (float):  Maximum wavelength of the spectral range in nanometers.
        - values (string): [P | ∂] Values of the spectral function at spectral range extremities.
        - range (string): [P | ∂] Spectral emission range.
    """
    wavelength_min: Optional[float] = None
    wavelength_max: Optional[float] = None
    values: Optional[str] = None
    range: Optional[str] = None

    def __init__(self, id: Optional[str] = None, wavelength_min: Optional[float] = None, wavelength_max: Optional[float] = None, values: Optional[str] = None, range: Optional[str] = None):
        super().__init__(type="regular", id=id)
        self.id = id
        self.wavelength_min = wavelength_min
        self.wavelength_max = wavelength_max
        self.values = values
        self.range = range

@dataclass
class IrregularSpectrum(Plugin):
    """Irregular spectrum (irregular)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_spectra.html#irregular
    Params:
        - wavelengths (string): [P | ∂] Wavelength values where the function is defined.
        - values (string): [P | ∂] Values of the spectral function at the specified wavelengths.
    """
    wavelengths: Optional[str] = None
    values: Optional[str] = None

    def __init__(self, id: Optional[str] = None, wavelengths: Optional[str] = None, values: Optional[str] = None):
        super().__init__(type="irregular", id=id)
        self.id = id
        self.wavelengths = wavelengths
        self.values = values

@dataclass
class SrgbSpectrum(Plugin):
    """sRGB spectrum (srgb)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_spectra.html#srgb
    Params:
        - color (color):  The corresponding sRGB color value.
        - value (color): [P | ∂] Spectral upsampling model coefficients of the srgb color value.
    """
    color: Optional[List[float]] = None
    value: Optional[List[float]] = None

    def __init__(self, id: Optional[str] = None, color: Optional[List[float]] = None, value: Optional[List[float]] = None):
        super().__init__(type="srgb", id=id)
        self.id = id
        self.color = color
        self.value = value

@dataclass
class D65Spectrum(Plugin):
    """D65 spectrum (d65)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_spectra.html#d65
    Params:
        - color (color):  The corresponding sRGB color value.
        - scale (float):  Optional scaling factor applied to the emitted spectrum. (Default: 1.0)
        - (Nested plugin) (texture): [P | ∂] Underlying texture/spectra to be multiplied by D65.
    """
    color: Optional[List[float]] = None
    scale: Optional[float] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(self, id: Optional[str] = None, color: Optional[List[float]] = None, scale: Optional[float] = None, nested_plugin: Optional[Plugin] = None):
        super().__init__(type="d65", id=id)
        self.id = id
        self.color = color
        self.scale = scale
        self.nested_plugin = nested_plugin

@dataclass
class RawConstantValuedTexture(Plugin):
    """Raw constant-valued texture (rawconstant)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_spectra.html#rawconstant
    Params:
        - value (float or vector): [P | ∂] The constant value(s) to be returned. Can be a single float or a 3D vector.
    """
    value: Optional[float] = None

    def __init__(self, id: Optional[str] = None, value: Optional[float] = None):
        super().__init__(type="rawconstant", id=id)
        self.id = id
        self.value = value

@dataclass
class BlackbodySpectrum(Plugin):
    """Blackbody spectrum (blackbody)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_spectra.html#blackbody
    Params:
        - wavelength_min (float):  Minimum wavelength of the spectral range in nanometers. (Default: 360nm)
        - wavelength_max (float):  Maximum wavelength of the spectral range in nanometers. (Default: 830nm)
        - temperature (float): [P] Black body temperature in Kelvins.
    """
    wavelength_min: Optional[float] = None
    wavelength_max: Optional[float] = None
    temperature: Optional[float] = None

    def __init__(self, id: Optional[str] = None, wavelength_min: Optional[float] = None, wavelength_max: Optional[float] = None, temperature: Optional[float] = None):
        super().__init__(type="blackbody", id=id)
        self.id = id
        self.wavelength_min = wavelength_min
        self.wavelength_max = wavelength_max
        self.temperature = temperature
