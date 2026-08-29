# Python automatically infers the type based on the value we assign.
# Python evaluates RHS expression before allocating memory.


# Basic data types
a = 34
b = 66.67
c = 'hello world'
d = False

print(a, "=>", type(a).__name__)
print(b, "=>", type(b).__name__)
print(c, "=>", type(c).__name__)
print(d, "=>", type(d).__name__)
print()



# Immutable data types: int, float, bool, str, tuple, frozenset, bytes
# Mutable data types: list, dict, set, bytearray



# Typecasting
a = 5
b = 2.5
c = a + b
print(c,"implicit convertion to",type(c).__name__)

a = "10"
b = int(b)
print(b, "explicit conversion to", type(b).__name__)
print()



# Local and Global scope
# Only Functions and Classes create local scope
def func():
    x = 34
    print(f"inside local scope {x}")
# print(f'outside local scope {x}')
func()

y = 90
def func2():
    global y
    y = 45
    print(f'update global variable to {y} locally')
func2()
print(f'global value of y {y}')
