from typing import Type, Callable
from pydantic import BaseModel


async def test_with_ids(
    cls, func: Callable, t: Type[BaseModel], default_length: int = 10
):
    """
    Helper to test with IDs
    :param cls: self of Testcase
    :param func: endpoint to be tested
    :param t: Return type
    :param default_length: default length of items to be tested
    :return: None
    """
    a = await func()
    cls.assertIsInstance(a, list)
    length = default_length if len(a) > default_length else len(a)
    a = a[:length]
    ans = await func(*a)
    cls.assertIsInstance(a, list)
    cls.assertTrue(len(ans) == length)
    for answer in ans:
        cls.assertIsInstance(answer, t)
