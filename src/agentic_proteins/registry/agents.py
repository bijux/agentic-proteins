# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

"""Agent registry."""

from __future__ import annotations

from typing import Any

from agentic_proteins.registry.base import RegistryBase


class AgentRegistry(RegistryBase):
    """AgentRegistry."""

    _registry: dict[str, type[Any]] = {}

    @classmethod
    def register(cls, agent_class: type[Any]) -> None:
        """register."""
        if cls._locked:
            raise ValueError("AgentRegistry is locked.")
        name = agent_class.name
        if name in cls._registry:
            raise ValueError(f"Agent already registered: {name}")
        cls._registry[name] = agent_class

    @classmethod
    def get(cls, name: str) -> type[Any]:
        """get."""
        return cls._registry[name]
