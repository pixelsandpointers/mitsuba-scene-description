from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Bsdfs


@dataclass
class SmoothDiffuseMaterial(Plugin):
    """Smooth diffuse material (diffuse)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#diffuse
    Params:
        - reflectance (spectrum or texture): [P | ∂] Specifies the diffuse albedo of the material (Default: 0.5)
    """

    reflectance: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self,
        id: Optional[str] = None,
        reflectance: Optional[Union[List[float], Plugin]] = None,
    ):
        super().__init__(type="diffuse", id=id)
        self.id = id
        self.reflectance = reflectance


@dataclass
class SmoothDielectricMaterial(Plugin):
    """Smooth dielectric material (dielectric)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#dielectric
    Params:
        - int_ior (float or string):  Interior index of refraction specified numerically or using a known material name. (Default: bk7 / 1.5046)
        - ext_ior (float or string):  Exterior index of refraction specified numerically or using a known material name.  (Default: air / 1.000277)
        - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection component. Note that for physical realism, this parameter should never be touched. (Default: 1.0)
        - specular_transmittance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular transmission component. Note that for physical realism, this parameter should never be touched. (Default: 1.0)
        - eta (float): [P] Relative index of refraction from the exterior to the interior
    """

    int_ior: Optional[float] = None
    ext_ior: Optional[float] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None
    specular_transmittance: Optional[Union[List[float], Plugin]] = None
    eta: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        int_ior: Optional[float] = None,
        ext_ior: Optional[float] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
        specular_transmittance: Optional[Union[List[float], Plugin]] = None,
        eta: Optional[float] = None,
    ):
        super().__init__(type="dielectric", id=id)
        self.id = id
        self.int_ior = int_ior
        self.ext_ior = ext_ior
        self.specular_reflectance = specular_reflectance
        self.specular_transmittance = specular_transmittance
        self.eta = eta


@dataclass
class ThinDielectricMaterial(Plugin):
    """Thin dielectric material (thindielectric)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#thindielectric
    Params:
        - int_ior (float or string):  Interior index of refraction specified numerically or using a known material name. (Default: bk7 / 1.5046)
        - ext_ior (float or string):  Exterior index of refraction specified numerically or using a known material name.  (Default: air / 1.000277)
        - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection component. Note that for physical realism, this parameter should never be touched. (Default: 1.0)
        - specular_transmittance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular transmission component. Note that for physical realism, this parameter should never be touched. (Default: 1.0)
        - eta (float): [P | ∂ | D] Relative index of refraction from the exterior to the interior
    """

    int_ior: Optional[float] = None
    ext_ior: Optional[float] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None
    specular_transmittance: Optional[Union[List[float], Plugin]] = None
    eta: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        int_ior: Optional[float] = None,
        ext_ior: Optional[float] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
        specular_transmittance: Optional[Union[List[float], Plugin]] = None,
        eta: Optional[float] = None,
    ):
        super().__init__(type="thindielectric", id=id)
        self.id = id
        self.int_ior = int_ior
        self.ext_ior = ext_ior
        self.specular_reflectance = specular_reflectance
        self.specular_transmittance = specular_transmittance
        self.eta = eta


