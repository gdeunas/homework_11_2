import re

import pytest

from src.decorators import log, my_function


def test_log():
    result = my_function(1, 2)
    assert result == 3


def test_log_raises():
    @log(filename=None)
    def some_func(x, y):
        return x * y

    with pytest.raises(
        ValueError,
        match=re.escape("my_function error: <class 'ValueError'>: (1, 2), {}"),
    ):
        some_func(1, 2)
