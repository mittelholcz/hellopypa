import pytest
from hellopypa.hellopypa import hello


def test_hello():
    assert hello() == 'Hello pypa!'
