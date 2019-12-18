import source  # importing from the same directory

print(source.__name__)  # name of the imported module

print(source.PI)    # accessing variable declared in the module

factorial_7 = source.factorial(7)

print(factorial_7)
