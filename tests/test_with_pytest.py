"""Tests function of pytest"""

import pytest


def test_always_passes():
    """Always passes"""
    assert True


@pytest.mark.xfail
def test_always_fails():
    """Always fails"""
    assert False
