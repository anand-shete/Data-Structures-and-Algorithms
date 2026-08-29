# Given an integer x, return true it is an Armstrong number otherwise return false
# Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
import math



# brute force - O(log_10 x), O(log_10 x)
def armstrong_1(x:int)->bool:
    if x < 0:
        return False
    
    string = str(x)
    arm = 0
    
    for c in string:
        arm += int(c) ** len(string)
        
    return True if arm == x else False


# optimal - O(log_10 x), O(1)
def armstrong_2(x:int) -> bool:
    temp = x
    arm = 0
    
    if x < 0:
        return False
    
    digits = math.floor(math.log10(x)) + 1 if x > 0 else 1
    
    while temp > 0:
        arm += (temp % 10) ** digits
        temp //= 10
    
    return True if arm == x else False
    
    
    
if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        x = int(input())
        
        res = armstrong_1(x)
        
        # res = armstrong_2(x)
        
        print(res)
        
        
        
'''
6
1253
153
371
0
1634
-1634
'''