def countdown(n:int):
    """
    Generators are a special type of function that allow you to create iterators in a clean, highly memory-efficient way.  
    `return` terminates a function and empties the stack memory  
    `yield` pauses function execution, yields value and freezes state in heap for next call
    """

    print("start countdown...")
    
    while n > 0:
        yield n
        n -= 1
        
    print("countdown over")
    
    

# generator object
counter = countdown(5)

for x in counter:
    print(x)
    
    

# generator expressions (zero memory bloat, on demand values)
gen = (x for x in range(1000))