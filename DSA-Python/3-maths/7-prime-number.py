# Given an integer n, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself.
import math


# brute force - O(n)
def check_prime_1(n:int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


# optimal - O(rt(n)), O(1)
def check_prime_2(n:int) -> bool:
    if n < 2:
        return False
    
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    
    return True
    
    
    
if __name__ == "__main__":
    loops = int(input())
    
    for _ in range(loops):
        n = int(input())
        
        res = check_prime_1(n)
        res = check_prime_2(n)
        
        print(res)
        
        
        
'''
6
2
13
91
13
0
-34
'''