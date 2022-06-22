# Built: DevOps Take Home - Python Challenge
> Take an IP address and determine if it's in a range of CIDRs

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![](github-header-built.png)

## Requirements

- Take IP address as a command line argument
- Get JSON data from [RIPE Network Coordination Center](https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix)
- Using the ipv4 block in JSON:
  - Determine whether IP address provided on CLI is in any of the CIDRs
- Output a Pass/Fail result
  - based on the presence of the IP address in the CIDR ranges

## How to Setup

Run the following commands given Python 3.8+ is installed.

OS X & Linux:

```sh
git clone https://github.com/codecharacter/devops-take-home.git
cd devops-take-home
pip install -r requirements.txt
```

## Usage Examples

```shell
# Navigate to script directory
cd devops-take-home
python ip_checker.py [IPv4 address]

Example:
python ip_checker.py 172.25.3.100
```
_(Pending) Examples of how the IP Checker program can be used (code blocks and screenshots)._

## Running Tests

_(Pending)_

## Libraries/Tools Used

- [argparse](https://docs.python.org/3.9/library/argparse.html)
  - The recommended command-line parsing module in the Python standard library.
  - Other modules that fulfill the same task: [getopt](https://docs.python.org/3.9/library/getopt.html#module-getopt), [optparse](https://docs.python.org/3.9/library/optparse.html#module-optparse) (deprecated)
  - argparse provides options: 
    - positional arguments, 
    - default value for arguments, 
    - help message, 
    - specifying data types of argument

## Decisions and Tradeoffs

_(Pending)_

## Resources

- argparse
  - [Python Docs: Argparse Tutorial](https://docs.python.org/3.9/howto/argparse.html)
  -  

## Release History

* 1.0
    * Work in progress

## Info: Dan Wadleigh

- Email: [dan@codecharacter.dev](mailto:dan@codecharacter.dev)
- Website: [www.CodeCharacter.dev](https://www.CodeCharacter.dev)
- LinkedIn: [LinkedIn Profile](https://linkedin.com/in/danwadleigh)
- Article: [So, What's the Deal with 'Code Character'?](https://codecharacter.dev/so-whats-the-deal-with-code-character/)

[https://github.com/codecharacter](https://github.com/codecharacter/)
