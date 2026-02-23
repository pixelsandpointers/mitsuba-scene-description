# Mitsuba Scene Description (MSD)

> **Disclaimer:** Expect rough edges and frequent changes to the API.

Typed, autocompletable Python dataclasses for composing [Mitsuba 3](https://github.com/mitsuba-renderer/mitsuba3) scenes programmatically.
Build a scene with normal Python objects and call `mi.load_dict(scene.to_dict())` to render.

The plugin classes are **generated at install time** by scraping the official Mitsuba plugin reference, so they always match your installed Mitsuba version.

## Installation

```bash
pip install mitsuba-scene-description
```

During installation the build hook detects your Mitsuba version and generates typed classes for every plugin in the docs.
The version is resolved in this order:

| Priority | Source | Example |
|----------|--------|---------|
| 1 | `MITSUBA_VERSION` env var | `MITSUBA_VERSION=3.7.1 pip install .` |
| 2 | Installed `mitsuba` package | automatic if mitsuba is already installed |
| 3 | Built-in fallback (`3.7.1`) | no extra setup needed |

### Development install

```bash
pip install -e .
```

## Usage

```python
import mitsuba_scene_description as msd
import mitsuba as mi

mi.set_variant("llvm_ad_rgb")

# Define components
diffuse = msd.SmoothDiffuseMaterial(reflectance=msd.RGB([0.8, 0.2, 0.2]))
ball = msd.Sphere(
    radius=1.0,
    bsdf=diffuse,
    to_world=msd.Transform().translate(0, 0, 3).scale(0.4),
)
cam = msd.PerspectivePinholeCamera(
    fov=45,
    to_world=msd.Transform().look_at(
        origin=[0, 1, -6], target=[0, 0, 0], up=[0, 1, 0]
    ),
)
integrator = msd.PathTracer()
emitter = msd.ConstantEnvironmentEmitter()
```

### Constructing scenes

Pass components directly to `Scene`:

```python
scene = msd.Scene(
    integrator=integrator,
    sensors=cam,  # also accepts a list for multi-sensor setups
    shapes={"ball": ball},
    emitters={"sun": emitter},
)
```

Or use the fluent `SceneBuilder`:

```python
scene = (
    msd.SceneBuilder()
    .integrator(integrator)
    .sensor(cam)
    .shape("ball", ball)
    .emitter("sun", emitter)
    .build()
)
```

### Rendering

```python
mi_scene = mi.load_dict(scene.to_dict())
rndr = mi.render(mi_scene)
mi.util.write_bitmap("test.png", rndr)
```

`scene.to_dict()` produces a plain dict ready for `mi.load_dict`:

```python
{'ball': {'bsdf': {'reflectance': {'type': 'rgb', 'value': [0.8, 0.2, 0.2]},
                   'type': 'diffuse'},
          'radius': 1.0,
          'to_world': Transform[
  matrix=[[0.4, 0, 0, 0],
          [0, 0.4, 0, 0],
          [0, 0, 0.4, 1.2],
          [0, 0, 0, 1]],
  ...
],
          'type': 'sphere'},
 'integrator': {'type': 'path'},
 'sensor': {'fov': 45,
            'to_world': Transform[...],
            'type': 'perspective'},
 'sun': {'type': 'constant'},
 'type': 'scene'}
```

### Core types

| Type | Description |
|------|-------------|
| `Plugin` | Base dataclass for all plugins |
| `Scene` | Top-level scene container |
| `SceneBuilder` | Fluent builder for `Scene` |
| `Transform` | Chainable affine transform builder (translate, scale, rotate, look_at, matrix) |
| `ProjectiveTransform` | Extends `Transform` with perspective/orthographic (Mitsuba >= 3.7) |
| `RGB` | RGB color value |
| `Ref` | Reference to a named asset |

### Generated plugin categories

Every Mitsuba plugin category gets its own module with a typed dataclass per plugin:

BSDFs, Emitters, Films, Integrators, Media, Phase functions, Reconstruction filters, Samplers, Sensors, Shapes, Spectra, Textures, Volumes.

All classes are re-exported from `mitsuba_scene_description`, so `msd.Sphere`, `msd.PathTracer`, etc. work directly.

## Running the generator manually

If you want to regenerate the API outside of the build process:

```bash
pip install requests beautifulsoup4
python generator/generate_mitsuba_api.py --out mitsuba_scene_description
```

Pass `--overview <url>` to target a specific docs version.

## License

MIT
