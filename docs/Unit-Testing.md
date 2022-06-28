# Unit Testing

![](images/unit-testing.png)

## Unit Test - Martin Fowler

### Common Elements

  - low-level, focusing on a small part of the software system
  - written by programmers using regular tools
    - only difference is use of some unit testing framework
  - expected to be significantly faster than other kinds of tests

### Difference

  - what is considered to be a *unit*
  - OO design treats a class as the unit
  - procedural or functional approaches might consider a single function as a unit
  - situational - team decides what makes sense to be a unit for purposes of understanding system testing

### Solitary or Sociable?

  - Solitary Tests: some unit testers prefer to isolate the tested unit
  - Sociable Tests: often the tested unit relies on other units to fulfill its behavior
  - "unit testing" - tests are tests of the behavior of a single unit
    - write the tests assuming everything other than that unit is working correctly
  - schools of unit testing philosophy
    - classic and mockist styles
      - mockists insist upon solitary unit tests
      - classicists prefer sociable tests

### Speed

  - small scope, done by programmer, and fast
    - meaning they can be run very frequently
    - one of the key characteristics of *Self Testing Code*
  - Compile Suite
    - run whenever thinking of "compiling", even in an interpreted language (Python)
    - may not run all the unit tests
      - only need to run those tests operating over part of code currently working on
      - trade off with depth of testing with time to run test suite
  - Commit Suite
    - if using CI should run a test suite, that includes all the unit tests
    - should run several times a day
      - def before any shared commit to version control
      - the faster the commit suite is, the more often you can run it
    - Kent Beck's rule of thumb: should run in no more than 10 min
    - real point: test suites should run fast enough not discouraged from running them frequently enough
      - frequently enough so when a bug detected, there's a small amount of work to look through and find quickly

## How Unit Testing Made Me a Better Developer (SeeleyCoder.com)

### Unit Testing

  - level of software testing where individual units/components of a software are tested
  - a unit is the smallest testable part of any software
  - simply: writing code to test your code

### Why Should I Write Unit Tests?

  - even if you're a *great* developer, you're still not infallible
  - writing unit tests is just as important to protect you from yourself...
    - as it is to protect your code from somebody else
  - Scenario A: data related problem
    - add some additional checks and balances
    - how certain are you this problem won't happen again?
    - how might the situation be different had then been unit tests?
  - Scenario B: return to code months later
    - hard to follow code
    - afraid to make modifications to it
    - aren't comfortable with where it's at and can't make predictions for success
    - unit tests (good ones), help allow predictability and reduce/remove fear and doubt

