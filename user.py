from constants import PI
from constants import cities as metro_cities    # aliasing
from factorial import factorial

# We execute the user.py module
# That means, the __name__ of this module will be __main__

if __name__ == '__main__':
    print('Executing user.py')

# However, this above block would not run if the user.py is imported

print(f'π = {PI}')    # accessing variable declared in the module

factorial_7 = factorial(7)

print(f'7! = {factorial_7}')

for metro in metro_cities:
    print(f'Metro city: {metro}')
