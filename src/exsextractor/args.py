"""Args for exsextractor."""

from .utils import nargs_range
from . import __version__
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='Excel String Extractor CLI (exsextractor)',
        description='''exsextractor is a Python script that scans Excel and CSV files,
extracting all strings from every cell and consolidating them into one or more output files.''',
        epilog='''.
.
.
. . . . Copyright (c) 2024 Giuseppe Ferri <jfinfoit@gmail.com> ''',
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



    return parser.parse_args()
