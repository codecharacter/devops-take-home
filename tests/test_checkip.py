"""Unit Test: tests if IPv4 address is present in CIDR range"""

import pytest
import ipaddress
from ipcheck.checkip import check_ipv4_in_cidr_ranges


@pytest.mark.parametrize("test_ip, test_cidr, expected_result", [
    ("2.56.8.10", "2.56.8.0/24", True),
    ("172.31.1.100", "223.165.112.0/20", False),
])
def test_check_ipv4_in_cidr_ranges(test_ip, test_cidr, expected_result):
    """Test if IPv4 is present in CIDR range"""

    # ARRANGE -> with parametrize
    # ACT
    ip_addr = ipaddress.ip_address(test_ip)
    cidr_range = ipaddress.ip_network(test_cidr)

    # ASSERT
    assert check_ipv4_in_cidr_ranges(ip_addr, cidr_range) is expected_result
