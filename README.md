Continuous Integration Demo
============================

Status of last [Travis CI build](https://travis-ci.com/jbrucker/demo-pyci):  
[![Build Status](https://travis-ci.com/jbrucker/demo-pyci.svg?branch=master)](https://travis-ci.com/jbrucker/demo-ci)

Demo project using Travis CI to build and test a Python project.

This application has some simple Python code and test classes using `unittest` to test the code.  By convention, the test class files end in `_test.py`.

### Building the Application

[Travis-CI](https://travis-ci.com) is a continuous integration server for building, testing, and deploying software projects.  It works with many lanaguages and integrates easily with Github.

The Travis configuration information is in [.travis.yml](.travis.yml).
Travis runs Python apps in a virtualenv. 
If your project requires any packages (such as Django),
use `pip` to add the required packages to the virtualenv.
The simplest way to do this (automatically) is to list your required packages 
in a file named `requirements.txt` and tell Travis to run:
```shell
pip install -r requirements.txt
```
The Python official docs explain the format of a requirements.txt file.

### Test the Build

This project uses the Python `unittest` library for tests, which has an auto-discovery feature.  So we can run all tests using:
```shell
cmd> python -m unittest discover -p "*_test.py"
```

Once you get the tests to work, add it to `.travis.yml` as the "script" to run:
```yml
# commands to run automatically, on separate lines
script:
  - python -m unittest discover -p "*_test.py"
```

Another way to "build" and test Python projects is the
venerable GNU Make utility, which is available on Travis.  
Make is very useful for more complex builds, 
the way Ant is used to build Java projects.
And makefiles are much human-readable than Ant build.xml files.

This project includes a Makefile with a `test` target.
So, in `.travis.yml` you could use:
```yml
script:
  - make test
```

### Managing Dependencies

If your Python project requires certain packages, specify the packages and versions in `requirements.txt` and enable these lines in `.travis.yml`:
```yml
# command to install dependencies
install:
  - pip install -r requirements.txt
```

### Enable Travis on Github

See links below for how to add Travis as an "Application" to your Github account.  You do this from the Travis-ci.com web site. Don't use the older travis-ci.org site.  

The Travis-CI site lets you configure project-specific settings, such as what branch it should build, and what triggers a build.  You can add pull requests as a trigger.

Then configure your Github project for Travis by adding a `.travis.yml` file.

------
### More Info

[Building a Python Project](https://docs.travis-ci.com/user/languages/python/) with Travis CI. 

[Travis Getting Started Guide](https://docs.travis-ci.com/user/getting-started/)