@dataclass
class RoughDielectricMaterial(Plugin):
    """Rough dielectric material (roughdielectric)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#roughdielectric
        Params:
            - int_ior (float or string):  Interior index of refraction specified numerically or using a known material name. (Default: bk7 / 1.5046)
            - ext_ior (float or string):  Exterior index of refraction specified numerically or using a known material name.  (Default: air / 1.000277)
            - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection/transmission components.
    Note that for physical realism, these parameters should never be touched. (Default: 1.0)
            - specular_transmittance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection/transmission components.
    Note that for physical realism, these parameters should never be touched. (Default: 1.0)
            - distribution (string):  Specifies the type of microfacet normal distribution used to model the surface roughness. beckmann : Physically-based distribution derived from Gaussian random surfaces.
    This is the default. ggx : The GGX [ WMLT07 ] distribution (also known as Trowbridge-Reitz [ TR75 ] distribution) was designed to better approximate the long
    tails observed in measurements of ground surfaces, which are not modeled by the Beckmann
    distribution.
            - alpha (texture or float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. alpha is a convenience
    parameter to initialize both alpha_u and alpha_v to the same value. (Default: 0.1)
            - alpha_u (texture or float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. alpha is a convenience
    parameter to initialize both alpha_u and alpha_v to the same value. (Default: 0.1)
            - alpha_v (texture or float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. alpha is a convenience
    parameter to initialize both alpha_u and alpha_v to the same value. (Default: 0.1)
            - sample_visible (boolean):  Enables a sampling technique proposed by Heitz and D’Eon [ HDEon14 ] , which
    focuses computation on the visible parts of the microfacet normal distribution, considerably
    reducing variance in some cases. (Default: true , i.e. use visible normal sampling)
            - eta (float): [P | ∂ | D] Relative index of refraction from the exterior to the interior
    """

    int_ior: Optional[float] = None
    ext_ior: Optional[float] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None
    specular_transmittance: Optional[Union[List[float], Plugin]] = None
    distribution: Optional[str] = None
    alpha: Optional[float] = None
    alpha_u: Optional[float] = None
    alpha_v: Optional[float] = None
    sample_visible: Optional[bool] = None
    eta: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        int_ior: Optional[float] = None,
        ext_ior: Optional[float] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
        specular_transmittance: Optional[Union[List[float], Plugin]] = None,
        distribution: Optional[str] = None,
        alpha: Optional[float] = None,
        alpha_u: Optional[float] = None,
        alpha_v: Optional[float] = None,
        sample_visible: Optional[bool] = None,
        eta: Optional[float] = None,
    ):
        super().__init__(type="roughdielectric", id=id)
        self.id = id
        self.int_ior = int_ior
        self.ext_ior = ext_ior
        self.specular_reflectance = specular_reflectance
        self.specular_transmittance = specular_transmittance
        self.distribution = distribution
        self.alpha = alpha
        self.alpha_u = alpha_u
        self.alpha_v = alpha_v
        self.sample_visible = sample_visible
        self.eta = eta


@dataclass
class SmoothConductor(Plugin):
    """Smooth conductor (conductor)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#conductor
        Params:
            - material (string):  Name of the material preset, see conductor-ior-list . (Default: none)
            - eta (spectrum or texture): [P | ∂ | D] Real and imaginary components of the material’s index of refraction. (Default: based on the value of material )
            - k (spectrum or texture): [P | ∂ | D] Real and imaginary components of the material’s index of refraction. (Default: based on the value of material )
            - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection component.
    Note that for physical realism, this parameter should never be touched. (Default: 1.0)
    """

    material: Optional[str] = None
    eta: Optional[Union[List[float], Plugin]] = None
    k: Optional[Union[List[float], Plugin]] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self,
        id: Optional[str] = None,
        material: Optional[str] = None,
        eta: Optional[Union[List[float], Plugin]] = None,
        k: Optional[Union[List[float], Plugin]] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
    ):
        super().__init__(type="conductor", id=id)
        self.id = id
        self.material = material
        self.eta = eta
        self.k = k
        self.specular_reflectance = specular_reflectance


@dataclass
class RoughConductorMaterial(Plugin):
    """Rough conductor material (roughconductor)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#roughconductor
        Params:
            - material (string):  Name of the material preset, see conductor-ior-list . (Default: none)
            - eta (spectrum or texture): [P | ∂ | D] Real and imaginary components of the material’s index of refraction. (Default: based on the value of material )
            - k (spectrum or texture): [P | ∂ | D] Real and imaginary components of the material’s index of refraction. (Default: based on the value of material )
            - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection component.
    Note that for physical realism, this parameter should never be touched. (Default: 1.0)
            - distribution (string):  Specifies the type of microfacet normal distribution used to model the surface roughness. beckmann : Physically-based distribution derived from Gaussian random surfaces.
    This is the default. ggx : The GGX [ WMLT07 ] distribution (also known as Trowbridge-Reitz [ TR75 ] distribution) was designed to better approximate the long
    tails observed in measurements of ground surfaces, which are not modeled by the Beckmann
    distribution.
            - alpha (texture or float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. alpha is a convenience
    parameter to initialize both alpha_u and alpha_v to the same value. (Default: 0.1)
            - alpha_u (texture or float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. alpha is a convenience
    parameter to initialize both alpha_u and alpha_v to the same value. (Default: 0.1)
            - alpha_v (texture or float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. alpha is a convenience
    parameter to initialize both alpha_u and alpha_v to the same value. (Default: 0.1)
            - sample_visible (boolean):  Enables a sampling technique proposed by Heitz and D’Eon [ HDEon14 ] , which
    focuses computation on the visible parts of the microfacet normal distribution, considerably
    reducing variance in some cases. (Default: true , i.e. use visible normal sampling)
    """

    material: Optional[str] = None
    eta: Optional[Union[List[float], Plugin]] = None
    k: Optional[Union[List[float], Plugin]] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None
    distribution: Optional[str] = None
    alpha: Optional[float] = None
    alpha_u: Optional[float] = None
    alpha_v: Optional[float] = None
    sample_visible: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        material: Optional[str] = None,
        eta: Optional[Union[List[float], Plugin]] = None,
        k: Optional[Union[List[float], Plugin]] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
        distribution: Optional[str] = None,
        alpha: Optional[float] = None,
        alpha_u: Optional[float] = None,
        alpha_v: Optional[float] = None,
        sample_visible: Optional[bool] = None,
    ):
        super().__init__(type="roughconductor", id=id)
        self.id = id
        self.material = material
        self.eta = eta
        self.k = k
        self.specular_reflectance = specular_reflectance
        self.distribution = distribution
        self.alpha = alpha
        self.alpha_u = alpha_u
        self.alpha_v = alpha_v
        self.sample_visible = sample_visible


