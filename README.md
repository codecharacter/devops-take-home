# Built: DevOps Take Home - Python Challenge
> Take an IP address and determine if it's in a range of CIDRs

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![](docs/images/dan-wadleigh-github-header-built.png)

## Requirements

- Take IP address as a command line argument
- Get JSON data from [RIPE Network Coordination Center](https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix)
- Using the ipv4 block in JSON:
  - Determine whether IP address provided on CLI is in any of the CIDRs
- Output a Pass/Fail result
  - based on the presence of the IP address in the CIDR ranges

## How to Setup

Run the following commands given Python 3.7+ is installed.

Developed on Python Version: 3.9.13  (pyenv local 3.9.13)

OS X & Linux:

```sh
# Clone repo from codecharacter GitHub
git clone https://github.com/codecharacter/devops-take-home.git
cd devops-take-home

# (Recommended) Set up virtual environment to safeguard from any package conflicts with current
python3 -m venv venv
source venv/bin/activate

# For running tests, install/restore dependencies from the requirements-dev.txt file
pip install -r requirements-dev.txt

# For running the script without test framework install/restore from requirements.txt
pip install -r requirements.txt
```

## Usage Examples

```shell
# Navigate to script directory
cd devops-take-home
python ip_checker.py [IPv4 address]

Example:
python ip_checker.py 2.56.8.1
```

Example Output for a PASS:

![](docs/images/devops-take-home-script-run-pass.png)

Example Output for a Fail:

![](docs/images/devops-take-home-script-run-fail.png)

## Running Tests

```shell
Framework: pytest

# In cloned GitHub directory (you may very well be aware of all this)
cd devops-take-home

pytest  # Run all tests
pytest tests/[filename].py  # Run any individual test

# Coverage report generated from pytest-cov plugin with:
coverage run ip-checker.py [ip-address]
```

![](docs/images/devops-take-home-coverage-report.png)

## Libraries/Tools Used

- [argparse](https://docs.python.org/3.9/library/argparse.html) (Std Lib)
  - The recommended command-line parsing module in the Python standard library.
  - Other modules that fulfill the same task: [getopt](https://docs.python.org/3.9/library/getopt.html#module-getopt), [optparse](https://docs.python.org/3.9/library/optparse.html#module-optparse) (deprecated)
  - argparse provides options: 
    - positional arguments, 
    - default value for arguments, 
    - help message, 
    - specifying data types of argument
- [ipaddress](https://docs.python.org/3.9/library/ipaddress.html) (Std Lib)
  - provides many capabilities to work with IP addresses (input) and networks (CIDRs)
  - including relevant to this task:
    - checking validity of an IP address (input)
    - iterating over all hosts in a particular subnet (CIDR)
- [requests](https://pypi.org/project/requests/) (PyPI)
  - the standard for making HTTP requests in Python
  - abstracts complexities of making requests so focus can be on consuming data & interacting with services
  - one of the most downloaded Python packages (~30M/wk)
  - relevant features:
    - keep-alive & connection pooling
    - timeouts
    - sessions
    - transport adapters
- [pytest](https://pypi.org/project/pytest/)
  - testing framework used to write tests for this exercise
  - alternate testing framework available (not used): [unittest](https://docs.python.org/3.9/library/unittest.html)
  - generally, easy to use, available resources online, usable output
    - ability to filter tests
    - allows test parametrization
- [pytest-cov](https://pypi.org/project/pytest-cov/)
  - plugin that produces coverage reports

## Workflow for Selecting Packages

I noted this workflow from one of the training courses I completed.  And am actively applying when possible.

### 1. Find Candidate Packages
   - Browse a curated list:
     - [awesome-python.com](https://awesome-python.com/), [python.libhunt.com](https://python.libhunt.com/), [python-guide.org](https://docs.python-guide.org/), [pymotw.com](https://pymotw.com/3/), [wiki.python.org](https://wiki.python.org/moin/)
   - Search Google 2-5 relevant keywords
   - Search Stack Overflow
   - Search Community Forums: Reddit, HackerNews, Twitter
   - Search PyPI directly
   . Ask a question on SO, Reddit, Twitter (slow)-
### 2. Check Package Popularity
   - Check download stats if available
   - Google/Reddit/SO recommendations
   - GitHub 'stars' (visible on PyPI)
   - python.libhunt.com popularity indicator
### 3. Check Project Homepage
   - Is it helpful?
   - Is it well-maintained?
   - How "successful" does the project look?
### 4. Check Project README
   - Does it cover what the project does & how to install it?
   - What license is the project under?
   - Who is the author?
### 5. Is the Project Actively Maintained?
   - Skim the changelog/update history
   - Is there activity on the bug tracker?
   - When was the last commit of the project?
### 6. Spot-Check the Source Code
   - note: growing in my ability to do this; principles apply
   - Does it follow best practices? (formatting, style, comments, docstrings)
   - Are there (automated) tests?
   - How experienced were the developers who wrote it?
   - Would I feel comfortable making small changes if I had to?
     - if I had to maintain the library going forward
### 7. Try Out a Few Candidates
   - Take the (narrowed down) list of candidates and try them out in an interpreter session.
   - Does the package install and import cleanly?
   - Do I enjoy working with the package?

## Resources

- argparse
  - [Python Docs: Argparse Tutorial](https://docs.python.org/3.9/howto/argparse.html)
  - [Read the Docs: argparse](https://pyneng.readthedocs.io/en/latest/book/additional_info/argparse.html)
- ipaddress
  - [Python Docs: An Intro to the ipaddress Module](https://docs.python.org/3.9/howto/ipaddress.html)
  - [RealPython.com: Learn IP Address Concepts with Python's ipaddress Module](https://realpython.com/python-ipaddress-module/)
- requests
  - [Read the Docs: requests](https://requests.readthedocs.io/en/latest/)
  - [RealPython.com: Python's Requests Library (Guide)](https://realpython.com/python-requests/)
- pytest
  - [pytest Docs](https://docs.pytest.org/en/7.1.x/)
  - [RealPython.com](https://realpython.com/pytest-python-testing/)
- pytest-cov
  - [Read the Docs: pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)

## Release History

* 1.0
    * ~~Work in progress~~ Submitted 6/24/2022

## Info: Dan Wadleigh

- Email: [dan@codecharacter.dev](mailto:dan@codecharacter.dev)
- Website: [www.CodeCharacter.dev](https://www.CodeCharacter.dev)
- LinkedIn: [LinkedIn Profile](https://linkedin.com/in/danwadleigh)
- Article: [So, What's the Deal with 'Code Character'?](https://codecharacter.dev/so-whats-the-deal-with-code-character/)

[https://github.com/codecharacter](https://github.com/codecharacter/)
