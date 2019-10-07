Continuous Integration Demo
============================

Status of last [Travis CI build](https://travis-ci.com/jbrucker/demo-pyci):  
[![Build Status](https://travis-ci.com/jbrucker/demo-pyci.svg?branch=master)](https://travis-ci.com/jbrucker/demo-pyci)

This project demonstrates use of Travis CI to build and test a Python project.  To do this, you first need a git repo with a remote on Github.

### Setup

1. Download `demo-pyci.zip`.
2. Change to a directory where you store projects (but **not** inside any git repo) and unpack the zip file.  This will create a subdir like this:
    ```
    demo-pyci/
        README.md
        stats.py
        stats_test.py
    ```
3. Change dir to `demo-pyci` and do:
   - create a git repository
   - add all 3 files
   - create and add a .gitignore file for Python projects.  You should at least ignore `__pycache__` dirs.
   - commit everything to the git repo
4. Create a public `demo-pyci` repo on Github and
   - add it as remote for your local repo
   - push everything to Github

## Run the Tests Locally - One test should FAIL

Run the tests yourself to verify the code (almost) works.
We will then "script" this command for Travis to run for us.

Run the unit tests using auto-discovery (so you don't
need to the name of the test file) using:
```bash
  python -m unittest discover -p "*_test.py"
```
The `-p "*_test.py"` defines a **pattern** for unit test files.
If you wanted files *beginning* with "test_" you would use
`-p test_*.py`.

It should run 3 tests and one test fails.

**Don't fix it**  We want a failure so you can see how Travis notifies you.

## Add Travis for CI

[Travis-CI](https://travis-ci.com) is a continuous integration server for building, testing, and deploying software projects.  It works with many lanaguages and integrates easily with Github.

1. Create a Travis account on travis-ci.com using Github authentication.
   - When you connect your Travis account to Github, a dialog will ask which Github projects you want to allow Travis to access.
   - You can grant access to specific projects or all projects. The next step (here) shows how to grant access to a project at any time.
2. On Github, in your Personal Settings page, select Applications. Choose "Travis" and add the project you want to Travis to test.  
    - If you already gave Travis access to all your repos, skip this step.
    - Otherwise, grant access to the `demo-pyci` project.
3. In your local repository, add a Travis Configuration file named `.travis.yml` that describes your project.  Here is a simple `.travis.yml` for this project:
    ```
    language: python
    
    python:
      - "3.6"
    
    # don't clone more than necessary
    git:
      depth: 1
    
    # Install dependencies
    install:
      - pip install -r requirements.txt
    
    # script to run tests. Can also use make, e.g. "make test"
    script: 
      - python -m unittest discover -p "*_test.py"
    ```
4. Add your `.travis.yml` file to the git repo, commit it, and push to Github.
5. Next go to https://travis-ci.com/your_githubid/demo-pyci.  You should see Travis pull, build, and run the project.

Travis runs Python apps in a virtualenv. 

If your project requires any packages (such as Django),
use `pip` to add the required packages to the virtualenv.
A common way to do this is you list required packages 
in a file named `requirements.txt`.  
Tell Travis to install these packages; in the `.travis.yml` file add:
```shell
# Install dependencies
install:
  - pip install -r requirements.txt
```

The Python official docs explain the format of a requirements.txt file.



Another way to "build" and test Python projects is the
venerable GNU Make, which is available on Travis.  
If you want to use "make" in your project, then in `.travis.yml` write:
```
script:
  - make test
```
you must provide a Makefile with a `test` target that runs your tests.
There's really no benefit to this for Python, except as practice using Make.




------
### More Info

[Building a Python Project](https://docs.travis-ci.com/user/languages/python/) with Travis CI. 

[Travis Getting Started Guide](https://docs.travis-ci.com/user/getting-started/)