@dataclass
class HairMaterial(Plugin):
    """Hair material (hair)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#hair
        Params:
            - eumelanin (float): [P | ∂ | D] Concentration of pigments (Default: 1.3 eumelanin and 0.2 pheomelanin)
            - pheomelanin (float): [P | ∂ | D] Concentration of pigments (Default: 1.3 eumelanin and 0.2 pheomelanin)
            - sigma_a (spectrum or texture): [P | ∂] Absorption coefficient in inverse scene units. The absorption can either
    be specified with pigmentation concentrations or this parameter, not both.
            - scale (float): [P] Optional scale factor that will be applied to the sigma_a parameter.
    (Default :1)
            - int_ior (float or string):  Interior index of refraction specified numerically or using a known
    material name. (Default: amber / 1.55f)
            - ext_ior (float or string):  Exterior index of refraction specified numerically or using a known
    material name.  (Default: air / 1.000277)
            - longitudinal_roughness (float): [P | ∂ | D] Hair roughness along each dimension (Default: 0.3 for both)
            - azimuthal_roughness (float): [P | ∂ | D] Hair roughness along each dimension (Default: 0.3 for both)
            - scale_tilt (float): [P | ∂ | D] Angle of the scales on the hair w.r.t. to the hair fiber’s surface. The
    angle is given in degrees. (Default: 2)
            - use_pigmentation (boolean): [P | ∂ | D] Specifies whether to use the pigmentation concentration values or the
    absorption coefficient sigma_a
            - eta (float): [P | ∂ | D] Relative index of refraction from the exterior to the interior
    """

    eumelanin: Optional[float] = None
    pheomelanin: Optional[float] = None
    sigma_a: Optional[Union[List[float], Plugin]] = None
    scale: Optional[float] = None
    int_ior: Optional[float] = None
    ext_ior: Optional[float] = None
    longitudinal_roughness: Optional[float] = None
    azimuthal_roughness: Optional[float] = None
    scale_tilt: Optional[float] = None
    use_pigmentation: Optional[bool] = None
    eta: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        eumelanin: Optional[float] = None,
        pheomelanin: Optional[float] = None,
        sigma_a: Optional[Union[List[float], Plugin]] = None,
        scale: Optional[float] = None,
        int_ior: Optional[float] = None,
        ext_ior: Optional[float] = None,
        longitudinal_roughness: Optional[float] = None,
        azimuthal_roughness: Optional[float] = None,
        scale_tilt: Optional[float] = None,
        use_pigmentation: Optional[bool] = None,
        eta: Optional[float] = None,
    ):
        super().__init__(type="hair", id=id)
        self.id = id
        self.eumelanin = eumelanin
        self.pheomelanin = pheomelanin
        self.sigma_a = sigma_a
        self.scale = scale
        self.int_ior = int_ior
        self.ext_ior = ext_ior
        self.longitudinal_roughness = longitudinal_roughness
        self.azimuthal_roughness = azimuthal_roughness
        self.scale_tilt = scale_tilt
        self.use_pigmentation = use_pigmentation
        self.eta = eta


@dataclass
class MeasuredMaterial(Plugin):
    """Measured material (measured)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#measured
    Params:
        - filename (string):  Filename of the material data file to be loaded
    """

    filename: Optional[str] = None

    def __init__(self, id: Optional[str] = None, filename: Optional[str] = None):
        super().__init__(type="measured", id=id)
        self.id = id
        self.filename = filename


