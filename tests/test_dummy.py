import pytest
from ditkov_etal_2023_cmipio.dummy_module import dummy_foo


def test_dummy():
    assert dummy_foo(4) == (4 + 4)
