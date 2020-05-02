import pprint

import cmakegenerators

generators = cmakegenerators.get_generators()

pprint.pprint([option for generator in generators for option in generator.options ])