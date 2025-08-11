from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Integrators


@dataclass
class DirectIlluminationIntegrator(Plugin):
    """Direct illumination integrator (direct)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#direct
        Params:
            - shading_samples (integer):  This convenience parameter can be used to set both emitter_samples and bsdf_samples at the same time.
            - emitter_samples (integer):  Optional more fine-grained parameter: specifies the number of samples that should be generated
    using the direct illumination strategies implemented by the scene’s emitters.
    (Default: set to the value of shading_samples )
            - bsdf_samples (integer):  Optional more fine-grained parameter: specifies the number of samples that should be generated
    using the BSDF sampling strategies implemented by the scene’s surfaces.
    (Default: set to the value of shading_samples )
            - hide_emitters (boolean):  Hide directly visible emitters.
    (Default: no, i.e. false )
    """

    shading_samples: Optional[int] = None
    emitter_samples: Optional[int] = None
    bsdf_samples: Optional[int] = None
    hide_emitters: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        shading_samples: Optional[int] = None,
        emitter_samples: Optional[int] = None,
        bsdf_samples: Optional[int] = None,
        hide_emitters: Optional[bool] = None,
    ):
        super().__init__(type="direct", id=id)
        self.id = id
        self.shading_samples = shading_samples
        self.emitter_samples = emitter_samples
        self.bsdf_samples = bsdf_samples
        self.hide_emitters = hide_emitters


@dataclass
class DirectIlluminationIntegrator(Plugin):
    """Direct illumination integrator (direct)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#direct
        Params:
            - shading_samples (integer):  This convenience parameter can be used to set both emitter_samples and bsdf_samples at the same time.
            - emitter_samples (integer):  Optional more fine-grained parameter: specifies the number of samples that should be generated
    using the direct illumination strategies implemented by the scene’s emitters.
    (Default: set to the value of shading_samples )
            - bsdf_samples (integer):  Optional more fine-grained parameter: specifies the number of samples that should be generated
    using the BSDF sampling strategies implemented by the scene’s surfaces.
    (Default: set to the value of shading_samples )
            - hide_emitters (boolean):  Hide directly visible emitters.
    (Default: no, i.e. false )
    """

    shading_samples: Optional[int] = None
    emitter_samples: Optional[int] = None
    bsdf_samples: Optional[int] = None
    hide_emitters: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        shading_samples: Optional[int] = None,
        emitter_samples: Optional[int] = None,
        bsdf_samples: Optional[int] = None,
        hide_emitters: Optional[bool] = None,
    ):
        super().__init__(type="direct", id=id)
        self.id = id
        self.shading_samples = shading_samples
        self.emitter_samples = emitter_samples
        self.bsdf_samples = bsdf_samples
        self.hide_emitters = hide_emitters


@dataclass
class PathTracer(Plugin):
    """Path tracer (path)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#path
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1
    corresponds to \\(\\infty\\) ). A value of 1 will only render directly
    visible light sources. 2 will lead to single-bounce (direct-only)
    illumination, and so on. (Default: -1)
            - rr_depth (integer):  Specifies the path depth, at which the implementation will begin to use
    the russian roulette path termination criterion. For example, if set to
    1, then path generation may randomly cease after encountering directly
    visible surfaces. (Default: 5)
            - hide_emitters (boolean):  Hide directly visible emitters. (Default: no, i.e. false )
    """

    max_depth: Optional[int] = None
    rr_depth: Optional[int] = None
    hide_emitters: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        max_depth: Optional[int] = None,
        rr_depth: Optional[int] = None,
        hide_emitters: Optional[bool] = None,
    ):
        super().__init__(type="path", id=id)
        self.id = id
        self.max_depth = max_depth
        self.rr_depth = rr_depth
        self.hide_emitters = hide_emitters


@dataclass
class ArbitraryOutputVariablesIntegrator(Plugin):
    """Arbitrary Output Variables integrator (aov)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#aov
        Params:
            - aovs (string):  List of <name>:<type> pairs denoting the enabled AOVs.
            - (Nested plugin) (integrator):  Sub-integrators (can have more than one) which will be sampled along the AOV integrator. Their
    respective output will be put into distinct images.
    """

    aovs: Optional[str] = None
    nested_plugin: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        aovs: Optional[str] = None,
        nested_plugin: Optional[Plugin] = None,
    ):
        super().__init__(type="aov", id=id)
        self.id = id
        self.aovs = aovs
        self.nested_plugin = nested_plugin


