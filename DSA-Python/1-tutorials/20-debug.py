
def calculate_tax(price:int):
    """
    `assert` crashes the program if condition is not passed
    """

    assert price >= 0, "Price cannot be negative"
    
    return price * 0.18


# calculate_tax(-34)


def complex_func(x, y):
    """
    When Python hits `breakpoint()`, it pauses execution, retains the entire stack frame state perfectly on the heap, and opens an interactive prompt in your terminal. You can use these essential commands:
    
    - `n` (next): Executes the current line and steps over to the next line.  
    - `s` (step): Steps into a function call on the current line.  
    - `c` (continue): Resumes normal execution until the next breakpoint is hit or the program finishes.  
    - `p variable_name` (print): Evaluates and prints the value of a variable on the heap.  
    - `q` (quit): Instantly aborts the program.
    """
    
    ans = x + y
    
    breakpoint()
    
    ans = ans * 2
    return ans


complex_func(3,4)