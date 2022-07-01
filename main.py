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
    """Main logic for ipcheck program"""

    ipv4_addr = iparg.get_ipv4_arg()

    json_url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
    cidr_ranges = cidrdata.get_cidr_data(json_url)

    checkip.check_ipv4_in_cidr_ranges(ipv4_addr, cidr_ranges["data"]["resources"]["ipv4"])


if __name__ == "__main__":
    main()
