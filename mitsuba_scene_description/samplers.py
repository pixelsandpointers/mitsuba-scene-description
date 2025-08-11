from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Samplers


@dataclass
class IndependentSampler(Plugin):
    """Independent sampler (independent)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_samplers.html#independent
    Params:
        - sample_count (integer):  Number of samples per pixel (Default: 4)
        - seed (integer):  Seed offset (Default: 0)
    """

    sample_count: Optional[int] = None
    seed: Optional[int] = None

    def __init__(
        self,
        id: Optional[str] = None,
        sample_count: Optional[int] = None,
        seed: Optional[int] = None,
    ):
        super().__init__(type="independent", id=id)
        self.id = id
        self.sample_count = sample_count
        self.seed = seed


@dataclass
class IndependentSampler(Plugin):
    """Independent sampler (independent)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_samplers.html#independent
    Params:
        - sample_count (integer):  Number of samples per pixel (Default: 4)
        - seed (integer):  Seed offset (Default: 0)
    """

    sample_count: Optional[int] = None
    seed: Optional[int] = None

    def __init__(
        self,
        id: Optional[str] = None,
        sample_count: Optional[int] = None,
        seed: Optional[int] = None,
    ):
        super().__init__(type="independent", id=id)
        self.id = id
        self.sample_count = sample_count
        self.seed = seed


@dataclass
class StratifiedSampler(Plugin):
    """Stratified sampler (stratified)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_samplers.html#stratified
    Params:
        - sample_count (integer):  Number of samples per pixel. This number should be a square number (Default: 4)
        - seed (integer):  Seed offset (Default: 0)
        - jitter (boolean):  Adds additional random jitter withing the stratum (Default: True)
    """

    sample_count: Optional[int] = None
    seed: Optional[int] = None
    jitter: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        sample_count: Optional[int] = None,
        seed: Optional[int] = None,
        jitter: Optional[bool] = None,
    ):
        super().__init__(type="stratified", id=id)
        self.id = id
        self.sample_count = sample_count
        self.seed = seed
        self.jitter = jitter


@dataclass
class CorrelatedMultiJitteredSampler(Plugin):
    """Correlated Multi-Jittered sampler (multijitter)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_samplers.html#multijitter
        Params:
            - sample_count (integer):  Number of samples per pixel. The sampler may internally choose to slightly increase this
    value to create a subdivision into strata that has an aspect ratio close to one. (Default: 4)
            - seed (integer):  Seed offset (Default: 0)
            - jitter (boolean):  Adds additional random jitter withing the substratum (Default: True)
    """

    sample_count: Optional[int] = None
    seed: Optional[int] = None
    jitter: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        sample_count: Optional[int] = None,
        seed: Optional[int] = None,
        jitter: Optional[bool] = None,
    ):
        super().__init__(type="multijitter", id=id)
        self.id = id
        self.sample_count = sample_count
        self.seed = seed
        self.jitter = jitter


@dataclass
class OrthogonalArraySampler(Plugin):
    """Orthogonal Array sampler (orthogonal)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_samplers.html#orthogonal
    Params:
        - sample_count (integer):  Number of samples per pixel. This value has to be the square of a prime number. (Default: 4)
        - strength (integer):  Orthogonal array’s strength (Default: 2)
        - seed (integer):  Seed offset (Default: 0)
        - jitter (boolean):  Adds additional random jitter withing the substratum (Default: True)
    """

    sample_count: Optional[int] = None
    strength: Optional[int] = None
    seed: Optional[int] = None
    jitter: Optional[bool] = None

    def __init__(
        self,
        id: Optional[str] = None,
        sample_count: Optional[int] = None,
        strength: Optional[int] = None,
        seed: Optional[int] = None,
        jitter: Optional[bool] = None,
    ):
        super().__init__(type="orthogonal", id=id)
        self.id = id
        self.sample_count = sample_count
        self.strength = strength
        self.seed = seed
        self.jitter = jitter