@dataclass
class VolumetricPathTracer(Plugin):
    """Volumetric path tracer (volpath)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#volpath
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1 corresponds to \\(\\infty\\) ). A value of 1 will only render directly visible light sources. 2 will lead
    to single-bounce (direct-only) illumination, and so on. (Default: -1)
            - rr_depth (integer):  Specifies the minimum path depth, after which the implementation will start to use the russian roulette path termination criterion. (Default: 5)
            - hide_emitters (boolean):  Hide directly visible emitters. (Default: no, i.e. false )
    """

    max_depth: Optional[int] = None
    rr_depth: Optional[int] = None
    hide_emitters: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        max_depth: Optional[int] = None,
        rr_depth: Optional[int] = None,
        hide_emitters: Optional[bool] = None,
    ):
        super().__init__(type="volpath", id=id)
        self.id = id
        self.max_depth = max_depth
        self.rr_depth = rr_depth
        self.hide_emitters = hide_emitters


@dataclass
class VolumetricPathTracerWithSpectralMis(Plugin):
    """Volumetric path tracer with spectral MIS (volpathmis)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#volpathmis
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1 corresponds to \\(\\infty\\) ). A value of 1 will only render directly visible light sources. 2 will lead
    to single-bounce (direct-only) illumination, and so on. (Default: -1)
            - rr_depth (integer):  Specifies the minimum path depth, after which the implementation will start to use the russian roulette path termination criterion. (Default: 5)
            - hide_emitters (boolean):  Hide directly visible emitters. (Default: no, i.e. false )
    """

    max_depth: Optional[int] = None
    rr_depth: Optional[int] = None
    hide_emitters: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        max_depth: Optional[int] = None,
        rr_depth: Optional[int] = None,
        hide_emitters: Optional[bool] = None,
    ):
        super().__init__(type="volpathmis", id=id)
        self.id = id
        self.max_depth = max_depth
        self.rr_depth = rr_depth
        self.hide_emitters = hide_emitters


@dataclass
class PathReplayBackpropagation(Plugin):
    """Path Replay Backpropagation (prb)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#prb
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1
    corresponds to \\(\\infty\\) ). A value of 1 will only render directly
    visible light sources. 2 will lead to single-bounce (direct-only)
    illumination, and so on. (Default: 6)
            - rr_depth (integer):  Specifies the path depth, at which the implementation will begin to use
    the russian roulette path termination criterion. For example, if set to
    1, then path generation many randomly cease after encountering directly
    visible surfaces. (Default: 5)
    """

    max_depth: Optional[int] = None
    rr_depth: Optional[int] = None

    def __init__(
        self,
        id: Optional[str] = None,
        max_depth: Optional[int] = None,
        rr_depth: Optional[int] = None,
    ):
        super().__init__(type="prb", id=id)
        self.id = id
        self.max_depth = max_depth
        self.rr_depth = rr_depth


@dataclass
class BasicPathReplayBackpropagation(Plugin):
    """Basic Path Replay Backpropagation (prb_basic)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#prb_basic
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1
    corresponds to \\(\\infty\\) ). A value of 1 will only render directly
    visible light sources. 2 will lead to single-bounce (direct-only)
    illumination, and so on. (Default: 6)
    """

    max_depth: Optional[int] = None

    def __init__(self, id: Optional[str] = None, max_depth: Optional[int] = None):
        super().__init__(type="prb_basic", id=id)
        self.id = id
        self.max_depth = max_depth


