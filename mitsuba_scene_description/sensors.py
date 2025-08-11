from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Sensors


@dataclass
class OrthographicCamera(Plugin):
    """Orthographic camera (orthographic)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#orthographic
        Params:
            - to_world (transform): [P] Specifies an optional camera-to-world transformation.
    (Default: none (i.e. camera space = world space))
            - near_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - far_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
    """

    to_world: Optional[Transform] = None
    near_clip: Optional[float] = None
    far_clip: Optional[float] = None
    srf: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self,
        id: Optional[str] = None,
        to_world: Optional[Transform] = None,
        near_clip: Optional[float] = None,
        far_clip: Optional[float] = None,
        srf: Optional[Union[List[float], Plugin]] = None,
    ):
        super().__init__(type="orthographic", id=id)
        self.id = id
        self.to_world = to_world
        self.near_clip = near_clip
        self.far_clip = far_clip
        self.srf = srf


@dataclass
class OrthographicCamera(Plugin):
    """Orthographic camera (orthographic)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#orthographic
        Params:
            - to_world (transform): [P] Specifies an optional camera-to-world transformation.
    (Default: none (i.e. camera space = world space))
            - near_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - far_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
    """

    to_world: Optional[Transform] = None
    near_clip: Optional[float] = None
    far_clip: Optional[float] = None
    srf: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self,
        id: Optional[str] = None,
        to_world: Optional[Transform] = None,
        near_clip: Optional[float] = None,
        far_clip: Optional[float] = None,
        srf: Optional[Union[List[float], Plugin]] = None,
    ):
        super().__init__(type="orthographic", id=id)
        self.id = id
        self.to_world = to_world
        self.near_clip = near_clip
        self.far_clip = far_clip
        self.srf = srf


@dataclass
class PerspectivePinholeCamera(Plugin):
    """Perspective pinhole camera (perspective)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#perspective
        Params:
            - to_world (transform): [P | ∂ | D] Specifies an optional camera-to-world transformation.
    (Default: none (i.e. camera space = world space))
            - fov (float):  Denotes the camera’s field of view in degrees—must be between 0 and 180,
    excluding the extremes. Alternatively, it is also possible to specify a
    field of view using the focal_length parameter.
            - focal_length (string):  Denotes the camera’s focal length specified using 35mm film
    equivalent units. Alternatively, it is also possible to specify a field of
    view using the fov parameter. See the main description for further
    details. (Default: 50mm )
            - fov_axis (string):  When the parameter fov is given (and only then), this parameter further specifies
    the image axis, to which it applies. x : fov maps to the x -axis in screen space. y : fov maps to the y -axis in screen space. diagonal : fov maps to the screen diagonal. smaller : fov maps to the smaller dimension
    (e.g. x when width < height ) larger : fov maps to the larger dimension
    (e.g. y when width < height ) The default is x .
            - near_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - far_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - principal_point_offset_x (float): [P | ∂ | D] Specifies the position of the camera’s principal point relative to the center of the film.
            - principal_point_offset_y (float): [P | ∂ | D] Specifies the position of the camera’s principal point relative to the center of the film.
            - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
            - x_fov (float): [P | ∂ | D] Denotes the camera’s field of view in degrees along the horizontal axis.
    """

    to_world: Optional[Transform] = None
    fov: Optional[float] = None
    focal_length: Optional[str] = None
    fov_axis: Optional[str] = None
    near_clip: Optional[float] = None
    far_clip: Optional[float] = None
    principal_point_offset_x: Optional[float] = None
    principal_point_offset_y: Optional[float] = None
    srf: Optional[Union[List[float], Plugin]] = None
    x_fov: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        to_world: Optional[Transform] = None,
        fov: Optional[float] = None,
        focal_length: Optional[str] = None,
        fov_axis: Optional[str] = None,
        near_clip: Optional[float] = None,
        far_clip: Optional[float] = None,
        principal_point_offset_x: Optional[float] = None,
        principal_point_offset_y: Optional[float] = None,
        srf: Optional[Union[List[float], Plugin]] = None,
        x_fov: Optional[float] = None,
    ):
        super().__init__(type="perspective", id=id)
        self.id = id
        self.to_world = to_world
        self.fov = fov
        self.focal_length = focal_length
        self.fov_axis = fov_axis
        self.near_clip = near_clip
        self.far_clip = far_clip
        self.principal_point_offset_x = principal_point_offset_x
        self.principal_point_offset_y = principal_point_offset_y
        self.srf = srf
        self.x_fov = x_fov


