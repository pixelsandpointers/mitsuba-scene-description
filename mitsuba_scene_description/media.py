from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Media


@dataclass
class HomogeneousMedium(Plugin):
    """Homogeneous medium (homogeneous)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_media.html#homogeneous
        Params:
            - albedo (float , spectrum or volume): [P | ∂] Single-scattering albedo of the medium (Default: 0.75).
            - sigma_t (float or spectrum): [P | ∂] Extinction coefficient in inverse scene units (Default: 1).
            - scale (float): [P] Optional scale factor that will be applied to the extinction parameter.
    It is provided for convenience when accommodating data based on different
    units, or to simply tweak the density of the medium. (Default: 1)
            - sample_emitters (boolean):  Flag to specify whether shadow rays should be cast from inside the volume (Default: true )
    If the medium is enclosed in a dielectric boundary,
    shadow rays are ineffective and turning them off will significantly reduce
    render time. This can reduce render time up to 50% when rendering objects
    with subsurface scattering.
            - (Nested plugin) (phase): [P | ∂] A nested phase function that describes the directional scattering properties of
    the medium. When none is specified, the renderer will automatically use an instance of
    isotropic.
    """

    albedo: Optional[float] = None
    sigma_t: Optional[float] = None
    scale: Optional[float] = None
    sample_emitters: Optional[bool] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        albedo: Optional[float] = None,
        sigma_t: Optional[float] = None,
        scale: Optional[float] = None,
        sample_emitters: Optional[bool] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="homogeneous", id=id)
        self.id = id
        self.albedo = albedo
        self.sigma_t = sigma_t
        self.scale = scale
        self.sample_emitters = sample_emitters
        self.nested_plugin = nested_plugin


@dataclass
class HomogeneousMedium(Plugin):
    """Homogeneous medium (homogeneous)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_media.html#homogeneous
        Params:
            - albedo (float , spectrum or volume): [P | ∂] Single-scattering albedo of the medium (Default: 0.75).
            - sigma_t (float or spectrum): [P | ∂] Extinction coefficient in inverse scene units (Default: 1).
            - scale (float): [P] Optional scale factor that will be applied to the extinction parameter.
    It is provided for convenience when accommodating data based on different
    units, or to simply tweak the density of the medium. (Default: 1)
            - sample_emitters (boolean):  Flag to specify whether shadow rays should be cast from inside the volume (Default: true )
    If the medium is enclosed in a dielectric boundary,
    shadow rays are ineffective and turning them off will significantly reduce
    render time. This can reduce render time up to 50% when rendering objects
    with subsurface scattering.
            - (Nested plugin) (phase): [P | ∂] A nested phase function that describes the directional scattering properties of
    the medium. When none is specified, the renderer will automatically use an instance of
    isotropic.
    """

    albedo: Optional[float] = None
    sigma_t: Optional[float] = None
    scale: Optional[float] = None
    sample_emitters: Optional[bool] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        albedo: Optional[float] = None,
        sigma_t: Optional[float] = None,
        scale: Optional[float] = None,
        sample_emitters: Optional[bool] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="homogeneous", id=id)
        self.id = id
        self.albedo = albedo
        self.sigma_t = sigma_t
        self.scale = scale
        self.sample_emitters = sample_emitters
        self.nested_plugin = nested_plugin


@dataclass
class HeterogeneousMedium(Plugin):
    """Heterogeneous medium (heterogeneous)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_media.html#heterogeneous
        Params:
            - albedo (float , spectrum or volume): [P | ∂] Single-scattering albedo of the medium (Default: 0.75).
            - sigma_t (float , spectrum or volume): [P | ∂] Extinction coefficient in inverse scene units (Default: 1).
            - scale (float): [P] Optional scale factor that will be applied to the extinction parameter.
    It is provided for convenience when accommodating data based on different
    units, or to simply tweak the density of the medium. (Default: 1)
            - sample_emitters (boolean):  Flag to specify whether shadow rays should be cast from inside the volume (Default: true )
    If the medium is enclosed in a dielectric boundary,
    shadow rays are ineffective and turning them off will significantly reduce
    render time. This can reduce render time up to 50% when rendering objects
    with subsurface scattering.
            - (Nested plugin) (phase): [P | ∂] A nested phase function that describes the directional scattering properties of
    the medium. When none is specified, the renderer will automatically use an instance of
    isotropic.
    """

    albedo: Optional[float] = None
    sigma_t: Optional[float] = None
    scale: Optional[float] = None
    sample_emitters: Optional[bool] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        albedo: Optional[float] = None,
        sigma_t: Optional[float] = None,
        scale: Optional[float] = None,
        sample_emitters: Optional[bool] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="heterogeneous", id=id)
        self.id = id
        self.albedo = albedo
        self.sigma_t = sigma_t
        self.scale = scale
        self.sample_emitters = sample_emitters
        self.nested_plugin = nested_plugin
