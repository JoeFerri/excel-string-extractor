[![GitHub issues](https://img.shields.io/github/issues/JoeFerri/excel-string-extractor)](https://github.com/JoeFerri/excel-string-extractor/issues)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct-eng.md)

# Excel String Extractor
exsextractor is a Python script that scans Excel files, extracting all strings from every cell and consolidating them into one or more output files.

---

## Version
1.0.0-alpha
---

## Installation (!!!not yet working!!!)
```sh
pip install exsextractor (!!!not yet working!!!)
```
---

## Usage
```sh
python -m exsextractor [options]
```
---

## Help Options
```
  -h, --help            show the help message
  -v, --version         show the version number
```
---

## Options Manual
```
Excel String Extractor CLI (exsextractor) [-h] [-v] [-u] [-uf FILE_NAME [FILE_NAME ...]] [-us SHEET_NAME [SHEET_NAME ...]] [-uc]
                                                 (-i FILE_NAME [FILE_NAME ...] | -l FILE_NAME [LIST_SHEET ...] | -lc FILE_NAME LIST_SHEET CONFIGURATION_SHEET)
                                                 [-co CONFIGURATION_FILE] [-gcj] [-gcx] [-o FILE_NAME] [-fo FORMAT] [-de DELIMITER] [-mp NUM_PROC] [-mt NUM_THR] [-oc SET]       
                                                 [-vl SET] [-d] [-w] [-t] [-s] [-r] [-re PATTERN] [-ic COLUMN [COLUMN ...]] [-ex COLUMN [COLUMN ...]] [-rn PAIR [PAIR ...]]      
                                                 [-ln PAIR [PAIR ...]] [-seq COLUMN]

exsextractor is a Python script that scans Excel and CSV files,
extracting all strings from every cell and consolidating them into one or more output files.

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

unique:
  the output will contain unique strings

  -u, --unique          the output will only contain unique strings
  -uf FILE_NAME [FILE_NAME ...], --unique-file FILE_NAME [FILE_NAME ...]
                        the output of the listed files will only contain unique strings
  -us SHEET_NAME [SHEET_NAME ...], --unique-sheet SHEET_NAME [SHEET_NAME ...]
                        the output of the listed sheets will only contain unique strings
  -uc, --unique-count   adds the "count" column with the number of occurrences of the string

files or list:
  files or list of input files

  -i FILE_NAME [FILE_NAME ...], --input FILE_NAME [FILE_NAME ...]
                        the input files to scan
  -l FILE_NAME [LIST_SHEET ...], --list FILE_NAME [LIST_SHEET ...]
                        FILE_NAME [str]: the file name with the list of files (required);
                        LIST_SHEET [str]: the name of the sheet where the list is inserted
                        if the list is an .xlsx file, then the file names are in the first sheet in column A starting from row 1 or 2;
                        if the file does not correspond to the Excel format and the LIST_SHEET argument is passed, the latter is ignored but a warning is generated;
  -lc FILE_NAME LIST_SHEET CONFIGURATION_SHEET, --list-config FILE_NAME LIST_SHEET CONFIGURATION_SHEET
                        FILE_NAME [str]: the file name with the list of files (required);
                        LIST_SHEET [str]: the name of the sheet where the list is inserted
                        CONFIGURATION_SHEET [str]: the sheet with the processing configuration
                        if the list is an .xlsx file, then the file names are in the first sheet in column A starting from row 1 or 2;
                        if the file does not correspond to the Excel format and the LIST_SHEET argument is passed, the latter is ignored but a warning is generated;

configuration:
  options for configuration

  If there's a conflict in the configuration files the rightmost command prevails from the passed parameter list
  (a Warning is shown on the terminal)

  -co CONFIGURATION_FILE, --config CONFIGURATION_FILE
                        the file.json is used for the processing configuration
                        used instead or together with command line parameters
  -gcj, --gen-config-json
                        generates a exse-config.json with the default configuration;
                        the configuration file will contain all the custom values passed from the command line
  -gcx, --gen-config-xlsx
                        generates a exse-config.xlsx with the default configuration;
                        the configuration file will contain all the custom values passed from the command line

output:
  options for output

  -o FILE_NAME, --out FILE_NAME
                        the name of the output file with or without extension;
                        the default name is "output.xlsx";
                        the default extension is ".xlsx"
  -fo FORMAT, --format-out FORMAT
                        overwrites the output file extension
                        choices: "xlsx", "csv";
                        default = "xlsx"
  -de DELIMITER, --delimiter DELIMITER
                        delimiter if the format is csv;
                        default = ";"

processing:
  Internally a fileList contains 1 or n files to be processed;
  for each file in fileList execute result = process_file(file);
  process_file() is executed in parallel by a process p_n in Pool;
  each p_n processes the sheets of the single file;
  each sheet is processed by a thread in Pool

  -mp NUM_PROC, --multi-proc NUM_PROC
                        use NUM_PROC number of processes in multiprocessing;
                        default = 1 process;
                        max = 16 process
  -mt NUM_THR, --multi-thr NUM_THR
                        use NUM_THR number of threads in multithreading;
                        default = 1 thread;
                        max = 32 threads

capture:
  by default only strings with at least one alphabetical character are captured;
  by default the captured strings are inserted into
  a single "value" column regardless of their capture type;

  the parameters -d, -w, -t, -s, -r, -re are cumulative;

  if -oc is set to True (default), for each output record there will be associated
  a value for the "value" column (captured string) and
  a value for the "type" column (capture type "digit", "word" , "text", "string", "raw", "regex");

  if -oc is set to False, for each record there will be an associated value for both the "value" column
  and the capture type column, i.e. for each record there will be both
  the "digit", "word", " columns text", "string", "raw", "regex" and the "value" column;

  -oc SET, --one-column-capture SET
                        the captured strings are inserted into a single "value" column
                        regardless of their capture type (default True)
  -vl SET, --value SET  only strings with at least one alphabetical character are captured (default True)
  -d, --digit           strings of only numbers are captured (default False)
  -w, --word            only strings with a single word are captured (default also strings with spaces)
  -t, --text            only strings with alphabetical characters and 0 or n spaces are captured (default False)
  -s, --string          only strings with alphabetical characters (1 or n) and
                        numbers (1 or m) with 0 or k intermediate spaces are captured (default False)
  -r, --raw             all strings are captured (default False)
  -re PATTERN, --regex PATTERN
                        only strings matching the pattern are captured

columns:
  options for the output columns

  -ic COLUMN [COLUMN ...], --include-column COLUMN [COLUMN ...]
                        if set, only the indicated columns will be created in the output;
                        the "value" column is not affected by this parameter
  -ex COLUMN [COLUMN ...], --exclude-column COLUMN [COLUMN ...]
                        if set, the indicated columns will not be generated in the output;
                        the "value" column is affected by this parameter
  -rn PAIR [PAIR ...], --rename PAIR [PAIR ...]
                        changes the column names;
                        the arguments passed must follow the following pattern: <COLUMN_NAME>=<NEW_COLUMN_NAME>;
                        pairs (name1,name2) are separated by spaces;
                        to use the equal character you need to escape `%=`;
                        Examples:
                        -rn seq=SEQ "string = COL 2" value=COL%=3
                        rename column `seq` to `SEQ`, `string` to `COL 2` and `value` to `COL=3`
                        -rn 'value="COL%= 3"'
                        rename the `value` column to `"COL= 3"`
  -ln PAIR [PAIR ...], --label-name PAIR [PAIR ...]
                        creates labels identifying files, sheets, columns,
                        callable in command line commands
                        to make the command line string more readable;
                        the arguments passed must follow the following pattern: <COLUMN_NAME>==<LABEL>;
                        to use the equal character you need to escape `%==`;
                        Examples:
                        -ln file.xlsx==f1 "SHEET %== 1 A == S1A" string==S value==V -ex V S seq
                        exclude the columns value, string and seq
  -seq COLUMN, --sequence COLUMN
                        changes the depth level of the sequential number associated with the record;
                        -ic seq 0: adds the sequential number column at cell level (never resets)
                        -ic seq 1: adds the sequential number column at sheet level (resets with each sheet)
                        -ic seq 2: adds the sequential number column at file level (resets with each file)
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