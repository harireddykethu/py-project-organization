# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.
# Within a module, the module’s name(as a string) is available as
# the value of the global variable __name__.


from math import factorial
from math import pow


def get_factorial(n):
    return factorial(n)


def get_power(base, exponent):
    return pow(base, exponent)


def compare_case_agnostic(lhs, rhs):
    return lhs.lower() == rhs.lower()


PI = 3.14159265359

cities = ('Bengaluru', 'Mangaluru', 'Mumbai',
          'Chennai', 'Kolkata', 'Amritsar', 'Jaipur')


class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def drive(self):
        print(f'{self.name} is driving')
