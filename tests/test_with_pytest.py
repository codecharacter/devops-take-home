"""tests function of pytest"""

import pytest


def test_always_passes():
    assert True


@pytest.mark.xfail
def test_always_fails():
    assert False
