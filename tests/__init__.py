import pytest
import os

from pygw2.api import api

from .test_account import AccountTests
from .test_achievements import AchievementsTests
from .test_items import ItemTests

import unittest

if __name__ == "__main__":
    unittest.main()


@pytest.fixture(scope="class")
def get_api(request):
    api.setup(os.environ.get("api_key", "NO-KEY"))
    request.cls.api = api