@dataclass
class MeasuredPolarizedMaterial(Plugin):
    """Measured polarized material (measured_polarized)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#measured_polarized
        Params:
            - filename (string):  Filename of the material data file to be loaded
            - alpha_sample (float):  Specifies which roughness value should be used for the internal Microfacet
    importance sampling routine. (Default: 0.1)
            - wavelength (float):  Specifies if the material should only be rendered for just one specific wavelength.
    The valid range is between 450 and 650 nm.
    A value of -1 means the full spectrally-varying pBRDF will be used.
    (Default: -1, i.e. all wavelengths.)
    """

    filename: Optional[str] = None
    alpha_sample: Optional[float] = None
    wavelength: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        alpha_sample: Optional[float] = None,
        wavelength: Optional[float] = None,
    ):
        super().__init__(type="measured_polarized", id=id)
        self.id = id
        self.filename = filename
        self.alpha_sample = alpha_sample
        self.wavelength = wavelength


@dataclass
class SmoothPlasticMaterial(Plugin):
    """Smooth plastic material (plastic)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#plastic
        Params:
            - diffuse_reflectance (spectrum or texture): [P | ∂] Optional factor used to modulate the diffuse reflection component. (Default: 0.5)
            - nonlinear (boolean):  Account for nonlinear color shifts due to internal scattering? See the main text for details..
    (Default: Don’t account for them and preserve the texture colors, i.e. false )
            - int_ior (float or string):  Interior index of refraction specified numerically or using a known material name.
    (Default: polypropylene / 1.49)
            - ext_ior (float or string):  Exterior index of refraction specified numerically or using a known material name.
    (Default: air / 1.000277)
            - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection component. Note that for
    physical realism, this parameter should never be touched. (Default: 1.0)
            - eta (float): [P] Relative index of refraction from the exterior to the interior
    """

    diffuse_reflectance: Optional[Union[List[float], Plugin]] = None
    nonlinear: Optional[bool] = None
    int_ior: Optional[float] = None
    ext_ior: Optional[float] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None
    eta: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        diffuse_reflectance: Optional[Union[List[float], Plugin]] = None,
        nonlinear: Optional[bool] = None,
        int_ior: Optional[float] = None,
        ext_ior: Optional[float] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
        eta: Optional[float] = None,
    ):
        super().__init__(type="plastic", id=id)
        self.id = id
        self.diffuse_reflectance = diffuse_reflectance
        self.nonlinear = nonlinear
        self.int_ior = int_ior
        self.ext_ior = ext_ior
        self.specular_reflectance = specular_reflectance
        self.eta = eta


@dataclass
class RoughPlasticMaterial(Plugin):
    """Rough plastic material (roughplastic)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#roughplastic
        Params:
            - diffuse_reflectance (spectrum or texture): [P | ∂] Optional factor used to modulate the diffuse reflection component. (Default: 0.5)
            - nonlinear (boolean):  Account for nonlinear color shifts due to internal scattering? See the plastic plugin for details.
    default{Don’t account for them and preserve the texture colors. (Default: false )
            - int_ior (float or string):  Interior index of refraction specified numerically or using a known material name. (Default: polypropylene / 1.49)
            - ext_ior (float or string):  Exterior index of refraction specified numerically or using a known material name.  (Default: air / 1.000277)
            - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection component.
    Note that for physical realism, this parameter should never be touched. (Default: 1.0)
            - distribution (string):  Specifies the type of microfacet normal distribution used to model the surface roughness. beckmann : Physically-based distribution derived from Gaussian random surfaces.
    This is the default. ggx : The GGX [ WMLT07 ] distribution (also known as Trowbridge-Reitz [ TR75 ] distribution) was designed to better approximate the long
    tails observed in measurements of ground surfaces, which are not modeled by the Beckmann
    distribution.
            - alpha (float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. (Default: 0.1)
            - sample_visible (boolean):  Enables a sampling technique proposed by Heitz and D’Eon [ HDEon14 ] , which
    focuses computation on the visible parts of the microfacet normal distribution, considerably
    reducing variance in some cases. (Default: true , i.e. use visible normal sampling)
            - eta (float): [P | ∂ | D] Relative index of refraction from the exterior to the interior
    """

    diffuse_reflectance: Optional[Union[List[float], Plugin]] = None
    nonlinear: Optional[bool] = None
    int_ior: Optional[float] = None
    ext_ior: Optional[float] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None
    distribution: Optional[str] = None
    alpha: Optional[float] = None
    sample_visible: Optional[bool] = None
    eta: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        diffuse_reflectance: Optional[Union[List[float], Plugin]] = None,
        nonlinear: Optional[bool] = None,
        int_ior: Optional[float] = None,
        ext_ior: Optional[float] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
        distribution: Optional[str] = None,
        alpha: Optional[float] = None,
        sample_visible: Optional[bool] = None,
        eta: Optional[float] = None,
    ):
        super().__init__(type="roughplastic", id=id)
        self.id = id
        self.diffuse_reflectance = diffuse_reflectance
        self.nonlinear = nonlinear
        self.int_ior = int_ior
        self.ext_ior = ext_ior
        self.specular_reflectance = specular_reflectance
        self.distribution = distribution
        self.alpha = alpha
        self.sample_visible = sample_visible
        self.eta = eta


