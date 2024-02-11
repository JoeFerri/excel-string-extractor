[![GitHub issues](https://img.shields.io/github/issues/JoeFerri/excel-string-extractor)](https://github.com/JoeFerri/excel-string-extractor/issues)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct-eng.md)

# Excel String Extractor
exsextractor is a Python script that scans Excel and CSV files, extracting all strings from every cell and consolidating them into one or more output files.

---

## Version
1.0.0-alpha
---

## Installation (!!!not yet working!!!)
```sh
pip install exsextractor (!!!not yet working!!!)
```
---

## Commands for installing and building the package within the virtual environment
```shell
$ cd PATH\excel-string-extractor
# create the virtual environment
$ python -m venv .venv
# activate the virtual environment
$ .venv\Scripts\activate

# install dependencies in the virtual environment
(.venv) $ pip install pytest
(.venv) $ pip install wheel
(.venv) $ pip install twine
(.venv) $ pip install tox
(.venv) $ pip install openpyxl

# install the package in the virtual environment
  # method 1: -e stands for editor mode
  (.venv) $ pip install -e .
  # method 2: install the package normally in build
  (.venv) $ pip install .

# create the dist folder
(.venv) $ python setup.py sdist
(.venv) $ python setup.py bdist_wheel
# check the files
(.venv) $ twine check dist/*
# create the requirements.txt file
(.venv) $ pip freeze > requirements.txt
# check the style of the python code
(.venv) $ flake8 src tests

# execute the integrated package test
(.venv) $ python
(.venv) >>> import exsextractor as ex
(.venv) >>> ex.test()

# execute the test
(.venv) $ cd path/test
  # Execute the test function with “verbose” reporting mode:
  (.venv) $ pytest
  # Execute the test function with “quiet” reporting mode:
  (.venv) $ pytest -q

# uninstall the package
(.venv) $ pip uninstall exsextractor
```

## Documentation
For the documentation see the notes inside the source code or [wiki page](https://github.com/JoeFerri/excel-string-extractor/wiki)

---

### Code of conduct
[ENG](code_of_conduct-eng.md)

[ITA](code_of_conduct-ita.md)

---

# License 

## MIT license 

Copyright (c) 2024 Giuseppe Ferri <jfinfoit@gmail.com>

Moral rights:
 Giuseppe Ferri <jfinfoit@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.