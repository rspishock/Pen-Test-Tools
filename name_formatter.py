#! /usr/python3

import argparse
import os
import re

def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--first', dest='first_name', help='Enter target\'s first name.')
    parser.add_argument('-l', '--last', dest='last_name', help='Enter target\'s last name.')
    parser.add_argument('-t', '--file', dest='file_name', help='Enter file to parse.')
    (options) = parser.parse_args()

    return options

options = get_arguments()
first_name = options.first_name
last_name = options.last_name
file = options.file_name

if file:
    if os.exists(file) as file_object:
        while open():
            for line in file_object:

    else:
        print(f'File {file} does not exist.')
        exit            # exits gracefully if file does not exist
