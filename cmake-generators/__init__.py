#! /usr/bin/python
# -*- coding: future_fstrings -*-
"""
Exposes cmake generator information to Python
"""

import re
import subprocess
import sys
import typing
from typing import List

import generators

GENERATOR_PATTERN = r'(?P<Name>[\w\s:\[\]\-]*)=(?P<Description>[\w\s\.]*\.)'
GENERATOR_REGEX = re.compile(GENERATOR_PATTERN)

def cmake_help() -> str:
    """
    Get the cmake help string
    """

    output_bytes = bytes(subprocess.run(["cmake", "--help"], 
                         capture_output=True).stdout)

    return output_bytes.decode(sys.stdout.encoding)

def get_generators() -> List[str]:
    """
    Get the list of generators available according to cmake
    """

    generators_list = cmake_help().split("The following generators are "
                                         "available on this platform:")[-1]

    for substring in generators_list.split("="):

        for line in substring.splitlines():

            pass

    return [generator_name.string for generator_name in 
            GENERATOR_REGEX.finditer(generators_list)]

if __name__ == "__main__":

    for generator_name in get_generators():

        print(generator_name)
