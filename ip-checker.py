#!/usr/bin/env python3
"""
Author: Dan Wadleigh <dan@codecharacter.dev>
Date: 6/23/2022
Purpose: Take an IP address from command line and check if it's in a CIDR list.
Python Performance Package (pending dev):
 - from flux.capacitor import GigaWatts  //default=1.21
 - from flux.capacitor import MilesPerHour //default=88
"""

import argparse
import ipaddress
import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError
from requests.adapters import HTTPAdapter


# -------------------------------------------------------------------
def get_args():
    """Get the command-line IP address argument"""

    parser = argparse.ArgumentParser(description="Input IPv4 address to check if exists in a group of supplied CIDRs.")
    parser.add_argument("ipv4", help="IPv4 address provided", type=ipaddress.IPv4Address)
    return parser.parse_args().ipv4


# -------------------------------------------------------------------
def mount_adapter(session):
    """Configure transport adapter retries and mount to session"""

    ripe_network_adapter = HTTPAdapter(max_retries=3)
    return session.mount("https://stat.ripe.net", ripe_network_adapter)


# -------------------------------------------------------------------
def get_data(session):
    """Get all data from webpage.  Setting timeout=(c, r) where c=connect timeout, r=read timeout
    """

    url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
    return session.get(url, timeout=(5, 30))


# -------------------------------------------------------------------
def return_json(response):
    """Return JSON object of the data result requested from webpage"""

    return response.json()


# -------------------------------------------------------------------
def get_ipv4_cidrs(json_response):
    """Get IPv4 CIDRs from JSON data result"""

    return json_response['data']['resources']['ipv4']


# -------------------------------------------------------------------
def check_ipv4_in_cidr(ipv4_addr, ipv4_cidrs):
    """Check if provided IPv4 address is present in CIDR ranges from data"""

    for cidr in ipv4_cidrs:
        if ipv4_addr in ipaddress.ip_network(cidr):
            print(f"PASS!  The provided IP {ipv4_addr} is in the CIDR range {cidr}.")
            break
    else:
        print(f"Fail.  The provided IP {ipv4_addr} is NOT in any of the CIDR ranges.")


# -------------------------------------------------------------------
def main():
    """Main logic for ip-checker program"""

    ipv4_addr = get_args()
    print(f"IPv4 Address Provided: {ipv4_addr}")

    try:
        with requests.Session() as session:

            mount_adapter(session)  # use context manager to mount adapter to session for retries

            print("Checking if CIDR data on webpage is available, then requesting data...")
            print("   > there's a lot of data, it may take a minute (insert: elevator theme music)")
            response = get_data(session)
            response.raise_for_status()  # Assert that there were no errors

    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}\nPlease try again.")
    except Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}\nPlease try again.")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}\nPlease try again.")
    except Exception as err:
        print(f"Other error occurred: {err}\nPlease try again.")
    else:
        print("CIDR data successfully captured.")
        json_response = return_json(response)
        ipv4_cidrs = get_ipv4_cidrs(json_response)
        print("Checking if IP provided is present in the list...")
        check_ipv4_in_cidr(ipv4_addr, ipv4_cidrs)


# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
