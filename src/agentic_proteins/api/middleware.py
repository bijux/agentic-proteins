# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

"""API middleware."""

from __future__ import annotations

import uuid

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class RequestIdMiddleware(BaseHTTPMiddleware):
    """Attach a request id header for tracing."""

    async def dispatch(self, request: Request, call_next) -> Response:  # type: ignore[override]
        """Inject a request id for correlation across logs."""
        request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["x-request-id"] = request_id
        return response