@dataclass
class DirectIlluminationProjectiveSampling(Plugin):
    """Direct illumination projective sampling (direct_projective)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#direct_projective
        Params:
            - sppc (integer):  Number of samples per pixel used to estimate the continuous
    derivatives. Unless it is zero, this parameter is overriden by the spp argument of the render method. If neither this parameter nor
    the spp argument are defined, the sample_count of the film’s
    sampler will be used.
            - sppp (integer):  Number of samples per pixel used to to estimate the gradients resulting
    from primary visibility changes (on the first segment of the light
    path: from the sensor to the first bounce) derivatives. Unless it is
    zero, this parameter is overriden by the spp argument of the render method. If neither this parameter nor the spp argument are
    defined, the sample_count of the film’s sampler will be used.
            - sppi (integer):  Number of samples per pixel used to to estimate the gradients resulting
    from indirect visibility changes  derivatives. Unless it is zero, this
    parameter is overriden by the spp argument of the render method.
    If neither this parameter nor the spp argument are defined, the sample_count of the film’s sampler will be used.
            - guiding (string):  Guiding type, must be one of: “none”, “grid”, or “octree”. This
    specifies the guiding method used for indirectly observed
    discontinuities. (Default: “octree”)
            - guiding_proj (boolean):  Whether or not to use projective sampling to generate the set of
    samples that are used to build the guiding structure. (Default: True)
            - guiding_rounds (integer):  Number of sampling iterations used to build the guiding data structure.
    A higher number of rounds will use more samples and hence should result
    in a more accurate guiding structure. (Default: 1)
    """

    sppc: Optional[int] = None
    sppp: Optional[int] = None
    sppi: Optional[int] = None
    guiding: Optional[str] = None
    guiding_proj: Optional[bool] = None
    guiding_rounds: Optional[int] = None

    def __init__(
        self,
        id: Optional[str] = None,
        sppc: Optional[int] = None,
        sppp: Optional[int] = None,
        sppi: Optional[int] = None,
        guiding: Optional[str] = None,
        guiding_proj: Optional[bool] = None,
        guiding_rounds: Optional[int] = None,
    ):
        super().__init__(type="direct_projective", id=id)
        self.id = id
        self.sppc = sppc
        self.sppp = sppp
        self.sppi = sppi
        self.guiding = guiding
        self.guiding_proj = guiding_proj
        self.guiding_rounds = guiding_rounds


@dataclass
class ProjectiveSamplingPathReplayBackpropagation(Plugin):
    """Projective sampling Path Replay Backpropagation (PRB)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#PRB
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1
    corresponds to \\(\\infty\\) ). A value of 1 will only render directly
    visible light sources. 2 will lead to single-bounce (direct-only)
    illumination, and so on. (Default: -1)
            - rr_depth (integer):  Specifies the path depth, at which the implementation will begin to use
    the russian roulette path termination criterion. For example, if set to
    1, then path generation many randomly cease after encountering directly
    visible surfaces. (Default: 5)
            - sppc (integer):  Number of samples per pixel used to estimate the continuous
    derivatives. Unless it is zero, this parameter is overriden by the spp argument of the render method. If neither this parameter nor
    the spp argument are defined, the sample_count of the film’s
    sampler will be used.
            - sppp (integer):  Number of samples per pixel used to to estimate the gradients resulting
    from primary visibility changes (on the first segment of the light
    path: from the sensor to the first bounce) derivatives. Unless it is
    zero, this parameter is overriden by the spp argument of the render method. If neither this parameter nor the spp argument are
    defined, the sample_count of the film’s sampler will be used.
            - sppi (integer):  Number of samples per pixel used to to estimate the gradients resulting
    from indirect visibility changes  derivatives. Unless it is zero, this
    parameter is overriden by the spp argument of the render method.
    If neither this parameter nor the spp argument are defined, the sample_count of the film’s sampler will be used.
            - guiding (string):  Guiding type, must be one of: “none”, “grid”, or “octree”. This
    specifies the guiding method used for indirectly observed
    discontinuities. (Default: “octree”)
            - guiding_proj (boolean):  Whether or not to use projective sampling to generate the set of
    samples that are used to build the guiding structure. (Default: True)
            - guiding_rounds (integer):  Number of sampling iterations used to build the guiding data structure.
    A higher number of rounds will use more samples and hence should result
    in a more accurate guiding structure. (Default: 1)
    """

    max_depth: Optional[int] = None
    rr_depth: Optional[int] = None
    sppc: Optional[int] = None
    sppp: Optional[int] = None
    sppi: Optional[int] = None
    guiding: Optional[str] = None
    guiding_proj: Optional[bool] = None
    guiding_rounds: Optional[int] = None

    def __init__(
        self,
        id: Optional[str] = None,
        max_depth: Optional[int] = None,
        rr_depth: Optional[int] = None,
        sppc: Optional[int] = None,
        sppp: Optional[int] = None,
        sppi: Optional[int] = None,
        guiding: Optional[str] = None,
        guiding_proj: Optional[bool] = None,
        guiding_rounds: Optional[int] = None,
    ):
        super().__init__(type="PRB", id=id)
        self.id = id
        self.max_depth = max_depth
        self.rr_depth = rr_depth
        self.sppc = sppc
        self.sppp = sppp
        self.sppi = sppi
        self.guiding = guiding
        self.guiding_proj = guiding_proj
        self.guiding_rounds = guiding_rounds


