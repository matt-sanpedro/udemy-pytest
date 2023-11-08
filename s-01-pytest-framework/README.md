# Pytest Framework

## Introduction
- frameworks structure our test
- helpful features
- focus on writing and adding tests

## Pytest
- test framework based on Python language
- easy to write, execute, and generate test reports
- different types and levels of testing
- used by developers and QA team

## Features
- auto-detect test
- uses Python's assert keyword
- can run tests written for "unittest" or "nose"
- CI/CD integration
- good features: fixtures, parameterize, etc
- good community support

## Hybrid Framework Goal
- modular
- data-driven design
- Library/Utils

## Pytest useful commands
- run tests in specific directory in verbose mode: ```pytest -v test_dir```
- run specific test with the "-k" flag: ```pytest -v -k a5```
- run multiple specific tests with or keyword: ```pytest -v -k "a1 or a2"```
- list all the tests and python packages: ```pytest -v --collect-only```
- run tests and exit if failure encountered: ```pytest -v --exitfirst```

## Pytest markers
- test can have multiple markers
- a marker can be on multiple tests
