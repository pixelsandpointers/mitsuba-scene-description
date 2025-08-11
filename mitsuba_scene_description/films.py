from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Films


@dataclass
class HighDynamicRangeFilm(Plugin):
    """High dynamic range film (hdrfilm)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_films.html#hdrfilm
        Params:
            - width (integer):  Width and height of the camera sensor in pixels. (Default: 768, 576)
            - height (integer):  Width and height of the camera sensor in pixels. (Default: 768, 576)
            - file_format (string):  Denotes the desired output file format. The options are openexr (for ILM’s OpenEXR format), rgbe (for Greg Ward’s RGBE format), or pfm (for the Portable Float Map format). (Default: openexr )
            - pixel_format (string):  Specifies the desired pixel format of output images. The options are luminance , luminance_alpha , rgb , rgba , xyz and xyza .
    (Default: rgb )
            - component_format (string):  Specifies the desired floating point component format of output images (when saving to disk).
    The options are float16 , float32 , or uint32 .
    (Default: float16 )
            - crop_offset_x (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_offset_y (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_width (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_height (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - sample_border (boolean):  If set to true , regions slightly outside of the film plane will also be sampled. This may
    improve the image quality at the edges, especially when using very large reconstruction
    filters. In general, this is not needed though. (Default: false , i.e. disabled)
            - compensate (boolean):  If set to true , sample accumulation will be performed using Kahan-style
    error-compensated accumulation. This can be useful to avoid roundoff error
    when accumulating very many samples to compute reference solutions using
    single precision variants of Mitsuba. This feature is currently only supported
    in JIT variants and can make sample accumulation quite a bit more expensive.
    (Default: false , i.e. disabled)
            - (Nested plugin) (rfilter):  Reconstruction filter that should be used by the film. (Default: gaussian , a windowed
    Gaussian filter)
            - size (Vector2u): [P] Width and height of the camera sensor in pixels
            - crop_size (Vector2u): [P] Size of the sub-rectangle of the output in pixels
            - crop_offset (Point2u): [P] Offset of the sub-rectangle of the output in pixels
    """

    width: Optional[int] = None
    height: Optional[int] = None
    file_format: Optional[str] = None
    pixel_format: Optional[str] = None
    component_format: Optional[str] = None
    crop_offset_x: Optional[int] = None
    crop_offset_y: Optional[int] = None
    crop_width: Optional[int] = None
    crop_height: Optional[int] = None
    sample_border: Optional[bool] = None
    compensate: Optional[bool] = None
    nested_plugin: Optional[Plugin] = None
    size: Optional[Plugin] = None
    crop_size: Optional[Plugin] = None
    crop_offset: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        file_format: Optional[str] = None,
        pixel_format: Optional[str] = None,
        component_format: Optional[str] = None,
        crop_offset_x: Optional[int] = None,
        crop_offset_y: Optional[int] = None,
        crop_width: Optional[int] = None,
        crop_height: Optional[int] = None,
        sample_border: Optional[bool] = None,
        compensate: Optional[bool] = None,
        nested_plugin: Optional[Plugin] = None,
        size: Optional[Plugin] = None,
        crop_size: Optional[Plugin] = None,
        crop_offset: Optional[Plugin] = None,
    ):
        super().__init__(type="hdrfilm", id=id)
        self.id = id
        self.width = width
        self.height = height
        self.file_format = file_format
        self.pixel_format = pixel_format
        self.component_format = component_format
        self.crop_offset_x = crop_offset_x
        self.crop_offset_y = crop_offset_y
        self.crop_width = crop_width
        self.crop_height = crop_height
        self.sample_border = sample_border
        self.compensate = compensate
        self.nested_plugin = nested_plugin
        self.size = size
        self.crop_size = crop_size
        self.crop_offset = crop_offset