@dataclass
class PathReplayBackpropagationVolumetricIntegrator(Plugin):
    """Path Replay Backpropagation Volumetric Integrator (prbvolpath)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#prbvolpath
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1
    corresponds to \\(\\infty\\) ). A value of 1 will only render directly
    visible light sources. 2 will lead to single-bounce (direct-only)
    illumination, and so on. (Default: 6)
            - rr_depth (integer):  Specifies the path depth, at which the implementation will begin to use
    the russian roulette path termination criterion. For example, if set to
    1, then path generation many randomly cease after encountering directly
    visible surfaces. (Default: 5)
            - hide_emitters (boolean):  Hide directly visible emitters. (Default: no, i.e. false )
    """

    max_depth: Optional[int] = None
    rr_depth: Optional[int] = None
    hide_emitters: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        max_depth: Optional[int] = None,
        rr_depth: Optional[int] = None,
        hide_emitters: Optional[bool] = None,
    ):
        super().__init__(type="prbvolpath", id=id)
        self.id = id
        self.max_depth = max_depth
        self.rr_depth = rr_depth
        self.hide_emitters = hide_emitters


@dataclass
class MomentIntegrator(Plugin):
    """Moment integrator (moment)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#moment
        Params:
            - (Nested plugin) (integrator):  Sub-integrators (can have more than one) which will be sampled along the AOV integrator. Their
    respective XYZ output will be put into distinct images.
    """

    nested_plugin: Optional[Plugin] = None

    def __init__(
        self, id: Optional[str] = None, nested_plugin: Optional[Plugin] = None
    ):
        super().__init__(type="moment", id=id)
        self.id = id
        self.nested_plugin = nested_plugin


@dataclass
class StokesVectorIntegrator(Plugin):
    """Stokes vector integrator (stokes)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#stokes
        Params:
            - (Nested plugin) (integrator):  Sub-integrator (only one can be specified) which will be sampled along the Stokes
    integrator. In polarized rendering modes, its output Stokes vector is written
    into distinct images.
    """

    nested_plugin: Optional[Plugin] = None

    def __init__(
        self, id: Optional[str] = None, nested_plugin: Optional[Plugin] = None
    ):
        super().__init__(type="stokes", id=id)
        self.id = id
        self.nested_plugin = nested_plugin


@dataclass
class ParticleTracer(Plugin):
    """Particle tracer (ptracer)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_integrators.html#ptracer
        Params:
            - max_depth (integer):  Specifies the longest path depth in the generated output image (where -1 corresponds to \\(\\infty\\) ). A value of 1 will only render directly visible light sources. 2 will lead
    to single-bounce (direct-only) illumination, and so on. (Default: -1)
            - rr_depth (integer):  Specifies the minimum path depth, after which the implementation will start to use the russian roulette path termination criterion. (Default: 5)
            - hide_emitters (boolean):  Hide directly visible emitters. (Default: no, i.e. false )
            - samples_per_pass (boolean):  If specified, divides the workload in successive passes with samples_per_pass samples per pixel.
    """

    max_depth: Optional[int] = None
    rr_depth: Optional[int] = None
    hide_emitters: Optional[bool] = None
    samples_per_pass: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        max_depth: Optional[int] = None,
        rr_depth: Optional[int] = None,
        hide_emitters: Optional[bool] = None,
        samples_per_pass: Optional[bool] = None,
    ):
        super().__init__(type="ptracer", id=id)
        self.id = id
        self.max_depth = max_depth
        self.rr_depth = rr_depth
        self.hide_emitters = hide_emitters
        self.samples_per_pass = samples_per_pass
