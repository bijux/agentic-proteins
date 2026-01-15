# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

"""HTTP API entry points."""

from __future__ import annotations

from agentic_proteins.api.app import AppConfig, create_app

__all__ = ["AppConfig", "create_app"]
