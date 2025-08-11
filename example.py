# minimal_scene.py
from pprint import pprint
import mitsuba as mi

mi.set_variant("llvm_ad_rgb")

import mitsuba_scene_description as msd

red = msd.SmoothDiffuseMaterial(reflectance=msd.RGB([0.8, 0.2, 0.2]))
ball = msd.Sphere(
    radius=1.0,
    bsdf=red,
    to_world=msd.Transform().translate(0, 0, 3).scale(1.0, 1.0, 1.0),
)

cam = msd.PerspectivePinholeCamera(
    fov=45,
    to_world=msd.Transform().look_at(origin=[0, 1, -6], target=[0, 0, 0], up=[0, 1, 0]),
)
integrator = msd.PathTracer()
sun = msd.PointLightSource(
    to_world=msd.Transform().translate(3, 4, 2), intensity=msd.RGB([3, 3, 3])
)

scene = msd.Scene(
    integrator=integrator,
    sensor=cam,
    shapes={"ball": ball},
    emitters={"sun": sun},
)


pprint(scene.to_dict())
mi_scene = mi.load_dict(scene.to_dict())
rndr = mi.render(mi_scene)
mi.util.write_bitmap("test.png", rndr)
