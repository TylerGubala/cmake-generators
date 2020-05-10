import pprint

import struct

import cmakegenerators

BITNESS = struct.calcsize("P") * 8

generators = cmakegenerators.get_generators()

filtered_generators = [generator for generator in generators if 
                                "Visual Studio".casefold() in 
                                generator.name.casefold()]

if len(filtered_generators) > 0:

    generator_option : str = None

    if BITNESS == 64:

        filtered_generator_options = [option for generator in filtered_generators for option in generator.options if "64".casefold() in option.casefold()]

        if len(filtered_generator_options) > 0:

            pprint.pprint(filtered_generator_options[0])

        else:

            pprint.pprint([option for option in filtered_generators[0].options])