"""
Docstring

How to set up a python package

- A pipenvironment, so import pipenv, run pipenv in the directory you intend to use it.
- Any LICENSE file you need.
- Create a setup file with these minimum things:
    - import setuptools
    - required packages
    - setuptools.setup(everything that's needed here)
- A folder by the same name; then the reason WHY this must be done this way.
- Within the package folder:
    - __init__.py
        - Docstring
        - Anything you need to import, as well as how to make sure it catches all of your functions, since that was a major issue for the people I worked with.
    - Any function files you have.
- THEN run those two lines of code you showed us in the powerpoint to upload it to test.pypi.org.









Upload to testpypi.org:
 Add
  python setup.py sdist bdist_wheel
 Remove
  rm dist

Push to testpypi.org
 twine upload --repository-url https://test.pypi.org/legacy/ dist/*
"""

import lambdata_joshuapmallory.plotting_functions
import lambdata_joshuapmallory.utility_functions

class thing:
    """
    This is a docstring
    """

    def __init__(self):
        variable = 1

    def some_function(self, x):
        print(x)

# import autopep8
# autopep8 --in-place __init__.py