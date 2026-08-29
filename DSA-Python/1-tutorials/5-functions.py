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




# Variable-Length Arguments
# Python allows functions to accept variable number of arguments using special syntax:
# *args: Combines all values into a single tuple (read-only array)
def add_all(*arg):
    curr_sum = 0
    for x in arg:
        curr_sum += x
    return curr_sum

res = add_all(1, 2, 3, 4)
print("current sum: ", res)



# **kwargs: Combines all values into a dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
print()



# Immutable types are pass-by-value
# int, float, bool, str, tuple, frozenset, bytes
num = 5
def modify_num(x:int):
    x = 100
print(num)



# Mutable types are pass-by-reference
# list, dict, set, bytearray
# If mutable values are re-assigned inside function, its pass-by-value
nums = [1,2,3,4]
def change_list(list:list):
    list.append(5)
print(nums)



# A lambda function is an anonymous (unnamed) function that only contain a single expression
square = lambda x: x**2
print(square(4))
print("")



# Higher order function 
# 1. They take another function as argument
double = map(lambda x:x*2, nums)
print(nums)



# 2. Or return another function. Function which return a function called closures
def multiply(factor: int):
    def mul(num:int):
        return num * factor
    return mul
func = multiply(5)
print(func(3))
print()