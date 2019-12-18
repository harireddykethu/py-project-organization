from constants import PI
from constants import cities as metro_cities
from factorial import factorial

print(f'π = {PI}')    # accessing variable declared in the module

factorial_7 = factorial(7)

print(f'7! = {factorial_7}')

for metro in metro_cities:
    print(f'Metro city: {metro}')