@dataclass
class BumpMapBsdfAdapter(Plugin):
    """Bump map BSDF adapter (bumpmap)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#bumpmap
    Params:
        - (Nested plugin) (texture): [P | ∂ | D] Specifies the bump map texture.
        - scale (float): [P] Bump map gradient multiplier. (Default: 1.0)
    """

    nested_plugin: Optional[Plugin] = None
    scale: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        nested_plugin: Optional[Plugin] = None,
        scale: Optional[float] = None,
    ):
        super().__init__(type="bumpmap", id=id)
        self.id = id
        self.nested_plugin = nested_plugin
        self.scale = scale


@dataclass
class NormalMapBsdf(Plugin):
    """Normal map BSDF (normalmap)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#normalmap
    Params:
        - normalmap (texture): [P | ∂ | D] The color values of this texture specify the perturbed normals relative in the local surface coordinate system
        - (Nested plugin) (bsdf): [P | ∂] A BSDF model that should be affected by the normal map
    """

    normalmap: Optional[Plugin] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        normalmap: Optional[Plugin] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="normalmap", id=id)
        self.id = id
        self.normalmap = normalmap
        self.nested_plugin = nested_plugin


@dataclass
class BlendedMaterial(Plugin):
    """Blended material (blendbsdf)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#blendbsdf
        Params:
            - weight (float or texture): [P | ∂] A floating point value or texture with values between zero and one. The extreme values zero and
    one activate the first and second nested BSDF respectively, and in-between values interpolate
    accordingly. (Default: 0.5)
            - (Nested plugin) (bsdf): [P | ∂] Two nested BSDF instances that should be mixed according to the specified blending weight
    """

    weight: Optional[float] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        weight: Optional[float] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="blendbsdf", id=id)
        self.id = id
        self.weight = weight
        self.nested_plugin = nested_plugin


@dataclass
class OpacityMask(Plugin):
    """Opacity mask (mask)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#mask
    Params:
        - opacity (spectrum or texture): [P | ∂ | D] Specifies the opacity (where 1=completely opaque) (Default: 0.5)
        - (Nested plugin) (bsdf): [P | ∂] A base BSDF model that represents the non-transparent portion of the scattering
    """

    opacity: Optional[Union[List[float], Plugin]] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        opacity: Optional[Union[List[float], Plugin]] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="mask", id=id)
        self.id = id
        self.opacity = opacity
        self.nested_plugin = nested_plugin


@dataclass
class TwoSidedBrdfAdapter(Plugin):
    """Two-sided BRDF adapter (twosided)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#twosided
    Params:
        - (Nested plugin) (bsdf): [P | ∂] A nested BRDF that should be turned into a two-sided scattering model. If two BRDFs are specified, they will be placed on the front and back side, respectively
    """

    nested_plugin: Optional[Plugin] = None

    def __init__(
        self, id: Optional[str] = None, nested_plugin: Optional[Plugin] = None
    ):
        super().__init__(type="twosided", id=id)
        self.id = id
        self.nested_plugin = nested_plugin


@dataclass
class LinearPolarizerMaterial(Plugin):
    """Linear polarizer material (polarizer)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#polarizer
        Params:
            - theta (spectrum or texture): [P | ∂ | D] Specifies the rotation angle (in degrees) of the polarizer around the optical axis (Default: 0.0)
            - transmittance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular transmission. (Default: 1.0)
            - polarizing (boolean):  Optional flag to disable polarization changes in order to use this as a neutral density filter,
    even in polarized render modes. (Default: true , i.e. act as polarizer)
    """

    theta: Optional[Union[List[float], Plugin]] = None
    transmittance: Optional[Union[List[float], Plugin]] = None
    polarizing: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        theta: Optional[Union[List[float], Plugin]] = None,
        transmittance: Optional[Union[List[float], Plugin]] = None,
        polarizing: Optional[bool] = None,
    ):
        super().__init__(type="polarizer", id=id)
        self.id = id
        self.theta = theta
        self.transmittance = transmittance
        self.polarizing = polarizing


