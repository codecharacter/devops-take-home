import argparse
import ipaddress


def get_ipv4_arg():
    """Get the command-line IP address argument"""

    parser = argparse.ArgumentParser(description="Input IPv4 address to check against a group of supplied CIDRs.")
    parser.add_argument("ipv4", help="IPv4 address provided", type=ipaddress.IPv4Address)
    return parser.parse_args().ipv4
