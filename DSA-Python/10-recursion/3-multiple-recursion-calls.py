# fibonacci series - O(2^N) , O(N)
def fibonacci(n:int) -> int:
    if n < 2:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)


# result = fibonacci(0)
# print(result)