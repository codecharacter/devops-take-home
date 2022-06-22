###################################################################################
# Exercise: Built Technologies - DevOps Take Home Challenge
# Author: Dan Wadleigh (6/21/2022)
# Overview: Write a program that will take an IP address from command line input,
# get ipv4 JSON data from a webpage, determine if the provided IP is in the
# CIDR range, and output a Pass/Fail based on that determination.
###################################################################################
import argparse
import ipaddress
import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError
from requests.adapters import HTTPAdapter


parser = argparse.ArgumentParser(description="Input IPv4 address to check if contained in a group of supplied CIDRs.")
parser.add_argument("ipv4", help="IPv4 address provided", type=ipaddress.IPv4Address)
ipv4_addr = parser.parse_args().ipv4
print(f"IPv4 Address Provided to Check: {ipv4_addr}")

ripe_network_adapter = HTTPAdapter(max_retries=3)
url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"

try:
    # Using context manager, ensures resources used by session released after use
    # In this case, enables mounting of Transport Adapter for retry attempts
    with requests.Session() as session:

        # Mounting transport adapter to CIDR webpage host with max retries
        session.mount("https://stat.ripe.net", ripe_network_adapter)

        # Setting timeout=(c, r) where c=connect timeout, r=read timeout
        print("Checking if CIDR data on webpage is available, then proceeding with checks...")
        response = session.get(url, timeout=(5, 30))

        # If the response was successful, no Exception will be raised
        response.raise_for_status()

except ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}\nPlease try again.")
except Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}\nPlease try again.")
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}\nPlease try again.")
except Exception as err:
    print(f"Other error occurred: {err}\nPlease try again.")
else:
    json_response = response.json()
    cidr_ranges = json_response['data']['resources']['ipv4']
    for cidr in cidr_ranges:
        if ipv4_addr in ipaddress.ip_network(cidr):
            print(f"Pass!  The provided IP address {ipv4_addr} is in the CIDR range {cidr}.")
            break
    else:
        print(f"Fail.  The provided IP address {ipv4_addr} is NOT in any of the CIDR ranges.")


# TODO - misc ongoing (comments, docstrings, linter, formatting, library/packages/resources)

# TODO - Pythonic refactoring (make it work > make it "pretty" > make it fast; classes/functions tbd)

# TODO - review README file (how to setup, example usage, testing)
