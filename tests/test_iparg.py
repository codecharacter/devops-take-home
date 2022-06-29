"""Unit Test: get a valid IPv4 address from command line argument"""

from ipcheck.iparg import get_ipv4_arg
import pytest


def test_get_ipv4_arg_valid(capsys):
    """
    GIVEN a valid IPv4 argument
    WHEN supplied on the command line
    THEN a successful print statement output with IP
    """
    # ARRANGE
    get_ipv4_arg(["2.56.8.1"])

    # ACT
    out = capsys.readouterr().out

    # ASSERT
    assert "IPv4 Address Provided: 2.56.8.1\n" in out


def test_get_ipv4_arg_null(capsys):
    """
    GIVEN no argument supplied
    WHEN application run
    THEN an error message provided
    """
    # ARRANGE
    with pytest.raises(SystemExit) as err:
        get_ipv4_arg(argv=[""])

    # ACT
    stderr = capsys.readouterr().err

    # ASSERT
    assert err.value.code == 2
    assert "invalid IPv4Address value: ''" in stderr


def test_get_ipv4_arg_invalid(capsys):
    """
    GIVEN invalid IP address format input
    WHEN application run
    THEN an error message provided
    """
    # ARRANGE
    with pytest.raises(SystemExit) as err:
        get_ipv4_arg(argv=["172.31.1.275"])

    # ACT
    stderr = capsys.readouterr().err

    # ASSERT
    assert err.value.code == 2
    assert "invalid IPv4Address value: '172.31.1.275'" in stderr
