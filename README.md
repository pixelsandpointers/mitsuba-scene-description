# Mitsuba Scene Description (MSD)

_Disclaimer: Expect rough edges and frequent changes to the API._

This package contains:
1) A **core runtime API** (`mitsuba_scene_description`) with typed dataclasses, a recursive serializer,
   and a small sample of common plugins (BSDFs, shapes, sensors, emitters, integrators, textures).
   You can use this immediately to build scenes programmatically and call `mi.load_dict(scene.to_dict())`.

2) A **generator script** (`generator/generate_mitsuba_api.py`) that **scrapes the official Mitsuba
   plugin reference** and generates modules per category with conservative typing.
   Run it locally (with internet access) to create a *complete* API for all plugins.

## Quick start (core API sample)

### Installation
```bash
pip install mitsuba-scene-description
```

### Usage
```python
import mitsuba_scene_description as msd
import mitsuba as mi

mi.set_variant("llvm_ad_rgb")

diffuse = msd.SmoothDiffuseMaterial(reflectance=msd.RGB([0.8, 0.2, 0.2]))
sun = msd.Sphere(
    radius=1.0,
    bsdf=diffuse,
    to_world=msd.Transform().translate(0, 0, 3).scale(0.4),
)

cam = msd.OrthographicCamera(
    to_world=msd.Transform().look_at(origin=[0, 0, -6], target=[0, 0, 0], up=[0, 1, 0])
)

integrator = msd.PathTracer()
emitter = msd.ConstantEnvironmentEmitter()

scene = msd.Scene(
    integrator=integrator,
    sensor=cam,
    shapes={"sun": sun},
    emitters={"emitter": emitter},
)


mi_scene = mi.load_dict(scene.to_dict())
rndr = mi.render(mi_scene)
mi.util.write_bitmap("test.png", rndr)
```

```python
# `scene.to_dict()` results in the following:
{'emitter': {'type': 'constant'},
 'integrator': {'type': 'path'},
 'sensor': {'to_world': Transform[
  matrix=[[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, -6],
          [0, 0, 0, 1]],
  inverse_transpose=[[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 6, 1]]
],
            'type': 'orthographic'},
 'sun': {'bsdf': {'reflectance': {'type': 'rgb', 'value': [0.8, 0.2, 0.2]},
                  'type': 'diffuse'},
         'radius': 1.0,
         'to_world': Transform[
  matrix=[[0.4, 0, 0, 0],
          [0, 0.4, 0, 0],
          [0, 0, 0.4, 1.2],
          [0, 0, 0, 1]],
  inverse_transpose=[[2.5, 0, 0, 0],
                     [0, 2.5, 0, 0],
                     [0, 0, 2.5, 0],
                     [0, 0, -3, 1]]
],
         'type': 'sphere'},
 'type': 'scene'}
```

## Generate the full API from docs

1. Install requirements: `pip install -e ".[dev]"`
2. Run the generator:
   ```bash
   python generator/generate_mitsuba_api.py --out gen --overview https://mitsuba.readthedocs.io/en/latest/src/plugin_reference.html
   ```

### Notes
- The generator uses **conservative typing by default** (`Optional[Plugin]` for unknown or nested plugin params).
- You can tweak typing, categories, and output via CLI flags (`--aggressive`, `--single-file`, `--categories`).

### Roadmap
- [ ] Post-processing of generation using the tree-sitter API to remove artifacts
- [ ] Versioning
