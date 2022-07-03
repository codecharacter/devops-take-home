# Design Decisions

> The method to the madness.  Review exercise design decisions.<br/>
> Identify opportunities to learn and improve - Coder, code, coding practices/skills.<br/>
> Learn "why" of the tools, not just "what/how" to use them.  Become skillful at using the language tools effectively (Pythonic).

## Source Code

### Overview

### main.py

### ipcheck Package

### iparg.py

### cidrdata.py

### checkip.py

## Unit Tests

### Test Framework: pytest

### test_iparg.py

### test_cidrdata.py

### test_checkip.py

## Summary

## Misc Notes

- packages/modules/libraries
  - [Difference Between Python Modules, Packages, Libraries, and Frameworks](https://learnpython.com/blog/python-modules-packages-libraries-frameworks/)
- namespaces
  - [Namespaces and Scope in Python](https://realpython.com/python-namespaces-scope/)
- \_\_main\_\_
  - [Defining Main Functions in Python](https://realpython.com/python-main-function/)
- Standard Library (PyMOTW)
  - [The Python Standard Library](https://docs.python.org/3.9/library/)
- Python Docs
  - [Python Documentation](https://docs.python.org/3.9/)
- PyPI
  - [Python Package Index: PyPI](https://pypi.org/)
- StdLib: argparse
  - [argparse - Parser for command-line options, arguments and sub-commands](https://docs.python.org/3.9/library/argparse.html)
  - [Argparse Tutorial](https://docs.python.org/3.9/howto/argparse.html#id1)
- StdLib: ipaddress
  - [ipaddress - IPv4/IPv6 manipulation library](https://docs.python.org/3.9/library/ipaddress.html)
  - [An introduction to the ipaddress module](https://docs.python.org/3.9/howto/ipaddress.html#ipaddress-howto)
- PyPI: requests
  - [PyPI: requests](https://pypi.org/project/requests/)
  - [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
- PyPI: responses
  - [PyPI: responses](https://pypi.org/project/responses/)
  - [GitHub: getsentry/responses](https://github.com/getsentry/responses)
- for ... Loop
  - [Python "for" Loops (Definite Iteration)](https://realpython.com/python-for-loop/)
- Functions
  - [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
- try...except...else
  - [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- StdLib vs requests.exceptions
  - ConnectionError
    - [Python Built-in Exceptions](https://realpython.com/python-exceptions/)
    - [requests.ConnectionError](https://requests.readthedocs.io/en/latest/api/#requests.ConnectionError)
  - Exception
    - [Python Errors and Exceptions](https://docs.python.org/3.9/tutorial/errors.html)
    - [Source Code for requests.exceptions](https://requests.readthedocs.io/en/latest/_modules/requests/exceptions/)
- response.raise_for_status
  - HTTPError
    - [requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
    - [response.raise_for_status() - Python requests](https://www.geeksforgeeks.org/response-raise_for_status-python-requests/)
- Test Framework: pytest
  - [pytest: helps you write better programs](https://docs.pytest.org/en/7.1.x/)
- capsys
  - [How to capture stdout/stderr output](https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html)
  - [Using capsys: Python Testing with pytest (Brian Okken)](https://medium.com/pragmatic-programmers/using-capsys-71b7f482d00a)
  - [Pytest capsys](https://waylonwalker.com/pytest-capsys/)
    - readouterr
- Assertions
  - [Python's assert: Debug and Test Your Code Like a Pro](https://realpython.com/python-assert-statement/)
  - [Python assert Keyword](https://www.w3schools.com/python/ref_keyword_assert.asp)
- pytest.raises
  - [How to write and report assertions in tests](https://docs.pytest.org/en/7.1.x/how-to/assert.html?highlight=assert)
- f-strings
  - [Python 3's f-Strings: An Improved String Formatting Syntax (Guide)]
- Context Manager
  - with...
    - [Context Managers and Python's with Statement](https://realpython.com/python-with-statement/)
- Classes
  - [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- Mocks
  - [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/)
  - [Python Mocking 101: Fake It Before You Make It](https://www.fugue.co/blog/2016-02-11-python-mocking-101)
  - [pytest: How to mock in Python](https://changhsinlee.com/pytest-mock/)
- @staticmethod
  - [Python's Instance, Class, and Static Methods Demystified](https://realpython.com/instance-class-and-static-methods-demystified/)
  - [Class method vs Static method in Python](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)
- Fixtures
  - [Effective Python Testing with Pytest](https://realpython.com/pytest-python-testing/)
  - [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)
    - @pytest.fixture
- monkeypatch
  - [How to monkeypatch/mock modules and environments](https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html)
  - [Monkey Patching in Python (Dynamic Behavior)](https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/)
- *args, **kwargs (unused?)
  - [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args/)
- "mock_response"
- @responses.activate
  - [responses: Basics](https://github.com/getsentry/responses#basics)
  - [Responses: A Utility for Mocking Out the Python Requests Library](https://morioh.com/p/fbaf641a18c7)
    - able to parametrize these? ... DRY
- responses.add
  - [PyPI: responses - Main Interface](https://pypi.org/project/responses/#main-interface)
- Parametrize
  - [How to Use Fixtures as Arguments in pytest.mark.parametrize](https://miguendes.me/how-to-use-fixtures-as-arguments-in-pytestmarkparametrize)
    - @pytest.mark.parametrize
- Software Design/Architecture (SOLID principles)
  - [Uncle Bob's SOLID principles made easy - in Python!](https://www.youtube.com/watch?v=pTB30aXS77U)
- Testing
- TDD
- Unit Testing
- Managing Dependencies
  - [Understanding setup.py, setup.cfg and pyproject.toml in Python](https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/)
    - setup.py, setup.cfg
    - conftest.py
    - [pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/6.2.x/fixture.html)
    - [Share fixtures among test files: conftest.py](https://code-maven.com/slides/python/pytest-conftest)
- Dev Workflow
  - IDE
  - Virtual Env
  - pyenv
- Git practices
- CPython
  - [Wikipedia: CPython](https://en.wikipedia.org/wiki/CPython)
- Python
  - [Wikipedia: Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- type
  - dynamic
    - [Dynamic vs Static](https://realpython.com/lessons/dynamic-vs-static/)
    - [Why Python is called Dynamically Typed?](https://www.geeksforgeeks.org/why-python-is-called-dynamically-typed/)
  - strong
    - [Using static typing](https://www.futurelearn.com/info/courses/python-in-hpc/0/steps/65121#:~:text=Python%20is%20both%20a%20strongly,is%20determined%20only%20during%20runtime.)
- typing
  - duck
    - [Duck Typing](https://realpython.com/lessons/duck-typing/)
  - gradual
    - [Python Type Checking (Guide)](https://realpython.com/python-type-checking/)
  - type hints
    - [Type Hinting](https://realpython.com/lessons/type-hinting/)
    - [5 Reasons Why You Should Use Type Hints in Python](https://www.youtube.com/watch?v=dgBCEB2jVU0)
- programming paradigms
  - imperative
    - object-oriented
    - procedural
  - declarative
    - functional
    - concurrent
- objects