### Reasons For and Benefits of Unit Tests

  - aggregated from sources: [DZone](https://dzone.com/articles/top-8-benefits-of-unit-testing) and [CODE Magazine](https://www.codemag.com/Article/1901071/10-Reasons-Why-Unit-Testing-Matters)
    - discipline and rigor / design / quality of code
    - does it work?
    - reduce cyclomatic complexity
    - your software is used before delivery
    - documentation (self-documenting)
    - measure the effort needed to modify an existing feature
    - *enforces inversion of control/dependency injection patterns*
    - code coverage
    - performance
    - enables continuous integration (CI)
    - reduce costs
    - *debugging process*
    - *finds software bugs early*

### Arguments Against Unit Tests

  - It's too hard
    - don't actually understand how to do it
    - ex: writing integration tests vs unit tests
  - I don't have the time
    - exponential long-term dividends vs short-term time savings value
  - It increases maintenance
    - unit tests are written against the smallest unit of work with application
    - if smallest unit of work is too complex then you're doing it wrong
  - It doesn't guarantee success
    - practicing good SOLID design principles

> *"I mean... doesn't everybody know how to unit test?  No.  No, they don't.  I didn't and neither did you.  Everybody has to learn at some point in time."*<br/>- **Jon Seeley (SeeleyCoder.com)**

### How to Unit Test

  - it's difficult to talk about unit testing without referring back to SOLID design principles
    - while it's possible to unit test without following them..
    - you're really just making your life more difficult than you need to
  - key points:
    - dependency injection
    - mocking
  - want to test the smallest unit possible ... what is that?
    - depending on pl: method or function
    - that's it, anything else is an integration test
  - What is Mocking?
    - substituting or simulating the behavior of the dependency
    - in the case of testing,
      - we can mock the behavior by stating the outcome of an action
  - Sample Tests
    - samples for contrived example (see article) ... principles of mocking
    - mocking the interfaces and *only* making them do something when want them to behave a certain way
      - each of the tests then is fairly minimal
      - would write unit tests against implementations of those interfaces as well

### How It Made Me a Better Developer

  - began writing tests against monolithic objects despite time and work involved
  - started seeing benefits as it caught bugs and narrowed scope
  - it was difficult, it was time-consuming, but it was still beneficial

### Found the Cadence

  - worked with other developers and consultants
  - particular job was nitpicky about unit tests
  - two things happened:
    - experienced a unit test epiphany
    - started both learning and applying SOLID design principles
  - unit testing helped properly apply SOLID design principles to code
  - gained added benefits that unit tests bring
  - writing unit tests will definitely empower you to write well-tested "bullet-proof" code

### Conclusion

  - unit testing is the practice of writing code to test your code
  - done properly, a unit test is written against the smallest unit of work within your app (aka, a method)
  - in order to reduce complexity of the test,
    - mock functionality of dependencies using mocking frameworks

> *"Before you can have unit tests, your code must be unit-testable."*<br/>- **John Peterson (CODE Magazine)**

## Beginner's Guide on Unit Tests (GitConnected.com)

### What is a Unit Test

  - usually focused on the functionality of a class, function, or UI component
    - and isolated from the external system - databases, 3rd-party API

### Why Bother to Write Unit Tests

  - The safety net of your software 
    - writing/refactoring: make sure you do not break existing functionality
  - increase confidence in shipping to prod

### Discover Mistakes as Early as Possible

  - unit tests should be written in an isolated manner
    - can be executed w/o having to spin up external services
    - can run fast
    - execute tests as much as needed during dev process

### Documentation

  - carefully written tests can act as docs
    - describes desired behavior of a piece of software
    - helpful during code review process
      - provides guidance on software behavior
      - eliminates need for going through implementation detail to understand functionality

### Short Intro on TDD

  - TDD can be summarized as a red-green-refactor approach to software dev
    - Write 1 test to cover 1 requirement
      - test should fail > don't have working implementation of system (red)
    - Write implementation
      - make it pass the test (green)
    - Refactor code (if necessary)
    - Move on to next requirement, back to step 1
  - Key: let the tests drive design, not the other way around

### Practices on Writing Unit Tests

  - Write Meaningful Test Name
    - golden rule: clear description of output and input
    - reader should be able to understand desired behavior...
      - w/o having to read the implementation detail of system under test
  - Each Test Should Cover Only 1 Scenario
    - with multiple functionalities, if test fails, don't know which functionality is failing

### Use AAA Pattern

  - Arrange > Act > Assert
    - improves the readability of the test by separating parts
  - Arrange
    - preparing the necessary fixtures, mocks, stubs, and system under test
  - Act
    - executing the functionality under test
  - Assert
    - asserting the result of execution against the desired value

### Isolate Unit from External Dependency

  - ex: adding functionality - how do we write a test for new functionality?
    - refactor class and use dependency injection...
      - to avoid direct dependency on another unit
    - then, easily assert against the injected mock
    - decouple implementation

### Avoid Testing Implementation Detail

  - example of testing implementation detail:
    - asserting sequence of function calls
    - asserting internal state of a class
  - testing implementation details should be avoided...
    - b/c it creates a tight coupling b/w tests and implementation

### Working on Legacy Code: Should I Refactor or Write Test First?

  - it depends
  - suggest writing a test before refactoring...
    - unless it is very hard to do so

> *"In the end, this technique (writing unit tests) would require some practice and discipline to master."*<br/>- **Danang Arbansa (GitConnected)**

## Resources

- [MartinFowler.com: Unit Test](https://martinfowler.com/bliki/UnitTest.html)
- [SeeleyCoder.com: How Unit Testing Made Me a Better Developer](https://www.seeleycoder.com/blog/how-unit-testing-made-me-better-developer/)
- [GitConnected.com: Beginner's Guide on Unit Tests](https://levelup.gitconnected.com/beginners-guide-on-unit-tests-1a6aeb3bac24)
- Examples:
  - [YouTube: How to Write Unit Tests for Existing Python Code - Part 1 (Arjan Codes)](https://www.youtube.com/watch?v=ULxMQ57engo)
  - [YouTube: How to Write Unit Tests for Existing Python Code - Part 2 (Arjan Codes)](https://www.youtube.com/watch?v=NI5IGAim8XU)

