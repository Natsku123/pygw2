import pytest
import os
from pathlib import Path

from pygw2.api import Api

from .test_account import AccountTests
from .test_achievements import AchievementsTests
from .test_items import ItemTests

import unittest

if __name__ == "__main__":
    unittest.main()


def _load_local_env() -> None:
    """Load key=value pairs from a local .env file for test runs.

    Existing environment variables win over file values.
    """
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key and key not in os.environ:
            os.environ[key] = value


_load_local_env()


@pytest.fixture(scope="class")
def get_api(request):
    api_key = os.environ.get("API_KEY") or os.environ.get("api_key", "NO-KEY")
    request.cls.api = Api(api_key=api_key)