@dataclass
class PerspectiveCameraWithAThinLens(Plugin):
    """Perspective camera with a thin lens (thinlens)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#thinlens
        Params:
            - to_world (transform): [P] Specifies an optional camera-to-world transformation.
    (Default: none (i.e. camera space = world space))
            - aperture_radius (float): [P] Denotes the radius of the camera’s aperture in scene units.
            - focus_distance (float): [P] Denotes the world-space distance from the camera’s aperture to the focal plane.
    (Default: 0 )
            - focal_length (string):  Denotes the camera’s focal length specified using 35mm film equivalent units.
    See the main description for further details. (Default: 50mm )
            - fov (float):  An alternative to focal_length : denotes the camera’s field of view in degrees—must be
    between 0 and 180, excluding the extremes.
            - fov_axis (string):  When the parameter fov is given (and only then), this parameter further specifies
    the image axis, to which it applies. x : fov maps to the x -axis in screen space. y : fov maps to the y -axis in screen space. diagonal : fov maps to the screen diagonal. smaller : fov maps to the smaller dimension
    (e.g. x when width < height ) larger : fov maps to the larger dimension
    (e.g. y when width < height ) The default is x .
            - near_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - far_clip (float): [P] Distance to the near/far clip planes. (Default: near_clip=1e-2 (i.e. 0.01 )
    and far_clip=1e4 (i.e. 10000 ))
            - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
            - x_fov (float): [P] Denotes the camera’s field of view in degrees along the horizontal axis.
    """

    to_world: Optional[Transform] = None
    aperture_radius: Optional[float] = None
    focus_distance: Optional[float] = None
    focal_length: Optional[str] = None
    fov: Optional[float] = None
    fov_axis: Optional[str] = None
    near_clip: Optional[float] = None
    far_clip: Optional[float] = None
    srf: Optional[Union[List[float], Plugin]] = None
    x_fov: Optional[float] = None

    def __init__(
        self,
        id: Optional[str] = None,
        to_world: Optional[Transform] = None,
        aperture_radius: Optional[float] = None,
        focus_distance: Optional[float] = None,
        focal_length: Optional[str] = None,
        fov: Optional[float] = None,
        fov_axis: Optional[str] = None,
        near_clip: Optional[float] = None,
        far_clip: Optional[float] = None,
        srf: Optional[Union[List[float], Plugin]] = None,
        x_fov: Optional[float] = None,
    ):
        super().__init__(type="thinlens", id=id)
        self.id = id
        self.to_world = to_world
        self.aperture_radius = aperture_radius
        self.focus_distance = focus_distance
        self.focal_length = focal_length
        self.fov = fov
        self.fov_axis = fov_axis
        self.near_clip = near_clip
        self.far_clip = far_clip
        self.srf = srf
        self.x_fov = x_fov


@dataclass
class DistantRadiancemeterSensor(Plugin):
    """Distant radiancemeter sensor (distant)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#distant
        Params:
            - to_world (transform):  Sensor-to-world transformation matrix.
            - direction (vector):  Alternative (and exclusive) to to_world . Direction orienting the
    sensor’s reference hemisphere.
            - target (point or nested shape plugin):  Optional. Define the ray target sampling strategy.
    If this parameter is unset, ray target points are sampled uniformly on
    the cross section of the scene’s bounding sphere.
    If a point is passed, rays will target it.
    If a shape plugin is passed, ray target points will be sampled from its
    surface.
            - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
    """

    to_world: Optional[Transform] = None
    direction: Optional[Plugin] = None
    target: Optional[Plugin] = None
    srf: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self,
        id: Optional[str] = None,
        to_world: Optional[Transform] = None,
        direction: Optional[Plugin] = None,
        target: Optional[Plugin] = None,
        srf: Optional[Union[List[float], Plugin]] = None,
    ):
        super().__init__(type="distant", id=id)
        self.id = id
        self.to_world = to_world
        self.direction = direction
        self.target = target
        self.srf = srf


@dataclass
class BatchSensor(Plugin):
    """Batch sensor (batch)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#batch
    Params:
        - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
    """

    srf: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self, id: Optional[str] = None, srf: Optional[Union[List[float], Plugin]] = None
    ):
        super().__init__(type="batch", id=id)
        self.id = id
        self.srf = srf


@dataclass
class RadianceMeter(Plugin):
    """Radiance meter (radiancemeter)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#radiancemeter
        Params:
            - to_world (transform):  Specifies an optional camera-to-world transformation.
    (Default: none (i.e. camera space = world space))
            - origin (point):  Location from which the sensor will be recording in world coordinates.
    Must be used with direction .
            - direction (vector):  Alternative (and exclusive) to to_world . Direction in which the
    sensor is pointing in world coordinates. Must be used with origin .
            - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
    """

    to_world: Optional[Transform] = None
    origin: Optional[Plugin] = None
    direction: Optional[Plugin] = None
    srf: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self,
        id: Optional[str] = None,
        to_world: Optional[Transform] = None,
        origin: Optional[Plugin] = None,
        direction: Optional[Plugin] = None,
        srf: Optional[Union[List[float], Plugin]] = None,
    ):
        super().__init__(type="radiancemeter", id=id)
        self.id = id
        self.to_world = to_world
        self.origin = origin
        self.direction = direction
        self.srf = srf


@dataclass
class IrradianceMeter(Plugin):
    """Irradiance meter (irradiancemeter)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_sensors.html#irradiancemeter
    Params:
        - srf (spectrum):  Sensor Response Function that defines the spectral sensitivity of the sensor (Default: none )
    """

    srf: Optional[Union[List[float], Plugin]] = None

    def __init__(
        self, id: Optional[str] = None, srf: Optional[Union[List[float], Plugin]] = None
    ):
        super().__init__(type="irradiancemeter", id=id)
        self.id = id
        self.srf = srf
