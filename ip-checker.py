###################################################################################
# Exercise: Built Technologies - DevOps Take Home Challenge
# Author: Dan Wadleigh (6/21/2022)
# Overview: Write a program that will take an IP address from command line input,
# get ipv4 JSON data from a webpage, determine if the provided IP is in the
# CIDR range, and output a Pass/Fail based on that determination.
###################################################################################
import argparse
import ipaddress


parser = argparse.ArgumentParser(description="Input IPv4 address to check if contained in a group of supplied CIDRs.")
parser.add_argument("ipv4", help="IPv4 address provided", type=ipaddress.IPv4Address)
ipv4_addr = parser.parse_args().ipv4

print(f"IPv4 Address: {ipv4_addr}")
print(type(ipv4_addr))

# ipv4_addr in ipaddress.ip_network(CIDR) ... List comprehension?

# TODO - validate command line input (loop to enter correct argument value?)

# TODO - get JSON data from webpage (request HTTP vs scrape; performance?)

# TODO - load/filter only the IPv4 JSON data (List, data type, CIDR formatting)

# TODO - determine whether IP provided on CLI is in any of CIDRs from JSON data (CIDR range checks, performance)

# TODO - output Pass/Fail from this result

# TODO - misc ongoing (comments, docstrings, linter, formatting, library/packages/resources)

# TODO - refactoring (make it work > make it "pretty" > make it fast; classes/functions tbd)
