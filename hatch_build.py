"""Hatch custom build hook – runs the Mitsuba API generator at build time.

Version resolution order:
1. ``MITSUBA_VERSION`` env var  (e.g. ``MITSUBA_VERSION=3.7.1 pip install .``)
2. Installed ``mitsuba`` package (available with ``--no-build-isolation``)
3. Hardcoded fallback in the generator
"""

import sys
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    PLUGIN_NAME = "custom"

    def initialize(self, version: str, build_data: dict) -> None:  # noqa: ARG002
        # Make the generator package importable
        gen_dir = str(Path(__file__).resolve().parent / "generator")
        if gen_dir not in sys.path:
            sys.path.insert(0, gen_dir)

        from generate_mitsuba_api import generate

        out_dir = str(Path(__file__).resolve().parent / "mitsuba_scene_description")
        print(f"[hatch hook] Generating API into {out_dir}")
        generate(out_dir=out_dir)
