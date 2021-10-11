from typing import Type, Callable
from pydantic import BaseModel


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

    # Stop if nothing was found:
    if len(a) == 0:
        return

    # Select some IDs
    length = default_length if len(a) > default_length else len(a)
    a = a[:length]

    # Get stuff with IDs
    ans = await func(*a)

    # If more than 1 were requested, return a list, otherwise only the object
    if len(a) > 1:
        cls.assertIsInstance(a, list)
        cls.assertTrue(len(ans) == length)
        for answer in ans:
            cls.assertIsInstance(answer, t)
    else:
        cls.assertIsInstance(ans, t)
