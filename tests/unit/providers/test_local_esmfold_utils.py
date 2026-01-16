# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

from __future__ import annotations

import pytest

from agentic_proteins.providers.errors import PredictionError
from agentic_proteins.providers.local.esmfold import LocalESMFoldProvider


torch = pytest.importorskip("torch")


def test_format_atom_name_alignment() -> None:
    assert LocalESMFoldProvider._format_atom_name("CA", "C") == "  CA"
    assert LocalESMFoldProvider._format_atom_name("ATOM", "CA") == "ATOM"


def test_positions_to_backbone_pdb_smoke() -> None:
    provider = LocalESMFoldProvider.__new__(LocalESMFoldProvider)
    sequence = "AC"
    positions = torch.zeros((2, 4, 3))
    positions[0, 0] = torch.tensor([1.0, 2.0, 3.0])
    positions[1, 1] = torch.tensor([4.0, 5.0, 6.0])
    plddt = torch.tensor([0.5, 0.9])
    pdb = provider._positions_to_backbone_pdb(sequence, positions, plddt)
    assert "ATOM" in pdb
    assert "ENDMDL" in pdb


def test_positions_to_backbone_pdb_invalid_shape() -> None:
    provider = LocalESMFoldProvider.__new__(LocalESMFoldProvider)
    sequence = "AC"
    positions = torch.zeros((1, 4, 3))
    plddt = torch.tensor([0.5, 0.9])
    with pytest.raises(PredictionError, match="Expected positions"):
        provider._positions_to_backbone_pdb(sequence, positions, plddt)


def test_to_per_res_plddt_normalizes_values() -> None:
    provider = LocalESMFoldProvider.__new__(LocalESMFoldProvider)
    raw = torch.tensor([[50.0, 60.0], [70.0, 80.0]])
    per_res = provider._to_per_res_plddt(raw, n_res=2, n_atoms=2)
    assert per_res.shape[0] == 2
    assert float(per_res.max().item()) <= 1.0


def test_to_per_res_plddt_rejects_bad_shape() -> None:
    provider = LocalESMFoldProvider.__new__(LocalESMFoldProvider)
    raw = torch.zeros((3,))
    with pytest.raises(PredictionError, match="Unexpected 1D pLDDT"):
        provider._to_per_res_plddt(raw, n_res=2, n_atoms=2)
