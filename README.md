# Intercom Technical Problem

Intercom Technical Problem project done in **Python** by **Ricardo Serra**.

## Prerequisites
**Python 3.7** is required and you can check how to install Python in your favorite OS following this URL:  https://wiki.python.org/moin/BeginnersGuide/Download

You'll also need **pipenv** before you proceed. **pipenv** is a tool that brings together **pip** and **virtualenv** to allow dependency management and virtual environments creation.
```
pip3 install pipenv
```
## Instalation
First, we need to install the dependencies:
```
cd intercom_challenge
pipenv install --dev --ignore-pipfile --deploy
```
This will create a virtualenv with all dependencies listed on Pipfile.lock using the exact same versions.
Then, *we need to enter our newly created virtualenv with all our dependencies (to run or test the program)*:
```
pipenv shell
```
## Usage
To run the program, type:
```
python main.py
```
On success 'output.txt' file will be created with all customers within 100KM from Intercom's office. You can also check program's result in 'output/output.txt'.

## Tests
To run all unit tests, make sure you have your virtualenv activated (pipenv shell):
```
pytest
```
All tests should pass.

## Dependencies
**pytest** - Unit test package that allows clean and simple unit tests

**flake8** - Package that wraps PyFlakes, pycodestyle and McCabe packages to check code against coding style (PEP8), programming errors and to check cyclomatic complexity

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

