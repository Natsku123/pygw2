import pytest

from pygw2.core.exceptions import ApiError
from tests.helpers import ids_helper


class _DummyCase:
    def assertIsInstance(self, value, expected_type):
        assert isinstance(value, expected_type)

    def assertTrue(self, value):
        assert value


@pytest.mark.asyncio
async def test_ids_helper_falls_back_to_single_fetches():
    calls = []

    async def endpoint(*ids):
        calls.append(ids)
        if not ids:
            return [1, 2, 3]
        if len(ids) > 1:
            return None
        return ids[0]

    await ids_helper(_DummyCase(), endpoint, int)

    assert calls == [(), (1, 2, 3), (1,), (2,), (3,)]


@pytest.mark.asyncio
async def test_ids_helper_ignores_missing_single_fetches():
    calls = []

    async def endpoint(*ids):
        calls.append(ids)
        if not ids:
            return [1, 2, 3]
        if len(ids) > 1:
            return None
        if ids[0] == 2:
            raise ApiError("Not found")
        return ids[0]

    await ids_helper(_DummyCase(), endpoint, int)

    assert calls == [(), (1, 2, 3), (1,), (2,), (3,)]
