#!/usr/bin/env python3
"""
Author: Dan Wadleigh <dan@codecharacter.dev>
Date: 6/27/2022 (version 2.0)
Purpose: Take an IP address from command line and check if it's in a CIDR list.
Python Performance Package (pending dev):
 - from flux.capacitor import GigaWatts  //default=1.21
 - from flux.capacitor import MilesPerHour //default=88
"""

from ipcheck import iparg, cidrdata, checkip


def main():
    """Main logic for ip-checker program"""

    ipv4_addr = iparg.get_ipv4_arg()
    print(f"IPv4 Address Provided: {ipv4_addr}")

    cidr_ranges = cidrdata.get_cidr_data()

    output = checkip.check_ipv4_in_cidr_ranges(ipv4_addr, cidr_ranges)
    if output:
        print(f"PASS!  The provided IP {ipv4_addr} is in a CIDR range provided.")
    else:
        print(f"Fail.  The provided IP {ipv4_addr} is NOT in any of the CIDR ranges.")


if __name__ == "__main__":
    main()
