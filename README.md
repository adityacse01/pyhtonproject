Continuous Integration Demo
============================

Status of last [Travis CI build](https://travis-ci.com/jbrucker/demo-pyci):  
[![Build Status](https://travis-ci.com/jbrucker/demo-pyci.svg?branch=master)](https://travis-ci.com/jbrucker/demo-ci)

Demo project using Travis CI to build and test a Python project.

[Travis-CI](https://travis-ci.com) is a continuous integration server for building, testing, and deploying software projects.  It works with many lanaguages and integrates easily with Github.

### Building the Application

Python doesn't require compilation, so its pretty simple.

Travis runs Python apps in a virtualenv.  Use `pip` to add any packages your project needs to the virtualenv, such as Django.  There are a few package managers available that work with `pip`, but the simplest way is to put your required packages in a file named `requirements.txt` and tell Travis to run:
```shell
pip install -r requirements.txt
```
The Python official docs explain the format of a requirements.txt file.

### Test the Build

This project uses the venerable (old) GNU Make to run tests, since it 
is mentioned on Travis CI.  The command to run tests is simple:
```shell
cmd> python -m unittest discover -p "*_test.py"
```
The only advantage of using a Makefile is that you don't have to escape wildcard characters and maybe quotes, which you need to do if you put the command directly in the `.travis.yml` file.

To run the tests using Make:
```shell
cmd> make test
```

### Managing Dependencies

If your Python project requires certain packages, since the packages and versions in `requirements.txt` and enable these lines in `.travis.yml`:
```yml
# command to install dependenceis
install:
  - pip install -r requirements.txt
```

### Enable Travis on Github

See links below for how to add Travis as an "Application" to your Github account.  You do this from the Travis-ci.com web site. Don't use the older travis-ci.org site.  

The Travis-CI site lets you configure project-specific settings, such as what branch it should build, and what triggers a build.  You can add pull requests as a trigger.

Then configure your Github project for Travis, such as adding a `.travis.yml` file.

------
### More Info

[Building a Python Project](https://docs.travis-ci.com/user/languages/python/) with Travis CI. 

[Travis Getting Started Guide](https://docs.travis-ci.com/user/getting-started/)

