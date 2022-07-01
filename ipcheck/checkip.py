"""Check if provided IPv4 address is present in CIDR ranges from JSON data."""

import ipaddress


def check_ipv4_in_cidr_ranges(ipv4_addr, ipv4_cidrs):
    """Check if IPv4 address is present in CIDR ranges."""

    for cidr in ipv4_cidrs:
        if ipv4_addr in ipaddress.ip_network(cidr):
            print(f"PASS!  The IP {ipv4_addr} is in a CIDR range provided.")
            return True
    else:
        print(f"Fail.  The IP {ipv4_addr} is NOT in any of the CIDR ranges.")
        return False
