from typing import Type, Callable
from pydantic import BaseModel


def subset(data: list, default_length: int):
    """
    Get a subset of a list
    :param data: list
    :param default_length: default length of list
    :return: list
    """

    # Stop if nothing was found:
    if len(data) == 0:
        return

    # Select some IDs
    length = default_length if len(data) > default_length else len(data)
    return data[:length]


async def ids_helper(cls, func: Callable, t: Type[BaseModel], default_length: int = 10):
    """
    Helper to test with IDs
    :param cls: self of Testcase
    :param func: endpoint to be tested
    :param t: Return type
    :param default_length: default length of items to be tested
    :return: None
    """

    # Call and get IDs
    a = await func()

    # Check that it is a list of IDs
    cls.assertIsInstance(a, list)

    a = subset(a, default_length)

    # Get stuff with IDs
    ans = await func(*a)

    # If more than 1 were requested, return a list, otherwise only the object
    if len(a) > 1:
        cls.assertIsInstance(a, list)
        cls.assertTrue(len(ans) == len(a))
        for answer in ans:
            cls.assertIsInstance(answer, t)
    else:
        cls.assertIsInstance(ans, t)
