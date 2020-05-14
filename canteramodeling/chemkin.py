#!/usr/bin/env python3

"""
A module for handling Chemkin input files
"""

from cantera import ck2cti


def convert_chemkin_file(input_file, thermo_file, output_file):
    parser = ck2cti.Parser()
    parser.convertMech(input_file, thermoFile=thermo_file, outName=output_file, quiet=True, permissive=True)
    print('Done')
