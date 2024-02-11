"""Args for exsextractor."""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='Excel String Extractor CLI (exsextractor)',
        description='''exsextractor is a Python script that scans Excel and CSV files,
            extracting all strings from every cell and consolidating them into one or more output files.''',
        epilog='''Copyright (c) 2024 Giuseppe Ferri <jfinfoit@gmail.com> ''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-u', '--unique',
        default=False,
        action='store_true',
        help='the output will only contain unique strings')
    return parser.parse_args()
