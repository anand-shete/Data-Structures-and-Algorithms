"""
Comprehensions are a concise, highly readable way to create new data structures from iterables in a single line of code.
"""


# list comprehensions
squares = [x*x for x in range(1,6)]
print('list comprehension:',squares)
evens = [x*2 for x in range(0,5)]
print('first 5 even numbers:',evens)
square_evens = [x*x for x in range(0,5) if x%2 == 0]
print('squares of even numbers:',square_evens)
print()


# dictionary comprehensions
names = ["anand", "sam", "bibhu"]
lens = {name:len(name) for name in names}
print("dict comprehension:",lens)
print()


# set comprehensions
l = [1,2,2,2,3,3,4,4,5]
uset = {x for x in l}
print("set:",uset)