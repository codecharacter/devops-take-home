"""tests if argument input provided is valid IPv4"""

import pytest
import ipaddress


def is_valid_ipv4(test_ip):
    """Test if IP address is valid IPv4"""

    try:
        ip = ipaddress.ip_address(test_ip)

        if isinstance(ip, ipaddress.IPv4Address):
            return True
        elif isinstance(ip, ipaddress.IPv6Address):
            return False
    except ValueError:
        return False


@pytest.mark.parametrize("test_ip, expected_result", [
    ("2.56.8.1", True),
    ("28.63.132.186", True),
    ("3.0.0.300", False),
    ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", False)
])
def test_is_valid_ipv4(test_ip, expected_result):
    """test if valid IPv4 address"""

    assert is_valid_ipv4(test_ip) == expected_result