@dataclass
class LinearRetarderMaterial(Plugin):
    """Linear retarder material (retarder)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#retarder
    Params:
        - theta (spectrum or texture): [P | ∂] Specifies the rotation angle (in degrees) of the retarder around the optical axis (Default: 0.0)
        - delta (spectrum or texture): [P | ∂] Specifies the retardance (in degrees) where 360 degrees is equivalent to a full wavelength. (Default: 90.0)
        - transmittance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular transmission. (Default: 1.0)
    """

    theta: Optional[Union[List[float], Plugin]] = None
    delta: Optional[Union[List[float], Plugin]] = None
    transmittance: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self,
        id: Optional[str] = None,
        theta: Optional[Union[List[float], Plugin]] = None,
        delta: Optional[Union[List[float], Plugin]] = None,
        transmittance: Optional[Union[List[float], Plugin]] = None,
    ):
        super().__init__(type="retarder", id=id)
        self.id = id
        self.theta = theta
        self.delta = delta
        self.transmittance = transmittance


@dataclass
class CircularPolarizerMaterial(Plugin):
    """Circular polarizer material (circular)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#circular
    Params:
        - transmittance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular transmission. (Default: 1.0)
        - left_handed (boolean):  Flag to switch between left and right circular polarization. (Default: false , i.e. right circular polarizer)
    """

    transmittance: Optional[Union[List[float], Plugin]] = None
    left_handed: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        transmittance: Optional[Union[List[float], Plugin]] = None,
        left_handed: Optional[bool] = None,
    ):
        super().__init__(type="circular", id=id)
        self.id = id
        self.transmittance = transmittance
        self.left_handed = left_handed


@dataclass
class PolarizedPlasticMaterial(Plugin):
    """Polarized plastic material (pplastic)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#pplastic
        Params:
            - diffuse_reflectance (spectrum or texture): [P | ∂] Optional factor used to modulate the diffuse reflection component. (Default: 0.5)
            - specular_reflectance (spectrum or texture): [P | ∂] Optional factor that can be used to modulate the specular reflection component.
    Note that for physical realism, this parameter should never be touched. (Default: 1.0)
            - int_ior (float or string):  Interior index of refraction specified numerically or using a known material name. (Default: polypropylene / 1.49)
            - ext_ior (float or string):  Exterior index of refraction specified numerically or using a known material name.  (Default: air / 1.000277)
            - distribution (string):  Specifies the type of microfacet normal distribution used to model the surface roughness. beckmann : Physically-based distribution derived from Gaussian random surfaces.
    This is the default. ggx : The GGX [ WMLT07 ] distribution (also known as Trowbridge-Reitz [ TR75 ] distribution) was designed to better approximate the long
    tails observed in measurements of ground surfaces, which are not modeled by the Beckmann
    distribution.
            - alpha (float): [P | ∂ | D] Specifies the roughness of the unresolved surface micro-geometry along the tangent and
    bitangent directions. When the Beckmann distribution is used, this parameter is equal to the root mean square (RMS) slope of the microfacets. (Default: 0.1)
            - sample_visible (boolean):  Enables a sampling technique proposed by Heitz and D’Eon [ HDEon14 ] , which
    focuses computation on the visible parts of the microfacet normal distribution, considerably
    reducing variance in some cases. (Default: true , i.e. use visible normal sampling)
            - eta (float): [P | ∂ | D] Relative index of refraction from the exterior to the interior
    """

    diffuse_reflectance: Optional[Union[List[float], Plugin]] = None
    specular_reflectance: Optional[Union[List[float], Plugin]] = None
    int_ior: Optional[float] = None
    ext_ior: Optional[float] = None
    distribution: Optional[str] = None
    alpha: Optional[float] = None
    sample_visible: Optional[bool] = None
    eta: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        diffuse_reflectance: Optional[Union[List[float], Plugin]] = None,
        specular_reflectance: Optional[Union[List[float], Plugin]] = None,
        int_ior: Optional[float] = None,
        ext_ior: Optional[float] = None,
        distribution: Optional[str] = None,
        alpha: Optional[float] = None,
        sample_visible: Optional[bool] = None,
        eta: Optional[float] = None,
    ):
        super().__init__(type="pplastic", id=id)
        self.id = id
        self.diffuse_reflectance = diffuse_reflectance
        self.specular_reflectance = specular_reflectance
        self.int_ior = int_ior
        self.ext_ior = ext_ior
        self.distribution = distribution
        self.alpha = alpha
        self.sample_visible = sample_visible
        self.eta = eta


