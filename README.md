Pine State Software
Homework Assignment 5 - Intro to DevOps CI/CD
11/21/2022

The code our team added to this repository does the following:
1. Sorting - the sorting algoritms can be found in ./sort/sort.py
     Our team implemented quick sort, bubble sort, and insertion sort
2. Testing - The testing scripts can be found in ./test/test_basic_sort.py
     Our team uses pytest to implement testing 
     to run testing, from the project folder run the following code
     ` python -m pytest -q test/ `
3. Github Workflow - The workflow can be found in ./.github/workflows/first-action.yml
    more information about the github workflow can be found below
    

Our devops workflow has 2 parts:
1. Precommit checking
2. Workflow testing on push

Precommit checking is configured though our .pre-commit-config.yml file. It uses 4 different repositories to do the following:
1. check if AWS secret keys are included in the commit by utilizing git secrets
2. format code though python black
3. check the formating of code though flake8 
4. check the flile length to ensure no huge files are commited

After a push occurs our github workflow runs to test the following on python versions 3.9 and 3.10 :
1. Does the pushed code follow flake8 and python black formatting?
2. Do the test files return successful?
3. Can the project be built and packaged on Windows, Mac, and Ubuntu systems?
