from source import *

# This imports all names except those beginning with an
# underscore (_). In most cases Python programmers
# do not use this facility since it introduces an unknown
# set of names into the interpreter, possibly hiding
# some things you have already defined.

# all things defined in the source except for _
# (considered private) are imported and used directly
# without qualifying

print(PI)

print(factorial(8))

print(compare_case_agnostic('raman', 'RamaN'))

# print(_counter)  # NameError: name '_counter' is not defined
