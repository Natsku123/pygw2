import pytest
from aiohttp import ContentTypeError

from pygw2.core.exceptions import ApiError
from pygw2.utils import endpoint
import pygw2.utils as utils


class _FakeResponse:
    def __init__(self, *, status, payload=None, json_error=None):
        self.status = status
        self._payload = payload
        self._json_error = json_error

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def json(self):
        if self._json_error is not None:
            raise self._json_error
        return self._payload


class _FakeSession:
    def __init__(self, response):
        self._response = response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    def get(self, *args, **kwargs):
        return self._response


class _DummyApi:
    @endpoint("/v2/test")
    async def get(self, *, data):
        return data


@pytest.mark.asyncio
async def test_endpoint_raises_api_error_for_server_errors(monkeypatch):
    monkeypatch.setattr(
        utils, "ClientSession", lambda: _FakeSession(_FakeResponse(status=503))
    )

    with pytest.raises(ApiError, match="API returned status 503"):
        await _DummyApi().get()


@pytest.mark.asyncio
async def test_endpoint_wraps_non_json_responses(monkeypatch):
    monkeypatch.setattr(
        utils,
        "ClientSession",
        lambda: _FakeSession(
            _FakeResponse(
                status=200,
                json_error=ContentTypeError(
                    None,
                    (),
                    status=200,
                    message="Attempt to decode JSON with unexpected mimetype",
                    headers={},
                ),
            )
        ),
    )

    with pytest.raises(ApiError, match="Unexpected non-JSON API response with status 200"):
        await _DummyApi().get()
