"""tests if CIDR data from webpage is valid IPv4 network address range"""

import pytest
import ipaddress


def is_valid_ipv4_cidr(test_cidr):
    """Return result of CIDR range check"""

    try:
        cidr = ipaddress.ip_network(test_cidr)

        if isinstance(cidr, ipaddress.IPv4Network):
            return True
        elif isinstance(cidr, ipaddress.IPv6Network):
            return False
    except ValueError:
        return False


@pytest.mark.parametrize("test_cidr, expected_result", [
    ("2.56.8.0/24", True),
    ("11.0.0.0/8", True),
    ("263.165.112.0/20", False),
    ("2001:400::/32", False)
])
def test_is_valid_ipv4_cidr(test_cidr, expected_result):
    """test if valid IPv4 CIDR range"""

    assert is_valid_ipv4_cidr(test_cidr) == expected_result
