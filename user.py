# https://docs.python.org/3/library/functions.html#dir

import lib.general.source as source_module

print('Names in the source module:')

for name in dir(source_module):
    print(name)

print('---------------------------------------')

print('Names in the current (user) module:')

for name in dir():
    print(name)
    # source_module is also a name in the current module
    # also, 'name' variable introduced by this iterator block
    # is also a name
