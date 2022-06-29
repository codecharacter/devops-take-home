from setuptools import setup, find_packages

setup(
    name="devops-take-home",
    version="2.0",
    description="Setting up the ipcheck package",
    author="Dan Wadleigh",
    author_email="dan@codecharacter.dev",
    packages=find_packages(include=["ipcheck", "ipcheck.*"]),
    install_requires=[
        "requests==2.28.0",
    ],
    setup_requires=["pytest-runner", "pytest-cov"],
    tests_require=["pytest"],
)
