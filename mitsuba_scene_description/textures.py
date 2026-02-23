from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform, ProjectiveTransform

# Category: Textures

@dataclass
class BitmapTexture(Plugin):
    """Bitmap texture (bitmap)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_textures.html#bitmap
    Params:
        - filename (string):  Filename of the bitmap to be loaded
        - bitmap (Bitmap object):  When creating a Bitmap texture at runtime, e.g. from Python or C++,
an existing Bitmap image instance can be passed directly rather than
loading it from the filesystem with filename .
        - data (tensor): [P | ∂] Tensor array containing the texture data. Similarly to the bitmap parameter, this field can only be used at runtime. The raw parameter must also be set to true .
        - filter_type (string):  Specifies how pixel values are interpolated and filtered when queried over larger
UV regions. The following options are currently available: bilinear (default): perform bilinear interpolation, but no filtering. nearest : disable filtering and interpolation. In this mode, the plugin
performs nearest neighbor lookups of texture values.
        - wrap_mode (string):  Controls the behavior of texture evaluations that fall outside of the \\([0, 1]\\) range. The following options are currently available: repeat (default): tile the texture infinitely. mirror : mirror the texture along its boundaries. clamp : clamp coordinates to the edge of the texture.
        - format (string):  Specifies the underlying texture storage format. The following options are
currently available: auto (default): If loading a texture from a bitmap, use half precision for bitmap data with 16 or lower bit depth, otherwise use
the native floating point representation of the Mitsuba variant. For
variants using a spectral color representation this option is the same
as variant . variant : Use the corresponding native floating point representation of the Mitsuba variant fp16 : Forcibly store the texture in half precision
        - raw (boolean):  Should the transformation to the stored color data (e.g. sRGB to linear,
spectral upsampling) be disabled? You will want to enable this when working
with bitmaps storing normal maps that use a linear encoding. (Default: false)
        - to_uv (transform): [P] Specifies an optional 3x3 transformation matrix that will be applied to UV
values. A 4x4 matrix can also be provided, in which case the extra row and
column are ignored.
        - accel (boolean):  Hardware acceleration features can be used in CUDA mode. These features can
cause small differences as hardware interpolation methods typically have a
loss of precision (not exactly 32-bit arithmetic). (Default: true)
    """
    filename: Optional[str] = None
    bitmap: Optional[Plugin] = None
    data: Optional[Plugin] = None
    filter_type: Optional[str] = None
    wrap_mode: Optional[str] = None
    format: Optional[str] = None
    raw: Optional[bool] = None
    to_uv: Optional[Transform] = None
    accel: Optional[bool] = None

    def __init__(self, id: Optional[str] = None, filename: Optional[str] = None, bitmap: Optional[Plugin] = None, data: Optional[Plugin] = None, filter_type: Optional[str] = None, wrap_mode: Optional[str] = None, format: Optional[str] = None, raw: Optional[bool] = None, to_uv: Optional[Transform] = None, accel: Optional[bool] = None):
        super().__init__(type="bitmap", id=id)
        self.id = id
        self.filename = filename
        self.bitmap = bitmap
        self.data = data
        self.filter_type = filter_type
        self.wrap_mode = wrap_mode
        self.format = format
        self.raw = raw
        self.to_uv = to_uv
        self.accel = accel

@dataclass
class CheckerboardTexture(Plugin):
    """Checkerboard texture (checkerboard)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_textures.html#checkerboard
    Params:
        - color0 (spectrum or texture): [P | ∂] Color values for the two differently-colored patches (Default: 0.4 and 0.2)
        - color1 (spectrum or texture): [P | ∂] Color values for the two differently-colored patches (Default: 0.4 and 0.2)
        - to_uv (transform): [P] Specifies an optional 3x3 UV transformation matrix. A 4x4 matrix can also be provided.
In that case, the last row and columns will be ignored.  (Default: none)
    """
    color0: Optional[Union[List[float], Plugin]] = None
    color1: Optional[Union[List[float], Plugin]] = None
    to_uv: Optional[Transform] = None

    def __init__(self, id: Optional[str] = None, color0: Optional[Union[List[float], Plugin]] = None, color1: Optional[Union[List[float], Plugin]] = None, to_uv: Optional[Transform] = None):
        super().__init__(type="checkerboard", id=id)
        self.id = id
        self.color0 = color0
        self.color1 = color1
        self.to_uv = to_uv

@dataclass
class MeshAttributeTexture(Plugin):
    """Mesh attribute texture (mesh_attribute)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_textures.html#mesh_attribute
    Params:
        - name (string):  Name of the attribute to evaluate. It should always start with "vertex_" or "face_" .
        - scale (float): [P] Scaling factor applied to the interpolated attribute value during evaluation.
(Default: 1.0)
    """
    name: Optional[str] = None
    scale: Optional[float] = None

    def __init__(self, id: Optional[str] = None, name: Optional[str] = None, scale: Optional[float] = None):
        super().__init__(type="mesh_attribute", id=id)
        self.id = id
        self.name = name
        self.scale = scale

@dataclass
class VolumetricTexture(Plugin):
    """Volumetric texture (volume)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_textures.html#volume
    Params:
        - volume (float , spectrum or volume): [P | ∂] Volumetric texture (Default: 0.75).
    """
    volume: Optional[float] = None

    def __init__(self, id: Optional[str] = None, volume: Optional[float] = None):
        super().__init__(type="volume", id=id)
        self.id = id
        self.volume = volume
