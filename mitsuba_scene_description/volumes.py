from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Volumes


@dataclass
class GridBasedVolumeDataSource(Plugin):
    """Grid-based volume data source (gridvolume)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_volumes.html#gridvolume
        Params:
            - filename (string):  Filename of the volume to be loaded
            - grid (VolumeGrid object):  When creating a grid volume at runtime, e.g. from Python or C++,
    an existing VolumeGrid instance can be passed directly rather than
    loading it from the filesystem with filename .
            - use_grid_bbox (boolean):  When set to true , the bounding box information contained in the VolumeGrid object (or the file it was loaded from) will be used. By
    default, it is assumed that the grid is defined in the unit cube spanning
    (0, 0, 0) x (1, 1, 1). Any evaluation of the volume outside of the bounding
    box is handled by the wrap_mode . (Default: false)
            - data (tensor): [P | ∂] Tensor array containing the grid data. This parameter can only be specified
    when building this plugin at runtime from Python or C++ and cannot be
    specified in the XML scene description. The raw parameter must
    also be set to true when using a tensor.
            - filter_type (string):  Specifies how voxel values are interpolated. The following options are
    currently available: trilinear (default): perform trilinear interpolation. nearest : disable interpolation. In this mode, the plugin
    performs nearest neighbor lookups of volume values.
            - wrap_mode (string):  Controls the behavior of volume evaluations that fall outside of the \\([0, 1]\\) range. The following options are currently available: clamp (default): clamp coordinates to the edge of the volume. repeat : tile the volume infinitely. mirror : mirror the volume along its boundaries.
            - raw (boolean):  Should the transformation to the stored color data (e.g. sRGB to linear,
    spectral upsampling) be disabled? You will want to enable this when working
    with non-color, 3-channel volume data. Currently, no plugin needs this option
    to be set to true (Default: false)
            - to_world (transform):  Specifies an optional 4x4 transformation matrix that will be applied to volume coordinates.
            - accel (boolean):  Hardware acceleration features can be used in CUDA mode. These features can
    cause small differences as hardware interpolation methods typically have a
    loss of precision (not exactly 32-bit arithmetic). (Default: true)
    """

    filename: Optional[str] = None
    grid: Optional[Plugin] = None
    use_grid_bbox: Optional[bool] = None
    data: Optional[Plugin] = None
    filter_type: Optional[str] = None
    wrap_mode: Optional[str] = None
    raw: Optional[bool] = None
    to_world: Optional[Transform] = None
    accel: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        grid: Optional[Plugin] = None,
        use_grid_bbox: Optional[bool] = None,
        data: Optional[Plugin] = None,
        filter_type: Optional[str] = None,
        wrap_mode: Optional[str] = None,
        raw: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        accel: Optional[bool] = None,
    ):
        super().__init__(type="gridvolume", id=id)
        self.id = id
        self.filename = filename
        self.grid = grid
        self.use_grid_bbox = use_grid_bbox
        self.data = data
        self.filter_type = filter_type
        self.wrap_mode = wrap_mode
        self.raw = raw
        self.to_world = to_world
        self.accel = accel


@dataclass
class GridBasedVolumeDataSource(Plugin):
    """Grid-based volume data source (gridvolume)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_volumes.html#gridvolume
        Params:
            - filename (string):  Filename of the volume to be loaded
            - grid (VolumeGrid object):  When creating a grid volume at runtime, e.g. from Python or C++,
    an existing VolumeGrid instance can be passed directly rather than
    loading it from the filesystem with filename .
            - use_grid_bbox (boolean):  When set to true , the bounding box information contained in the VolumeGrid object (or the file it was loaded from) will be used. By
    default, it is assumed that the grid is defined in the unit cube spanning
    (0, 0, 0) x (1, 1, 1). Any evaluation of the volume outside of the bounding
    box is handled by the wrap_mode . (Default: false)
            - data (tensor): [P | ∂] Tensor array containing the grid data. This parameter can only be specified
    when building this plugin at runtime from Python or C++ and cannot be
    specified in the XML scene description. The raw parameter must
    also be set to true when using a tensor.
            - filter_type (string):  Specifies how voxel values are interpolated. The following options are
    currently available: trilinear (default): perform trilinear interpolation. nearest : disable interpolation. In this mode, the plugin
    performs nearest neighbor lookups of volume values.
            - wrap_mode (string):  Controls the behavior of volume evaluations that fall outside of the \\([0, 1]\\) range. The following options are currently available: clamp (default): clamp coordinates to the edge of the volume. repeat : tile the volume infinitely. mirror : mirror the volume along its boundaries.
            - raw (boolean):  Should the transformation to the stored color data (e.g. sRGB to linear,
    spectral upsampling) be disabled? You will want to enable this when working
    with non-color, 3-channel volume data. Currently, no plugin needs this option
    to be set to true (Default: false)
            - to_world (transform):  Specifies an optional 4x4 transformation matrix that will be applied to volume coordinates.
            - accel (boolean):  Hardware acceleration features can be used in CUDA mode. These features can
    cause small differences as hardware interpolation methods typically have a
    loss of precision (not exactly 32-bit arithmetic). (Default: true)
    """

    filename: Optional[str] = None
    grid: Optional[Plugin] = None
    use_grid_bbox: Optional[bool] = None
    data: Optional[Plugin] = None
    filter_type: Optional[str] = None
    wrap_mode: Optional[str] = None
    raw: Optional[bool] = None
    to_world: Optional[Transform] = None
    accel: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        grid: Optional[Plugin] = None,
        use_grid_bbox: Optional[bool] = None,
        data: Optional[Plugin] = None,
        filter_type: Optional[str] = None,
        wrap_mode: Optional[str] = None,
        raw: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        accel: Optional[bool] = None,
    ):
        super().__init__(type="gridvolume", id=id)
        self.id = id
        self.filename = filename
        self.grid = grid
        self.use_grid_bbox = use_grid_bbox
        self.data = data
        self.filter_type = filter_type
        self.wrap_mode = wrap_mode
        self.raw = raw
        self.to_world = to_world
        self.accel = accel


@dataclass
class ConstantValuedVolumeDataSource(Plugin):
    """Constant-valued volume data source (constvolume)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_volumes.html#constvolume
    Params:
        - value (float or spectrum): [P | ∂] Specifies the value of the constant volume.
    """

    value: Optional[float] = None

    def __init__(self, id: Optional[str] = None, value: Optional[float] = None):
        super().__init__(type="constvolume", id=id)
        self.id = id
        self.value = value
