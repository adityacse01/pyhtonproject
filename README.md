Continuous Integration Demo
============================

Status of last [Travis CI build](https://travis-ci.com/jbrucker/demo-pyci):  
[![Build Status](https://travis-ci.com/jbrucker/demo-pyci.svg?branch=master)](https://travis-ci.com/jbrucker/demo-pyci)

This project demonstrates use of Travis CI to build and test a Python project.

> If you want to test this project using Travis CI,
> then you need to create your **own Github repo** for it.
>
> Therefore, **do not clone** this repo from Github.
> Download it as a **ZIP file**, create your own repo, then
> add Github as remote origin and push.

> Then give Travis access to your Github repo and trigger a build on Travis.

This application has some simple Python code and test classes for unit tests.  By convention, the test class files end in `_test.py`.

### Building the Application

[Travis-CI](https://travis-ci.com) is a continuous integration server for building, testing, and deploying software projects.  It works with many lanaguages and integrates easily with Github.

To enable Travis on a Python project you need to:

1. Create a Travis account on travis-ci.com using Github authentication.
2. On Github, in your Personal Settings page, select Applications. Choose "Travis" and add the project you want to use.  If you already gave Travis access to all your repos, skip this step.
3. In the repository, add a `.travis.yml` file containing configuration info.
    * Look at the [.travis.yml](.travis.yml) in this project as example.


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


### Test the Build

This project uses Python `unittest` for tests, which has an auto-discovery feature.  So we can run all tests using:
```shell
cmd> python -m unittest discover -p "*_test.py"
```

Once you get the tests to work, add it to `.travis.yml` as the "script" to run:
```yml
# commands to run automatically, on separate lines
script:
  - python -m unittest discover -p "*_test.py"
```
You might also be able to run tests via `pytest` which Travis uses by default:
```
script:
  - pytest
```

Another way to "build" and test Python projects is the
venerable GNU Make, which is available on Travis.  
If you want to use "make" in your project, then in `.travis.yml` write:
```
script:
  - make test
```
you must provide a Makefile with a `test` target that runs your tests.
There's really no benefit to this for Python, except as practice using Make.

### Enable Travis on Github

See links below for how to add Travis as an "Application" to your Github account.  You do this from the Travis-ci.com web site. 

After you grant Travis-CI access to your Github account, you can control which projects (repos) Travis has access to.  On Github:

1. Open the Person Settings page (under you photo, choose Settings).
2. Select Applications.
3. Select Travis-CI.
4. A screen is shown with options to either grant access to all repos or selected repos.


------
### More Info

[Building a Python Project](https://docs.travis-ci.com/user/languages/python/) with Travis CI. 

[Travis Getting Started Guide](https://docs.travis-ci.com/user/getting-started/)

