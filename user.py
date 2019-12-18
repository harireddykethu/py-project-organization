import sys


# whenever a module is imported, it is searched in these locations
for line in sys.path:
    print(f'Path (original): {line}')

# as such, source module cannot be imported
# since it is not in the present directory

# import source # ModuleNotFoundError

# in order to import it, we can use either:

# from lib.general.source import PI     # looks elegant

# or
sys.path.append('./lib/general')    # offers more flexibility

for line in sys.path:
    print(f'Path (after append): {line}')


try:
    import source
    print(source.PI)
except ModuleNotFoundError as e:
    print(f'Error: {e}')
