#! /usr/bin/python
# -*- coding: future_fstrings -*-
"""
Generator classes and functions
"""

from abc import ABC, abstractmethod, abstractproperty
import logging
import re
import subprocess
import sys
import typing
from typing import List

LOGGER = logging.getLogger(__name__)

class GeneratorTypeNotFoundError(Exception):

    pass

class AbstractGenerator(ABC):
    """
    Generator base class, inherit from this and override the abstract methods
    """

    @abstractproperty
    def available(self) -> bool:
        """
        Return true if we can find it in the current environment, otherwise false
        """

        raise NotImplementedError()

class BaseGenerator(AbstractGenerator):
    """
    Base class for generators
    """

    def __init__(self, name: str, description: str):

        self.name = name
        self.description = description

class OptionalParam():
    """
    Defines an optional parameter that can be passed into a generator
    """

    PATTERN = r'\[(?P<name>\w+)\]'
    REGEX = re.compile(PATTERN)

    def __init__(self, name:str, parent: BaseGenerator):

        self.name = name
        self.parent = parent

        values_pattern = r'Optional \[' + self.name + r'\] can be ([\d\w\s]|")*\.'
        values_regex = re.compile(values_pattern)

        value_pattern = r'"(?P<value>[\w\d]+)"'
        value_regex = re.compile(value_pattern)

        self.values = [match.group("value") for match in 
                       value_regex.finditer(values_regex.search(self.parent.description).string)]

        self.values.append("")

class Generator(BaseGenerator):
    """
    Generic generator
    """

    def __init__(self, name: str, description: str):

        super().__init__(name, description)

        self.optional_params =  [OptionalParam(match.group("name"), self) for 
                                 match in OptionalParam.REGEX.finditer(self.name)]

class IDEGenerator(Generator):
    """
    A generator that relies on an IDE to perform build setup
    """

    @property
    def available(self) -> bool:
        """
        Find whether the IDE tool exists in the environment
        """

        if sys.platform == "win32" and self.name.startswith("Visual Studio"):

            return True

        elif sys.platform == "darwin" and self.name.startswith("Xcode"):

            return True

        else:

            return False

class ShellGenerator(Generator):
    """
    A generator that must run in a terminal or shell environment
    """

    @property
    def available(self) -> bool:
        """
        Return true if the generator exists in the current environment
        """

        # Not sure how to handle this currently

        if sys.platform == "win32":

            find_process = subprocess.run(["where", self.name], 
                                          capture_output=True)

            return (find_process.returncode == 0 and
                    len(find_process.stdout) > 0)

        elif sys.platform == "linux":

            find_process = subprocess.run(["which", self.name], 
                                          capture_output=True)

            return (find_process.returncode == 0 and
                    len(find_process.stdout) > 0)

class ExtraGenerator(Generator):
    """
    Auxiliary tool generators/ variant generator
    """

    @property
    def available(self):
        """
        Search for the presence of such a generator
        """

        # Not sure how to handle this currently

        return False

def get_generator(name: str, description: str) -> Generator:
    """
    Find the correct type of generator given the name
    """

    shell_generator_prefixes = ["Borland Makefiles", "MSYS Makefiles", 
                                "MinGW Makefiles", "NMake Makefiles", 
                                "NMake Makefiles JOM", "Ninja", 
                                "Unix Makefiles", "Watcom WMake"]

    ide_generator_prefixes = ["Green Hills MULTI", "Visual Studio", "Xcode"]

    extra_generator_prefixes = ["CodeBlocks", "CodeLite", "Eclipse CDT4", 
                                "KDevelop3", "Kate", "Sublime Text 2"]

    if any([name.startswith(prefix) for prefix in shell_generator_prefixes]):

        return ShellGenerator(name, description)

    elif any([name.startswith(prefix) for prefix in ide_generator_prefixes]):

        return IDEGenerator(name, description)

    elif any([name.startswith(prefix) for prefix in extra_generator_prefixes]):

        return ExtraGenerator(name, description)

    else:

        raise GeneratorTypeNotFoundError()
