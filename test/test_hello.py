import pytest
from hellopypa.hellopypa import hello


def test_hello():
    assert hello() == 'Hello pypa!'
    assert hello(upper=False) == 'Hello pypa!'
    assert hello(upper=True) == 'HELLO PYPA!'
