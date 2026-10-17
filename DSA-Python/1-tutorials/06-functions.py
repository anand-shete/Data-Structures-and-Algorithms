# Functions are first class objects in python

# define function
def avg(a, b, c):
    return (a + b + c) / 3



# call function
avg_nums = avg(1, 5, 7)
print("Average is", avg_nums)
print()



# default parameters
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
print(greet("Bob"))
print("")



# Variable length arguments
def add_all(required_arg, *args, **kwargs):
    """
    Python allows functions to accept variable number of arguments:  
    `*args` collects positional arguments and packs into a **tuple**  
    `**kwargs` collects named arguments (`key=value`) and packs into **dictionary**  
    
    When used together, you must follow the same order: `required_args`, `*args`, `**kwargs`  
    Actual magic is `*` and `**` not the arguemnt names
    """
    
    print("positional arguments:",args)
    print("named arguments:",kwargs)

add_all(1, 2, 3, 4, name="Mohit", age=34, is_disabled=False)
print()



# int, float, bool, str, tuple, frozenset, bytes
num = 5
def modify_num(x:int):
    """
    Immutable types are always passed by value (copied)
    """
    x = 100
    
print("immutable data structure outside function:",num)
print()



nums = [1,2,3]
def change_list():
    """
    Mutable types (`list`, `dict`, `set` and `bytearray`) are passed by reference  
    If mutable values are re-assigned inside function, it overrides local reference
    """
    nums = [10, 20, 30]
    print("local reference:", nums)
    
change_list()
print("mutable data strcuture outside function:",nums)
print()



"""
A lambda function (anonymous function) can contain a single expression
lamda param: return expression
"""
square = lambda x: x**2
print("lamda function:",square(4))
print()



def outer(factor: int):
    """
    Higher order function can:
    1. take another function as an argument or
    2. return another function. 

    A higher order function is called a closure if inner function remembers references variables from outer function
    """
    
    def inner(num:int):
        return num * factor
    return inner

f = outer(5)
print("inner function is a closure:",f.__closure__)
print("value inside heap:",f.__closure__[0].cell_contents)
print("use value stored in heap:",f(3))