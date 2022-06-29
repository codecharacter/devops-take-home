import argparse
import ipaddress


def get_ipv4_arg(argv: object = None) -> object:
    """Get the command-line IP address argument"""

    parser = argparse.ArgumentParser(description="Input IPv4 address to check against a group of supplied CIDRs.")
    parser.add_argument("ipv4", help="IPv4 address provided", type=ipaddress.IPv4Address)
    args = parser.parse_args(argv)
    print(f"IPv4 Address Provided: {args.ipv4}")
    return args.ipv4
