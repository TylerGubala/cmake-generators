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

def get_generators() -> List[generators.Generator]:
    """
    Get the list of generators available according to cmake
    """

    results = []

    generators_list = cmake_help().split("The following generators are "
                                         "available on this platform:")[-1]

    generator_half_text = generators_list.split("=")

    for i in range(len(generator_half_text)-1):

        generator_name = generator_half_text[i].split(".")[-1]

        generator_description = " ".join([e.strip() + "." for e in generator_half_text[i+1].split(".") if e][0:-1])

        results.append(generators.get_generator(generator_name.strip(), 
                                                generator_description.strip()))

    return results

if __name__ == "__main__":

    [print(generator.name) for generator in get_generators()]
