from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform, ProjectiveTransform

# Category: Emitters

@dataclass
class AreaLight(Plugin):
    """Area light (area)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#area
    Params:
        - radiance (spectrum or texture): [P | ∂] Specifies the emitted radiance in units of power per unit area per unit steradian.
    """
    radiance: Optional[Union[List[float], Plugin]] = None

    def __init__(self, id: Optional[str] = None, radiance: Optional[Union[List[float], Plugin]] = None):
        super().__init__(type="area", id=id)
        self.id = id
        self.radiance = radiance

@dataclass
class PointLightSource(Plugin):
    """Point light source (point)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#point
    Params:
        - intensity (spectrum): [P | ∂] Specifies the radiant intensity in units of power per unit steradian.
        - position (point): [P] Alternative parameter for specifying the light source position.
Note that only one of the parameters to_world and position can be used at a time.
        - to_world (transform):  Specifies an optional emitter-to-world transformation.  (Default: none,
i.e. emitter space = world space)
    """
    intensity: Optional[Union[List[float], Plugin]] = None
    position: Optional[Plugin] = None
    to_world: Optional[Transform] = None

    def __init__(self, id: Optional[str] = None, intensity: Optional[Union[List[float], Plugin]] = None, position: Optional[Plugin] = None, to_world: Optional[Transform] = None):
        super().__init__(type="point", id=id)
        self.id = id
        self.intensity = intensity
        self.position = position
        self.to_world = to_world

@dataclass
class ConstantEnvironmentEmitter(Plugin):
    """Constant environment emitter (constant)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#constant
    Params:
        - radiance (spectrum): [P | ∂] Specifies the emitted radiance in units of power per unit area per unit steradian.
    """
    radiance: Optional[Union[List[float], Plugin]] = None

    def __init__(self, id: Optional[str] = None, radiance: Optional[Union[List[float], Plugin]] = None):
        super().__init__(type="constant", id=id)
        self.id = id
        self.radiance = radiance

@dataclass
class EnvironmentEmitter(Plugin):
    """Environment emitter (envmap)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#envmap
    Params:
        - filename (string):  Filename of the radiance-valued input image to be loaded; must be in latitude-longitude format.
        - bitmap (Bitmap object):  When creating a Environment emitter at runtime, e.g. from Python or C++,
an existing Bitmap image instance can be passed directly rather than
loading it from the filesystem with filename .
        - scale (float): [P | ∂] A scale factor that is applied to the radiance values stored in the input image. (Default: 1.0)
        - to_world (transform): [P] Specifies an optional emitter-to-world transformation.  (Default: none, i.e. emitter space = world space)
        - mis_compensation (boolean):  Compensate sampling for the presence of other Monte Carlo techniques that
will be combined using multiple importance sampling (MIS)? This is
extremely cheap to do and can slightly reduce variance. (Default: false)
        - data (tensor): [P | ∂ | D] Tensor array containing the radiance-valued data.
    """
    filename: Optional[str] = None
    bitmap: Optional[Plugin] = None
    scale: Optional[float] = None
    to_world: Optional[Transform] = None
    mis_compensation: Optional[bool] = None
    data: Optional[Plugin] = None

    def __init__(self, id: Optional[str] = None, filename: Optional[str] = None, bitmap: Optional[Plugin] = None, scale: Optional[float] = None, to_world: Optional[Transform] = None, mis_compensation: Optional[bool] = None, data: Optional[Plugin] = None):
        super().__init__(type="envmap", id=id)
        self.id = id
        self.filename = filename
        self.bitmap = bitmap
        self.scale = scale
        self.to_world = to_world
        self.mis_compensation = mis_compensation
        self.data = data

