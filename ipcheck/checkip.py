import ipaddress


def check_ipv4_in_cidr_ranges(ipv4_addr, ipv4_cidrs):
    """Check if provided IPv4 address is present in CIDR ranges from data"""

    for cidr in ipv4_cidrs:
        if ipv4_addr in ipaddress.ip_network(cidr):
            return True
        break
    else:
        return False
