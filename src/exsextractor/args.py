"""Args for exsextractor."""

from .utils import nargs_range
from .utils import bool_parser
from .utils import pair_parser
from . import __version__
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Excel String Extractor CLI (exsextractor)',
        description='''exsextractor is a Python script that scans Excel and CSV files,
extracting all strings from every cell and consolidating them into one or more output files.''',
        epilog='''.
.
. . . Copyright (c) 2024 Giuseppe Ferri <jfinfoit@gmail.com>
. . . Licensed under the MIT License.
.
.''',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    unique_group = parser.add_argument_group('unique', 'the output will contain unique strings')

    unique_group.add_argument(
        '-u', '--unique',
        default=False,
        action='store_true',
        help='the output will only contain unique strings')

    unique_group.add_argument(
        '-uf', '--unique-file',
        nargs='+',
        metavar=('FILE_NAME'),
        default=[],
        help='the output of the listed files will only contain unique strings')

    unique_group.add_argument(
        '-us', '--unique-sheet',
        nargs='+',
        metavar=('SHEET_NAME'),
        default=[],
        help='the output of the listed sheets will only contain unique strings')

    unique_group.add_argument(
        '-uc', '--unique-count',
        default=False,
        action='store_true',
        help='adds the "count" column with the number of occurrences of the string')

    files_or_list_group = parser.add_argument_group('files or list', 'files or list of input files')

    exclusive_files_or_list_group = files_or_list_group.add_mutually_exclusive_group(required=True)

    exclusive_files_or_list_group.add_argument(
        '-i', '--input',
        nargs='+',
        default=[],
        metavar=('FILE_NAME'),
        help='the input files to scan')

    exclusive_files_or_list_group.add_argument(
        '-l', '--list',
        nargs='+',
        action=nargs_range(1, 2),
        default=[],
        metavar=('FILE_NAME', 'LIST_SHEET'),
        help='''FILE_NAME [str]: the file name with the list of files (required);
LIST_SHEET [str]: the name of the sheet where the list is inserted
if the list is an .xlsx file, then the file names are in the first sheet in column A starting from row 1 or 2;
if the file does not correspond to the Excel format and the LIST_SHEET argument is passed, the latter is ignored but a warning is generated;''')

    exclusive_files_or_list_group.add_argument(
        '-lc', '--list-config',
        nargs=3,
        default=[],
        metavar=('FILE_NAME', 'LIST_SHEET', 'CONFIGURATION_SHEET'),
        help='''FILE_NAME [str]: the file name with the list of files (required);
LIST_SHEET [str]: the name of the sheet where the list is inserted
CONFIGURATION_SHEET [str]: the sheet with the processing configuration
if the list is an .xlsx file, then the file names are in the first sheet in column A starting from row 1 or 2;
if the file does not correspond to the Excel format and the LIST_SHEET argument is passed, the latter is ignored but a warning is generated;''')

    config_group = parser.add_argument_group('configuration', '''options for configuration

If there's a conflict in the configuration files the rightmost command prevails from the passed parameter list
(a Warning is shown on the terminal)''')

    config_group.add_argument(
        '-co', '--config',
        nargs=1,
        default=[],
        metavar=('CONFIGURATION_FILE'),
        help='''the file.json is used for the processing configuration
used instead or together with command line parameters''')

    config_group.add_argument(
        '-gcj', '--gen-config-json',
        default=False,
        action='store_true',
        help='''generates a exse-config.json with the default configuration;
the configuration file will contain all the custom values passed from the command line''')

    config_group.add_argument(
        '-gcx', '--gen-config-xlsx',
        default=False,
        action='store_true',
        help='''generates a exse-config.xlsx with the default configuration;
the configuration file will contain all the custom values passed from the command line''')

    output_group = parser.add_argument_group('output', 'options for output')

    output_group.add_argument(
        '-o', '--out',
        nargs=1,
        default=[],
        metavar=('FILE_NAME'),
        help='''the name of the output file with or without extension;
the default name is "output.xlsx";
the default extension is ".xlsx"''')

    output_group.add_argument(
        '-fo', '--format-out',
        nargs=1,
        default=['xlsx'],
        choices=['xlsx', 'csv'],
        metavar=('FORMAT'),
        help='''overwrites the output file extension
choices: "xlsx", "csv";
default = "xlsx"''')

    output_group.add_argument(
        '-de', '--delimiter',
        nargs=1,
        default=[';'],
        metavar=('DELIMITER'),
        help='''delimiter if the format is csv;
default = ";"''')

    processing_group = parser.add_argument_group('processing', '''Internally a fileList contains 1 or n files to be processed;
for each file in fileList execute result = process_file(file);
process_file() is executed in parallel by a process p_n in Pool;
each p_n processes the sheets of the single file;
each sheet is processed by a thread in Pool''')

    processing_group.add_argument(
        '-mp', '--multi-proc',
        nargs=1,
        default=[1],
        type=int,
        choices=range(1, 17),
        metavar=('NUM_PROC'),
        help='''use NUM_PROC number of processes in multiprocessing;
default = 1 process;
max = 16 process''')

    processing_group.add_argument(
        '-mt', '--multi-thr',
        nargs=1,
        default=[1],
        type=int,
        choices=range(1, 33),
        metavar=('NUM_THR'),
        help='''use NUM_THR number of threads in multithreading;
default = 1 thread;
max = 32 threads''')

    capture_group = parser.add_argument_group('capture', '''by default only strings with at least one alphabetical character are captured;
by default the captured strings are inserted into
a single "value" column regardless of their capture type;

the parameters -d, -w, -t, -s, -r, -re are cumulative;

if -oc is set to True (default), for each output record there will be associated
a value for the "value" column (captured string) and
a value for the "type" column (capture type "digit", "word" , "text", "string", "raw", "regex");

if -oc is set to False, for each record there will be an associated value for both the "value" column
and the capture type column, i.e. for each record there will be both
the "digit", "word", " columns text", "string", "raw", "regex" and the "value" column;''')

    capture_group.add_argument(
        '-oc', '--one-column-capture',
        default=True,
        action='store',
        type=bool_parser,
        choices=[True, False],
        metavar=('SET'),
        help='''the captured strings are inserted into a single "value" column
regardless of their capture type (default True)''')

    capture_group.add_argument(
        '-vl', '--value',
        default=True,
        action='store',
        type=bool_parser,
        choices=[True, False],
        metavar=('SET'),
        help='''only strings with at least one alphabetical character are captured (default True)''')

    capture_group.add_argument(
        '-d', '--digit',
        default=False,
        action='store_true',
        help='''strings of only numbers are captured (default False)''')

    capture_group.add_argument(
        '-w', '--word',
        default=False,
        action='store_true',
        help='''only strings with a single word are captured (default also strings with spaces)''')

    capture_group.add_argument(
        '-t', '--text',
        default=False,
        action='store_true',
        help='''only strings with alphabetical characters and 0 or n spaces are captured (default False)''')

    capture_group.add_argument(
        '-s', '--string',
        default=False,
        action='store_true',
        help='''only strings with alphabetical characters (1 or n) and
numbers (1 or m) with 0 or k intermediate spaces are captured (default False)''')

    capture_group.add_argument(
        '-r', '--raw',
        default=False,
        action='store_true',
        help='''all strings are captured (default False)''')

    capture_group.add_argument(
        '-re', '--regex',
        nargs=1,
        default=[],
        metavar=('PATTERN'),
        help='''only strings matching the pattern are captured''')

    columns_group = parser.add_argument_group('columns', '''options for the output columns''')

    columns_group.add_argument(
        '-ic', '--include-column',
        nargs='+',
        default=[],
        metavar=('COLUMN'),
        help='''if set, only the indicated columns will be created in the output;
the "value" column is not affected by this parameter''')

    columns_group.add_argument(
        '-ex', '--exclude-column',
        nargs='+',
        default=[],
        metavar=('COLUMN'),
        help='''if set, the indicated columns will not be generated in the output;
the "value" column is affected by this parameter''')

    columns_group.add_argument(
        '-rn', '--rename',
        nargs='+',
        default=[],
        type=pair_parser('=', '%'),
        metavar=('PAIR'),
        help='''changes the column names;
the arguments passed must follow the following pattern: <COLUMN_NAME>=<NEW_COLUMN_NAME>;
pairs (name1,name2) are separated by spaces;
to use the equal character you need to escape `%%=`;
Examples:
-rn seq=SEQ "string = COL 2" value=COL%%=3
rename column `seq` to `SEQ`, `string` to `COL 2` and `value` to `COL=3`
-rn 'value=\"COL%%= 3\"'
rename the `value` column to `"COL= 3"`
''')

    columns_group.add_argument(
        '-ln', '--label-name',
        nargs='+',
        default=[],
        type=pair_parser('==', '%'),
        metavar=('PAIR'),
        help='''creates labels identifying files, sheets, columns,
callable in command line commands
to make the command line string more readable;
the arguments passed must follow the following pattern: <COLUMN_NAME>==<LABEL>;
to use the equal character you need to escape `%%==`;
Examples:
-ln file.xlsx==f1 "SHEET %%== 1 A == S1A" string==S value==V -ex V S seq
exclude the columns value, string and seq''')

    columns_group.add_argument(
        '-seq', '--sequence',
        default=1,
        type=int,
        choices=[0, 1, 2],
        metavar=('COLUMN'),
        help='''changes the depth level of the sequential number associated with the record;
-ic seq 0: adds the sequential number column at cell level (never resets)
-ic seq 1: adds the sequential number column at sheet level (resets with each sheet)
-ic seq 2: adds the sequential number column at file level (resets with each file)''')

    return parser.parse_args()
