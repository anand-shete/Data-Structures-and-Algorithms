# Since functions are first class objects, we can pass function as pointer or argument to another function, use nested functions, return pointers from inner functions, etc.


def my_decorator(func):
    """
    Decorator is a **design pattern** that allows you to modify or extend the behavior of a function or method without changing its actual source code.
    """
    
    def wrapper():
        print("1. something printed before function runs")
        func()
        print("2. something printed after function runs")
        
    return wrapper


# apply a decorator
@my_decorator
def say_hello():
    print("Hello, world")
    
say_hello()
print()



def uppercase_decorator(func):
    """
    Wrapper function can also accept (args and kwargs): :doc: `./03-operators.py`
    """
    
    def wrapper(*args, **kwargs):
        print("Processing...")
        print("args:",*args)
        print("kwargs:",kwargs)
        
        result = func(*args, **kwargs)
        
        return result.upper()
    
    return wrapper

@uppercase_decorator
def greet(name, isMale,place):
    return f'Good morning, {name}'

print(greet("Rohit", isMale=True, place="nerul"))



# A decorator function can have multiple wrappers, but it must only return one