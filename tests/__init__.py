import pytest
import os

from pygw2.api import Api

from .test_account import AccountTests
from .test_achievements import AchievementsTests
from .test_items import ItemTests

import unittest

if __name__ == "__main__":
    unittest.main()


@pytest.fixture(scope="class")
def get_api(request):
    request.cls.api = Api(api_key=os.environ.get("api_key", "NO-KEY"))