@dataclass
class SunAndSkyEmitter(Plugin):
    """Sun and sky emitter (sunsky)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#sunsky
    Params:
        - turbidity (float): [P] Atmosphere turbidity, must be within [1, 10] (Default: 3, clear sky in a temperate climate).
Smaller turbidity values (∼ 1 − 2) produce an arctic-like clear blue sky,
whereas larger values (∼ 8 − 10) create an atmosphere that is more typical
of a warm, humid day.
        - albedo (spectrum): [P] Ground albedo, must be within [0, 1] for each wavelength/channel, (Default: 0.3).
This cannot be spatially varying (e.g. have bitmap as type).
        - latitude (float): [P] Latitude of the location in degrees (Default: 35.689, Tokyo’s latitude).
        - longitude (float): [P] Longitude of the location in degrees (Default: 139.6917, Tokyo’s longitude).
        - timezone (float): [P] Timezone of the location in hours (Default: 9).
        - year (integer): [P] Year (Default: 2010).
        - month (integer): [P] Month (Default: 7).
        - day (integer): [P] Day (Default: 10).
        - hour (float): [P] Hour (Default: 15).
        - minute (float): [P] Minute (Default: 0).
        - second (float): [P] Second (Default: 0).
        - sun_direction (vector): [P | ∂] Direction of the sun in the sky (No defaults),
cannot be specified along with one of the location/time parameters.
        - sun_scale (float): [P] Scale factor for the sun radiance (Default: 1).
Can be used to turn the sun off (by setting it to 0).
        - sky_scale (float): [P] Scale factor for the sky radiance (Default: 1).
Can be used to turn the sky off (by setting it to 0).
        - sun_aperture (float):  Aperture angle of the sun in degrees (Default: 0.5338, normal sun aperture).
        - to_world (transform): [P] Specifies an optional emitter-to-world transformation.  (Default: none, i.e. emitter space = world space)
    """
    turbidity: Optional[float] = None
    albedo: Optional[Union[List[float], Plugin]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timezone: Optional[float] = None
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[float] = None
    minute: Optional[float] = None
    second: Optional[float] = None
    sun_direction: Optional[Plugin] = None
    sun_scale: Optional[float] = None
    sky_scale: Optional[float] = None
    sun_aperture: Optional[float] = None
    to_world: Optional[Transform] = None

    def __init__(self, id: Optional[str] = None, turbidity: Optional[float] = None, albedo: Optional[Union[List[float], Plugin]] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, timezone: Optional[float] = None, year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None, hour: Optional[float] = None, minute: Optional[float] = None, second: Optional[float] = None, sun_direction: Optional[Plugin] = None, sun_scale: Optional[float] = None, sky_scale: Optional[float] = None, sun_aperture: Optional[float] = None, to_world: Optional[Transform] = None):
        super().__init__(type="sunsky", id=id)
        self.id = id
        self.turbidity = turbidity
        self.albedo = albedo
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.sun_direction = sun_direction
        self.sun_scale = sun_scale
        self.sky_scale = sky_scale
        self.sun_aperture = sun_aperture
        self.to_world = to_world

@dataclass
class SpotLightSource(Plugin):
    """Spot light source (spot)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#spot
    Params:
        - intensity (spectrum): [P | ∂] Specifies the maximum radiant intensity at the center in units of power per unit steradian. (Default: 1).
This cannot be spatially varying (e.g. have bitmap as type).
        - cutoff_angle (float):  Cutoff angle, beyond which the spot light is completely black (Default: 20 degrees)
        - beam_width (float):  Subtended angle of the central beam portion (Default: \\(cutoff_angle \\times 3/4\\) )
        - texture (texture): [P | ∂] An optional texture to be projected along the spot light. This must be spatially varying (e.g. have bitmap as type).
        - to_world (transform): [P] Specifies an optional emitter-to-world transformation.  (Default: none, i.e. emitter space = world space)
    """
    intensity: Optional[Union[List[float], Plugin]] = None
    cutoff_angle: Optional[float] = None
    beam_width: Optional[float] = None
    texture: Optional[Plugin] = None
    to_world: Optional[Transform] = None

    def __init__(self, id: Optional[str] = None, intensity: Optional[Union[List[float], Plugin]] = None, cutoff_angle: Optional[float] = None, beam_width: Optional[float] = None, texture: Optional[Plugin] = None, to_world: Optional[Transform] = None):
        super().__init__(type="spot", id=id)
        self.id = id
        self.intensity = intensity
        self.cutoff_angle = cutoff_angle
        self.beam_width = beam_width
        self.texture = texture
        self.to_world = to_world

@dataclass
class DirectionalAreaLight(Plugin):
    """Directional area light (directionalarea)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#directionalarea
    Params:
        - radiance (spectrum): [P | ∂] Specifies the emitted radiance in units of power per unit area per unit steradian.
    """
    radiance: Optional[Union[List[float], Plugin]] = None

    def __init__(self, id: Optional[str] = None, radiance: Optional[Union[List[float], Plugin]] = None):
        super().__init__(type="directionalarea", id=id)
        self.id = id
        self.radiance = radiance

@dataclass
class DistantDirectionalEmitter(Plugin):
    """Distant directional emitter (directional)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#directional
    Params:
        - irradiance (spectrum): [P | ∂] Spectral irradiance, which corresponds to the amount of spectral power
per unit area received by a hypothetical surface normal to the specified
direction.
        - to_world (transform): [P] Emitter-to-world transformation matrix.
        - direction (vector):  Alternative (and exclusive) to to_world . Direction towards which the
emitter is radiating in world coordinates.
    """
    irradiance: Optional[Union[List[float], Plugin]] = None
    to_world: Optional[Transform] = None
    direction: Optional[Plugin] = None

    def __init__(self, id: Optional[str] = None, irradiance: Optional[Union[List[float], Plugin]] = None, to_world: Optional[Transform] = None, direction: Optional[Plugin] = None):
        super().__init__(type="directional", id=id)
        self.id = id
        self.irradiance = irradiance
        self.to_world = to_world
        self.direction = direction

@dataclass
class ProjectionLightSource(Plugin):
    """Projection light source (projector)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#projector
    Params:
        - irradiance (texture): [P | ∂] 2D texture specifying irradiance on the emitter’s virtual image plane,
which lies at a distance of \\(z=1\\) from the pinhole. Note that this
does not directly correspond to emitted radiance due to the presence of an
additional directionally varying scale factor equal to the inverse
sensitivity profile (a.k.a. importance) of a perspective camera. This
ensures that a projection of a constant texture onto a plane is truly
constant.
        - scale (float): [P | ∂] A scale factor that is applied to the radiance values stored in the above
parameter. (Default: 1.0)
        - to_world (transform): [P] Specifies an optional camera-to-world transformation.
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
    """
    irradiance: Optional[Plugin] = None
    scale: Optional[float] = None
    to_world: Optional[Transform] = None
    fov: Optional[float] = None
    focal_length: Optional[str] = None
    fov_axis: Optional[str] = None

    def __init__(self, id: Optional[str] = None, irradiance: Optional[Plugin] = None, scale: Optional[float] = None, to_world: Optional[Transform] = None, fov: Optional[float] = None, focal_length: Optional[str] = None, fov_axis: Optional[str] = None):
        super().__init__(type="projector", id=id)
        self.id = id
        self.irradiance = irradiance
        self.scale = scale
        self.to_world = to_world
        self.fov = fov
        self.focal_length = focal_length
        self.fov_axis = fov_axis

@dataclass
class TimedSunAndSkyEmitter(Plugin):
    """Timed sun and sky emitter (timed_sunsky)
    https://mitsuba.readthedocs.io/en/v3.7.1/src/generated/plugins_emitters.html#timed_sunsky
    Params:
        - turbidity (float): [P] Atmosphere turbidity, must be within [1, 10] (Default: 3, clear sky in a temperate climate).
Smaller turbidity values (∼ 1 − 2) produce an arctic-like clear blue sky,
whereas larger values (∼ 8 − 10) create an atmosphere that is more typical
of a warm, humid day.
        - albedo (spectrum): [P] Ground albedo, must be within [0, 1] for each wavelength/channel, (Default: 0.3).
This cannot be spatially varying (e.g. have bitmap as type).
        - latitude (float): [P] Latitude of the location in degrees (Default: 35.689, Tokyo’s latitude).
        - longitude (float): [P] Longitude of the location in degrees (Default: 139.6917, Tokyo’s longitude).
        - timezone (float): [P] Timezone of the location in hours (Default: 9).
        - window_start_time (float): [P] Start hour for the daily average (Default: 7).
        - window_end_time (float): [P] Final hour for the daily average (Default: 19).
        - start_year (integer): [P] Year of the start of the average (Default: 2025).
        - start_month (integer): [P] Month of the start of the average (Default: 01).
        - start_day (integer): [P] Day of the start of the average (Default: 01).
        - end_year (integer): [P] Year of the end of the average (Default: start_year + 1).
        - end_month (integer): [P] Month of the end of the average (Default: start_month).
        - end_day (integer): [P] Day of the end of the average (Default: start_day).
        - sun_scale (float): [P] Scale factor for the sun radiance (Default: 1).
Can be used to turn the sun off (by setting it to 0).
        - sky_scale (float): [P] Scale factor for the sky radiance (Default: 1).
Can be used to turn the sky off (by setting it to 0).
        - sun_aperture (float):  Aperture angle of the sun in degrees (Default: 0.5338, normal sun aperture).
        - shutter_open (float):  Shutter opening time (Default: 0).
Used to vary sunsky appearance
        - shutter_close (float):  Shutter closing time (Default: 1).
Used to vary sunsky appearance
        - to_world (transform): [P] Specifies an optional emitter-to-world transformation.  (Default: none, i.e. emitter space = world space)
    """
    turbidity: Optional[float] = None
    albedo: Optional[Union[List[float], Plugin]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timezone: Optional[float] = None
    window_start_time: Optional[float] = None
    window_end_time: Optional[float] = None
    start_year: Optional[int] = None
    start_month: Optional[int] = None
    start_day: Optional[int] = None
    end_year: Optional[int] = None
    end_month: Optional[int] = None
    end_day: Optional[int] = None
    sun_scale: Optional[float] = None
    sky_scale: Optional[float] = None
    sun_aperture: Optional[float] = None
    shutter_open: Optional[float] = None
    shutter_close: Optional[float] = None
    to_world: Optional[Transform] = None

    def __init__(self, id: Optional[str] = None, turbidity: Optional[float] = None, albedo: Optional[Union[List[float], Plugin]] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, timezone: Optional[float] = None, window_start_time: Optional[float] = None, window_end_time: Optional[float] = None, start_year: Optional[int] = None, start_month: Optional[int] = None, start_day: Optional[int] = None, end_year: Optional[int] = None, end_month: Optional[int] = None, end_day: Optional[int] = None, sun_scale: Optional[float] = None, sky_scale: Optional[float] = None, sun_aperture: Optional[float] = None, shutter_open: Optional[float] = None, shutter_close: Optional[float] = None, to_world: Optional[Transform] = None):
        super().__init__(type="timed_sunsky", id=id)
        self.id = id
        self.turbidity = turbidity
        self.albedo = albedo
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.window_start_time = window_start_time
        self.window_end_time = window_end_time
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.end_year = end_year
        self.end_month = end_month
        self.end_day = end_day
        self.sun_scale = sun_scale
        self.sky_scale = sky_scale
        self.sun_aperture = sun_aperture
        self.shutter_open = shutter_open
        self.shutter_close = shutter_close
        self.to_world = to_world
