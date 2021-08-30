# Continuous Integration with Python and CircleCI

I used CircleCI to perform continuous integration with Python.

Follow the step-by-step guide using CircleCI for Continuous Integration:
### 1. Understand the basic concepts

Continuous Integration
> _Continuous integration (CI) is the practice of automating the integration of code changes from multiple contributors into a single software project_

Build automation
> _Build automation is the process of automating the creation of a software build and the associated processes including: compiling computer source code into binary code, packaging binary code, and running automated tests_

Automated testing
> _Automated testing is a process that validates if software is functioning appropriately and meeting requirements before it is released into production_

Staging Environment
> _A staging environment is a nearly exact replica of a production environment for software testing. Staging environments are made to test codes, builds, and updates to ensure quality under a production-like environment before application deployment_

### 2. Create a repository in GitHub

### 3. Set up a virtual environment outside the repo:
```
python3 -m venv venv

. calculator/bin/activate
```

### 4. Create a Python file with your code and commit the code in GitHub

### 5. Install external packages to test your code
Analyze code for potential errors called as linting. We are using flake8 for linting along with a requirements.txt file which will help others to replicate your environment:
```
pip install flake8 pytest pytest-cov

pip freeze > requirements.txt
```

### 6. Execute the flake8 command and correct errors, if any:
```
flake8 --statistics
```

### 7. Create unit test 
Unit test is used to test a single function or a unit of test. We used pytest here for unit test:
```
pytest -v --cov
```

### 8. Connect to CircleCI
Create a .circleci folder and a ```config.yml``` file which includes intructions for all steps that the build server will need to execute

### 9. Connect to CircleCI 
Log in -> Add projects -> Select your repo -> Set Up Project -> Start Building

### 10. Try Test Driven Development (TDD)
TDD: write failing test then add a code which will pass the test and refactor



# Reference:
Check out this Python tutorial: Continuous Integration With Python: An Introduction
https://realpython.com/python-continuous-integration/