@dataclass
class TheThinPrincipledBsdf(Plugin):
    """The Thin Principled BSDF (principledthin)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#principledthin
        Params:
            - base_color (spectrum or texture): [P | ∂] The color of the material. (Default: 0.5)
            - roughness (float or texture): [P | ∂ | D] Controls the roughness parameter of the main specular lobes. (Default: 0.5)
            - anisotropic (float or texture): [P | ∂ | D] Controls the degree of anisotropy. (0.0: isotropic material) (Default: 0.0)
            - spec_trans (texture or float): [P | ∂] Blends diffuse and specular responses. (1.0: only
    specular response, 0.0 : only diffuse response.)(Default: 0.0)
            - eta (float or texture): [P | ∂ | D] Interior IOR/Exterior IOR (Default: 1.5)
            - spec_tint (texture or float): [P | ∂] The fraction of base_color tint applied onto the dielectric reflection
    lobe. (Default: 0.0)
            - sheen (float or texture): [P | ∂] The rate of the sheen lobe. (Default: 0.0)
            - sheen_tint (float or texture): [P | ∂] The fraction of base_color tint applied onto the sheen lobe. (Default: 0.0)
            - flatness (float or texture): [P | ∂] Blends between the diffuse response and fake subsurface approximation based
    on Hanrahan-Krueger approximation. (0.0:only diffuse response, 1.0:only
    fake subsurface scattering.) (Default: 0.0)
            - diff_trans (texture or float): [P | ∂] The fraction that the energy of diffuse reflection is given to the
    transmission. (0.0: only diffuse reflection, 2.0: only diffuse
    transmission) (Default:0.0)
            - diffuse_reflectance_sampling_rate (float): [P] The rate of the cosine hemisphere reflection in sampling. (Default: 1.0)
            - specular_reflectance_sampling_rate (float): [P] The rate of the main specular reflection in sampling. (Default: 1.0)
            - specular_transmittance_sampling_rate (float): [P] The rate of the main specular transmission in sampling. (Default: 1.0)
            - diffuse_transmittance_sampling_rate (float): [P] The rate of the cosine hemisphere transmission in sampling. (Default: 1.0)
    """

    base_color: Optional[Union[List[float], Plugin]] = None
    roughness: Optional[float] = None
    anisotropic: Optional[float] = None
    spec_trans: Optional[float] = None
    eta: Optional[float] = None
    spec_tint: Optional[float] = None
    sheen: Optional[float] = None
    sheen_tint: Optional[float] = None
    flatness: Optional[float] = None
    diff_trans: Optional[float] = None
    diffuse_reflectance_sampling_rate: Optional[float] = None
    specular_reflectance_sampling_rate: Optional[float] = None
    specular_transmittance_sampling_rate: Optional[float] = None
    diffuse_transmittance_sampling_rate: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        base_color: Optional[Union[List[float], Plugin]] = None,
        roughness: Optional[float] = None,
        anisotropic: Optional[float] = None,
        spec_trans: Optional[float] = None,
        eta: Optional[float] = None,
        spec_tint: Optional[float] = None,
        sheen: Optional[float] = None,
        sheen_tint: Optional[float] = None,
        flatness: Optional[float] = None,
        diff_trans: Optional[float] = None,
        diffuse_reflectance_sampling_rate: Optional[float] = None,
        specular_reflectance_sampling_rate: Optional[float] = None,
        specular_transmittance_sampling_rate: Optional[float] = None,
        diffuse_transmittance_sampling_rate: Optional[float] = None,
    ):
        super().__init__(type="principledthin", id=id)
        self.id = id
        self.base_color = base_color
        self.roughness = roughness
        self.anisotropic = anisotropic
        self.spec_trans = spec_trans
        self.eta = eta
        self.spec_tint = spec_tint
        self.sheen = sheen
        self.sheen_tint = sheen_tint
        self.flatness = flatness
        self.diff_trans = diff_trans
        self.diffuse_reflectance_sampling_rate = diffuse_reflectance_sampling_rate
        self.specular_reflectance_sampling_rate = specular_reflectance_sampling_rate
        self.specular_transmittance_sampling_rate = specular_transmittance_sampling_rate
        self.diffuse_transmittance_sampling_rate = diffuse_transmittance_sampling_rate


