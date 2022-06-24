"""Tests if IPv4 address is present in CIDR range"""

import pytest
import ipaddress


def is_ipv4_in_cidr(test_ip, test_cidr):
    """Return result of IPV4 address in CIDR range check"""

    ip_addr = ipaddress.ip_address(test_ip)
    cidr_range = ipaddress.ip_network(test_cidr)

    if ip_addr in cidr_range:
        return True
    else:
        return False


@pytest.mark.parametrize("test_ip, test_cidr, expected_result", [
    ("2.56.8.10", "2.56.8.0/24", True),
    ("11.11.11.11", "11.0.0.0/8", True),
    ("168.68.255.255", "168.67.0.0/16", False),
    ("172.31.1.100", "223.165.112.0/20", False),
])
def test_is_ipv4_in_cidr(test_ip, test_cidr, expected_result):
    """Test if valid IPv4 in CIDR range"""

    assert is_ipv4_in_cidr(test_ip, test_cidr) == expected_result
