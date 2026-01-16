# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

from __future__ import annotations

from dataclasses import dataclass, field
import sys
from types import SimpleNamespace
from typing import Any

import pytest
from requests.exceptions import RequestException

from agentic_proteins.providers.errors import PredictionError
from agentic_proteins.providers.experimental import _async_utils
from agentic_proteins.providers.experimental import colabfold
from agentic_proteins.providers.experimental.openprotein import APIOpenProteinProvider


def test_sleep_with_backoff_deadline_passed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(_async_utils.time, "sleep", lambda _s: None)
    backoff, slept = _async_utils.sleep_with_backoff(deadline=0.0, backoff=1.0)
    assert backoff == 1.0
    assert slept == 0.0


def test_sleep_with_retry_after_uses_retry_after(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(_async_utils.time, "sleep", lambda _s: None)
    monkeypatch.setattr(
        _async_utils.secrets.SystemRandom, "random", lambda _self: 0.0
    )
    deadline = _async_utils.time.time() + 10.0
    backoff, slept = _async_utils.sleep_with_retry_after(
        deadline=deadline, backoff=1.0, retry_after=3.0
    )
    assert backoff > 1.0
    assert slept == 3.0


@dataclass
class _FakeResponse:
    status_code: int
    payload: dict[str, Any]
    headers: dict[str, str] = field(default_factory=dict)

    def json(self) -> dict[str, Any]:
        return self.payload

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RequestException(f"status={self.status_code}")


class _FakeSession:
    def __init__(self, post_response: _FakeResponse, get_response: _FakeResponse) -> None:
        self._post_response = post_response
        self._get_response = get_response
        self.headers: dict[str, str] = {}

    def mount(self, *_args, **_kwargs) -> None:
        return None

    def post(self, *_args, **_kwargs) -> _FakeResponse:
        return self._post_response

    def get(self, *_args, **_kwargs) -> _FakeResponse:
        return self._get_response

    def close(self) -> None:
        return None


def test_colabfold_predict_success(monkeypatch: pytest.MonkeyPatch) -> None:
    post = _FakeResponse(status_code=200, payload={"job_id": "job-1"})
    poll = _FakeResponse(
        status_code=200,
        payload={"status": "SUCCESS", "result": {"models": [{"pdb": "PDB"}]}},
    )
    monkeypatch.setattr(colabfold.requests, "Session", lambda: _FakeSession(post, poll))
    monkeypatch.setattr(colabfold, "sleep_with_backoff", lambda *args, **kwargs: (1.0, 0.0))
    monkeypatch.setattr(
        colabfold, "sleep_with_retry_after", lambda *args, **kwargs: (1.0, 0.0)
    )
    provider = colabfold.APIColabFoldProvider(api_url="http://example")
    result = provider.predict("ACD", timeout=5.0)
    assert result.provider == provider.name
    assert result.pdb_text == "PDB"


def test_colabfold_predict_auth_error(monkeypatch: pytest.MonkeyPatch) -> None:
    post = _FakeResponse(status_code=401, payload={})
    poll = _FakeResponse(status_code=500, payload={})
    monkeypatch.setattr(colabfold.requests, "Session", lambda: _FakeSession(post, poll))
    provider = colabfold.APIColabFoldProvider(api_url="http://example")
    with pytest.raises(PredictionError, match="Authentication failed"):
        provider.predict("ACD", timeout=5.0)


def test_openprotein_predict_success(monkeypatch: pytest.MonkeyPatch) -> None:
    class _Job:
        def wait_for_pdb(self, timeout: float = 0.0) -> str:
            return "PDB"

    class _FoldNamespace:
        def esmfold(self, sequence: str) -> _Job:
            return _Job()

    class _Session:
        fold = _FoldNamespace()

    fake_module = SimpleNamespace(connect=lambda username, password: _Session())
    monkeypatch.setitem(sys.modules, "openprotein", fake_module)

    provider = APIOpenProteinProvider(user="user", password="pw", model="esmfold")
    result = provider.predict("ACDE", timeout=1.0)
    assert result.provider == provider.name
    assert result.pdb_text == "PDB"


def test_openprotein_requires_credentials() -> None:
    with pytest.raises(ValueError, match="OPENPROTEIN_USER"):
        APIOpenProteinProvider(user=None, password=None)