@dataclass
class ThePrincipledBsdf(Plugin):
    """The Principled BSDF (principled)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_bsdfs.html#principled
        Params:
            - base_color (spectrum or texture): [P | ∂] The color of the material. (Default:0.5)
            - roughness (float or texture): [P | ∂ | D] Controls the roughness parameter of the main specular lobes. (Default:0.5)
            - anisotropic (float or texture): [P | ∂ | D] Controls the degree of anisotropy. (0.0 : isotropic material) (Default:0.0)
            - metallic (texture or float): [P | ∂ | D] The “metallicness” of the model. (Default:0.0)
            - spec_trans (texture or float): [P | ∂ | D] Blends BRDF and BSDF major lobe. (1.0: only BSDF
    response, 0.0 : only BRDF response.) (Default: 0.0)
            - eta (float): [P | ∂ | D] Interior IOR/Exterior IOR
            - specular (float): [P | ∂ | D] Controls the Fresnel reflection coefficient. This parameter has one to one
    correspondence with eta , so both of them can not be specified in xml.
    (Default:0.5)
            - spec_tint (texture or float): [P | ∂] The fraction of base_color tint applied onto the dielectric reflection
    lobe. (Default:0.0)
            - sheen (float or texture): [P | ∂] The rate of the sheen lobe. (Default:0.0)
            - sheen_tint (float or texture): [P | ∂] The fraction of base_color tint applied onto the sheen lobe. (Default:0.0)
            - flatness (float or texture): [P | ∂] Blends between the diffuse response and fake subsurface approximation based
    on Hanrahan-Krueger approximation. (0.0:only diffuse response, 1.0:only
    fake subsurface scattering.) (Default:0.0)
            - clearcoat (texture or float): [P | ∂ | D] The rate of the secondary isotropic specular lobe. (Default:0.0)
            - clearcoat_gloss (texture or float): [P | ∂ | D] Controls the roughness of the secondary specular lobe. Clearcoat response
    gets glossier as the parameter increases. (Default:0.0)
            - diffuse_reflectance_sampling_rate (float): [P] The rate of the cosine hemisphere reflection in sampling. (Default:1.0)
            - main_specular_sampling_rate (float): [P] The rate of the main specular lobe in sampling. (Default:1.0)
            - clearcoat_sampling_rate (float): [P] The rate of the secondary specular reflection in sampling. (Default:0.0)
    """

    base_color: Optional[Union[List[float], Plugin]] = None
    roughness: Optional[float] = None
    anisotropic: Optional[float] = None
    metallic: Optional[float] = None
    spec_trans: Optional[float] = None
    eta: Optional[float] = None
    specular: Optional[float] = None
    spec_tint: Optional[float] = None
    sheen: Optional[float] = None
    sheen_tint: Optional[float] = None
    flatness: Optional[float] = None
    clearcoat: Optional[float] = None
    clearcoat_gloss: Optional[float] = None
    diffuse_reflectance_sampling_rate: Optional[float] = None
    main_specular_sampling_rate: Optional[float] = None
    clearcoat_sampling_rate: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        base_color: Optional[Union[List[float], Plugin]] = None,
        roughness: Optional[float] = None,
        anisotropic: Optional[float] = None,
        metallic: Optional[float] = None,
        spec_trans: Optional[float] = None,
        eta: Optional[float] = None,
        specular: Optional[float] = None,
        spec_tint: Optional[float] = None,
        sheen: Optional[float] = None,
        sheen_tint: Optional[float] = None,
        flatness: Optional[float] = None,
        clearcoat: Optional[float] = None,
        clearcoat_gloss: Optional[float] = None,
        diffuse_reflectance_sampling_rate: Optional[float] = None,
        main_specular_sampling_rate: Optional[float] = None,
        clearcoat_sampling_rate: Optional[float] = None,
    ):
        super().__init__(type="principled", id=id)
        self.id = id
        self.base_color = base_color
        self.roughness = roughness
        self.anisotropic = anisotropic
        self.metallic = metallic
        self.spec_trans = spec_trans
        self.eta = eta
        self.specular = specular
        self.spec_tint = spec_tint
        self.sheen = sheen
        self.sheen_tint = sheen_tint
        self.flatness = flatness
        self.clearcoat = clearcoat
        self.clearcoat_gloss = clearcoat_gloss
        self.diffuse_reflectance_sampling_rate = diffuse_reflectance_sampling_rate
        self.main_specular_sampling_rate = main_specular_sampling_rate
        self.clearcoat_sampling_rate = clearcoat_sampling_rate
