import sys
import keyword

print('python version: ', sys.version)
print('keywords in current version: ', keyword.kwlist) 
print()



# Everything is object in python
print("type of 4:",type(4).__name__)
print()



# Booleans are integers in python
print("True + True:",True + True)
print("False - 5:",False - 5)
print()



# Integers and floating point are same if they are numerically equal
print("1 == 1.0:",1 == 1.0)
print()



# variable is a name that points to a value stored in your computer's memory
x = "hello"
PI = 3.142
print('x is variable with value:', x)
print('hello is a literal')
print('value of constant PI:', PI)
print()



# Memory address
test = 123
print('memory location of object:',id(test))