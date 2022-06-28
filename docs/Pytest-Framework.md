# Pytest Framework

![](images/pytest-framework.png)

## Effective Python Testing with Pytest (RealPython.com)

### What Makes *pytest* So Useful?

- **Less Boilerplate**
  - most functional tests follow Arrange-Act-Assert model
    - Arrange: set up, the conditions for the test
    - Act: by calling some function or method
    - Assert: that some end condition is true
  - pytest simplifies workflow by allowing use of normal functions and Python's *assert* keyword directly
- **Nicer Output**
  - can run test suite using the *pytest* command from to-level folder of project
  - report shows:
    - system state: incl versions of Python, pytest, any plugins installed
    - rootdir: or dir to search under for config and tests
    - number of tests the runner discovered
  - failed tests gives a detailed breakdown of the failure
- **Less to Learn**
  - being able to use the *assert* keyword is powerful
  - normal Python functions makes learning curve shallower
    - don't need to learn new constructs
  - each test is small and self-contained
    - see long function names and not a lot going on in functions
    - serves to keep tests isolated from each other
      - if something breaks, know exactly where problem is
- **Easier to Manage State and Dependencies**
  - tests will often depend on types of data or *test doubles* that mock objects
  - tests should help make code more understandable
  - *explicit* dependency declarations
    - still reusable with *fixtures*
    - *fixtures* - functions that can create data, test doubles, or initialize system state for test suite
  - note: usu want to put tests into their own folder *tests* at root level of project
- **Easy to Filter Tests**
  - ability to run a few tests on a feature
  - ways of doing this:
    - *Name-based filtering*
    - *Directory scoping*
    - *Test categorization*
      - with *marks*, or custom labels
- **Allows Test Parametrization**
  - ability to eliminate duplicating test code
  - provide functions with process data
- **Has a Plugin-Based Architecture**
  - open to customization and new features
  - users have developed an ecosystem of plugins

### Fixtures: Managing State Dependencies

- *pytest fixtures*: a way of providing data, test doubles, or state setup to tests
  - functions that can return a wide range of values
  - each test that depends on a fixture must *explicitly* accept that fixture as an argument
  - can be used to reduce code duplication by extracting common dependencies
- **When to Create Fixtures**
  - one of the advantages of TDD is that it helps plan out the work ahead
  - when you find yourself writing several tests that all make use of the same underlying test data
    - can pull the repeated data into a single function decorated with *@pytest.fixture* 
      - indicates that the function is a *pytest* fixture
    - can use the fixture by adding the function reference as an argument to tests
      - able to use the return value of the fixture function as the name of the fixture function
  - be sure to name fixture something specific
    - then, can quickly determine if you want to use it when writing new tests
- **When to Avoid Fixtures**
  - good for:
    - extracting data or objects used across multiple tests
  - not good for:
    - tests that require slight variations in the data
- **How to Use Fixtures at Scale**
  - in pytest fixtures are *modular*, means that:
    - fixtures can be imported,
    - can import other modules,
    - can depend on and import other fixtures
  - *conftest.py*
    - add general purpose fixtures to this module
    - use case: making fixture available for whole project w/o having to import it
    - use case: guarding access to resources
      - monkeypatch fixture - replace values and behaviors

### Marks: Categorizing Tests

- pytest enables ability to define categories for tests, and provides options:
  - *including* categories
    - ex: *pytest -m db_access*
  - *excluding* categories
    - ex: *pytest -m "not db_access"*
- can mark a test with any number of categories
  - marking tests useful for categorizing tests by:
    - subsystem, or
    - dependencies
- pytest provided *marks* out of the box:
  - *skip*: skips a test unconditionally
  - *skipif*: skips a test if the expressions passed to it evaluates to True
  - *xfail*: indicates a test is expected to fail, so if test fails, overall suite can still pass
  - *parametrize*: creates multiple variants of a test w/difft values as args
  - note: to see all marks > *pytest --markers*

### Parametrization

- fixtures aren't quite as useful when you have several tests with slightly diff't inputs & expected outputs
- *parametrize* a single test definition
  - pytest will create variants of the test with parameters supplied
  - ex: *@pytest.mark.parametrize*
- can use *parametrization* to:
  - separate test data from test behavior
    - so it's clear what the test is testing, and
    - make diff't test cases easier to read and maintain

### Durations Reports: Fighting Slow Tests

- *overhead* each time switch contexts from implementation code to test code
- *marks* can filter out slow tests when running suite
  - but will need to run at some point
- *improve speed* of tests - know *which* tests offer biggest improvements
- pytest can automatically record test durations and report top offenders
  - ex: *pytest --durations=5*
  - note: short durations are hidden by default

### Useful pytest Plugins

- *pytest-randomly*
  - forces tests to run in a random order
  - great way to uncover tests that depend on running in a specific order
    - means they have a *stateful dependency* on some other test
- *pytest-cov*
  - measures how well tests cover implementation code
  - ex: *pytest --cov*
- *pytest-django*
  - provides useful fixtures and marks for dealing with Django tests
- *pytest-bdd*
  - helps write feature tests for code

### Conclusion

  - **Fixtures** for handling test dependencies, state, and reusable functionality
  - **Marks** for categorizing tests and limiting access to external resources
  - **Parametrization** for reducing duplicated code between tests
  - **Durations** to identify the slowest tests
  - **Plugins** for integrating with other frameworks and testing tools

## Resources

- [Pytest Docs: Get Started, How-to Guides, Library of Examples](https://docs.pytest.org/en/7.1.x/)
- [RealPython.com: Effective Python Testing with Pytest](https://realpython.com/pytest-python-testing/)
- [Udemy: Practical Python Unit Testing with Pytest + Mocking](https://www.udemy.com/course/practical-unit-testing-for-python-with-pytest-and-mocking/)
