# DevOps Exercise

This is a skeleton repository for your exercise. 
The goal of this exercise is to implement a Python package for sorting integer 
lists using the DevOps software development approach.

> **Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

You will need to:
1. Add .pre-commit-config.yml which:  
    1. Limits maximal file size.
    1. Runs the black and flake8 linters.
    1. Detect presence of aws credentials private keys.    
1. Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory,
code should be documented using standard Python practices (there are several [docstring 
styles](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
select one and be consistent).
1. Implement testing using the [pytest](https://docs.pytest.org/en/6.2.x/) framework, see test directory.
1. Implement linting, style checking using both [flake8](https://flake8.pycqa.org/en/latest/) and 
[black](https://black.readthedocs.io/en/stable/). 
1. Modify the GitHub actions workflow so that it tests and builds the package for all 
three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about [Distributing Python packages](https://docs.python.org/3/distributing/index.html).
1. Modify this file to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
1. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
    >**Warning**: Do not upload to the authoritative Python Package Index (PyPI).  


Possible work division, three sub-teams:
1. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
1. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
1. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).


The code our team added to this repository does the following:
1. Sorting - the sorting algoritms can be found in ./sort/sort.py
    our team implemented quick sort, bubble sort, and insertion sort
2. Testing - 
    

Our devops workflow has 2 parts:
1. Precommit checking
2. Workflow testing on push

Precommit checking is configured though our .pre-commit-config.yml file. It uses 4 different repositories to do the following:
1. check if AWS secret keys are included in the commit by utilizing git secrets
2. format code though python black
3. check the formating of code though flake8 
4. check the flile length to ensure no huge files are commited

After a push occurs our github workflow runs to test the following on python versions 3.9 and 3.10 :
1. Does the pushed code follow flake8 and python black formatting
2. Do the test files return successful 
3. Can the project be built and packaged on Windows, Mac, and Ubuntu systems
