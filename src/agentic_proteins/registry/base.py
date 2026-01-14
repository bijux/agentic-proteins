# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

"""Shared registry behavior."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


class RegistryBase:
    """RegistryBase."""

    _registry: dict[Any, Any] = {}
    _locked: bool = False

    @classmethod
    def list(cls) -> Iterable[Any]:
        """list."""
        return tuple(cls._registry.values())

    @classmethod
    def lock(cls) -> None:
        """lock."""
        cls._locked = True

    @classmethod
    def clear(cls) -> None:
        """clear."""
        cls._registry.clear()
        cls._locked = False
