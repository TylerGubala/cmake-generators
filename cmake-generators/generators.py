#! /usr/bin/python
# -*- coding: future_fstrings -*-
"""
Generator classes and functions
"""

from abc import ABC, abstractmethod
import logging
import sys
import typing

LOGGER = logging.getLogger(__name__)

# Platform specific imports
try:
    import winreg
except ImportError:
    LOGGER.info("Could not import winreg")

class Generator(ABC):
    """
    Generator base class, inherit from this and override the abstract methods
    """

    @abstractmethod
    def available(self) -> bool:
        """
        Return true if we can find it in the current environment, otherwise false
        """

        raise NotImplementedError()

class IDEGenerator(Generator):
    """
    A generator that relies on an IDE, like Visual Studio to perform build setup
    """

    def __init__(self, name:str):

        if name is None:

            raise ValueError("Name cannot be None")

        self.name = name

    def available(self) -> bool:
        """
        Find whether the IDE tool exists in the environment
        """

        if sys.platform == "win32":

            pass

        elif sys.platform == "darwin":

            pass

        else:

            return False
