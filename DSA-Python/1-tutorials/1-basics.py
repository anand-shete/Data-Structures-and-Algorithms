import sys
import keyword

print('python version: ', sys.version)
print('keywords of current version: ', keyword.kwlist) 
print()


# Everything is object in python
print(type(4).__name__)
print()


# Booleans are integers in python True(1) and False(0)
print(True + True)
print(False - 5)



# Integers and floating point are same if they are numerically equal
print(1 == 1.0)
print()


# Memory address
test = 123
print('memory location of object',id(test))