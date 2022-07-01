import ipaddress


def check_ipv4_in_cidr_ranges(ipv4_addr, ipv4_cidrs):
    """Check if provided IPv4 address is present in CIDR ranges from data"""

    for cidr in ipv4_cidrs:
        if ipv4_addr in ipaddress.ip_network(cidr):
            return print(f"PASS!  The IP {ipv4_addr} is in a CIDR range provided.")
    else:
        return print(f"Fail.  The IP {ipv4_addr} is NOT in any of the CIDR ranges.")