@dataclass
class HighDynamicRangeFilm(Plugin):
    """High dynamic range film (hdrfilm)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_films.html#hdrfilm
        Params:
            - width (integer):  Width and height of the camera sensor in pixels. (Default: 768, 576)
            - height (integer):  Width and height of the camera sensor in pixels. (Default: 768, 576)
            - file_format (string):  Denotes the desired output file format. The options are openexr (for ILM’s OpenEXR format), rgbe (for Greg Ward’s RGBE format), or pfm (for the Portable Float Map format). (Default: openexr )
            - pixel_format (string):  Specifies the desired pixel format of output images. The options are luminance , luminance_alpha , rgb , rgba , xyz and xyza .
    (Default: rgb )
            - component_format (string):  Specifies the desired floating point component format of output images (when saving to disk).
    The options are float16 , float32 , or uint32 .
    (Default: float16 )
            - crop_offset_x (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_offset_y (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_width (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_height (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - sample_border (boolean):  If set to true , regions slightly outside of the film plane will also be sampled. This may
    improve the image quality at the edges, especially when using very large reconstruction
    filters. In general, this is not needed though. (Default: false , i.e. disabled)
            - compensate (boolean):  If set to true , sample accumulation will be performed using Kahan-style
    error-compensated accumulation. This can be useful to avoid roundoff error
    when accumulating very many samples to compute reference solutions using
    single precision variants of Mitsuba. This feature is currently only supported
    in JIT variants and can make sample accumulation quite a bit more expensive.
    (Default: false , i.e. disabled)
            - (Nested plugin) (rfilter):  Reconstruction filter that should be used by the film. (Default: gaussian , a windowed
    Gaussian filter)
            - size (Vector2u): [P] Width and height of the camera sensor in pixels
            - crop_size (Vector2u): [P] Size of the sub-rectangle of the output in pixels
            - crop_offset (Point2u): [P] Offset of the sub-rectangle of the output in pixels
    """

    width: Optional[int] = None
    height: Optional[int] = None
    file_format: Optional[str] = None
    pixel_format: Optional[str] = None
    component_format: Optional[str] = None
    crop_offset_x: Optional[int] = None
    crop_offset_y: Optional[int] = None
    crop_width: Optional[int] = None
    crop_height: Optional[int] = None
    sample_border: Optional[bool] = None
    compensate: Optional[bool] = None
    nested_plugin: Optional[Plugin] = None
    size: Optional[Plugin] = None
    crop_size: Optional[Plugin] = None
    crop_offset: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        file_format: Optional[str] = None,
        pixel_format: Optional[str] = None,
        component_format: Optional[str] = None,
        crop_offset_x: Optional[int] = None,
        crop_offset_y: Optional[int] = None,
        crop_width: Optional[int] = None,
        crop_height: Optional[int] = None,
        sample_border: Optional[bool] = None,
        compensate: Optional[bool] = None,
        nested_plugin: Optional[Plugin] = None,
        size: Optional[Plugin] = None,
        crop_size: Optional[Plugin] = None,
        crop_offset: Optional[Plugin] = None,
    ):
        super().__init__(type="hdrfilm", id=id)
        self.id = id
        self.width = width
        self.height = height
        self.file_format = file_format
        self.pixel_format = pixel_format
        self.component_format = component_format
        self.crop_offset_x = crop_offset_x
        self.crop_offset_y = crop_offset_y
        self.crop_width = crop_width
        self.crop_height = crop_height
        self.sample_border = sample_border
        self.compensate = compensate
        self.nested_plugin = nested_plugin
        self.size = size
        self.crop_size = crop_size
        self.crop_offset = crop_offset


@dataclass
class SpectralFilm(Plugin):
    """Spectral film (specfilm)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_films.html#specfilm
        Params:
            - width (integer):  Width and height of the camera sensor in pixels. (Default: 768, 576)
            - height (integer):  Width and height of the camera sensor in pixels. (Default: 768, 576)
            - component_format (string):  Specifies the desired floating point component format of output images. The options are float16 , float32 , or uint32 . (Default: float16 )
            - crop_offset_x (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_offset_y (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_width (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - crop_height (integer):  These parameters can optionally be provided to select a sub-rectangle
    of the output. In this case, only the requested regions
    will be rendered. (Default: Unused)
            - sample_border (boolean):  If set to true , regions slightly outside of the film plane will also be sampled. This may
    improve the image quality at the edges, especially when using very large reconstruction
    filters. In general, this is not needed though. (Default: false , i.e. disabled)
            - compensate (boolean):  If set to true , sample accumulation will be performed using Kahan-style
    error-compensated accumulation. This can be useful to avoid roundoff error
    when accumulating very many samples to compute reference solutions using
    single precision variants of Mitsuba. This feature is currently only supported
    in JIT variants and can make sample accumulation quite a bit more expensive.
    (Default: false , i.e. disabled)
            - (Nested plugin) (rfilter):  Reconstruction filter that should be used by the film. (Default: gaussian , a windowed
    Gaussian filter)
            - (Nested plugins) (spectrum): [P] One or several Sensor Response Functions (SRF) used to compute different spectral bands
            - size (Vector2u): [P] Width and height of the camera sensor in pixels
            - crop_size (Vector2u): [P] Size of the sub-rectangle of the output in pixels
            - crop_offset (Point2u): [P] Offset of the sub-rectangle of the output in pixels
    """

    width: Optional[int] = None
    height: Optional[int] = None
    component_format: Optional[str] = None
    crop_offset_x: Optional[int] = None
    crop_offset_y: Optional[int] = None
    crop_width: Optional[int] = None
    crop_height: Optional[int] = None
    sample_border: Optional[bool] = None
    compensate: Optional[bool] = None
    nested_plugin: Optional[Plugin] = None
    nested_plugins: Optional[Union[List[float], Plugin]] = None
    size: Optional[Plugin] = None
    crop_size: Optional[Plugin] = None
    crop_offset: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        component_format: Optional[str] = None,
        crop_offset_x: Optional[int] = None,
        crop_offset_y: Optional[int] = None,
        crop_width: Optional[int] = None,
        crop_height: Optional[int] = None,
        sample_border: Optional[bool] = None,
        compensate: Optional[bool] = None,
        nested_plugin: Optional[Plugin] = None,
        nested_plugins: Optional[Union[List[float], Plugin]] = None,
        size: Optional[Plugin] = None,
        crop_size: Optional[Plugin] = None,
        crop_offset: Optional[Plugin] = None,
    ):
        super().__init__(type="specfilm", id=id)
        self.id = id
        self.width = width
        self.height = height
        self.component_format = component_format
        self.crop_offset_x = crop_offset_x
        self.crop_offset_y = crop_offset_y
        self.crop_width = crop_width
        self.crop_height = crop_height
        self.sample_border = sample_border
        self.compensate = compensate
        self.nested_plugin = nested_plugin
        self.nested_plugins = nested_plugins
        self.size = size
        self.crop_size = crop_size
        self.crop_offset = crop_offset
