# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# brute force - O(log_10 x), O(log_10 x)
def reverse_number_1(x:int) -> int:
    res = 0
    string = str(x)
    
    if x < 0:
        res = -1 * int(string[:0:-1])
    else:
        res = int(str(x)[::-1])
        
    
    return 0 if res < -2**31 or res > 2**31 -1 else res
        
        
# optimal - O(log_10 x), O(1)
def reverse_number_2(x:int) -> int:
    temp = abs(x)
    res = 0
    
    while temp > 0:
        res = res * 10 + temp % 10
        temp //= 10
    
    if x < 0:
        res = res * -1
        
    return 0 if res < -2**31 or res > 2**31 - 1 else res


if __name__ == "__main__":
    n = int(input())
    
    for i in range(n):
        x = int(input())
        
        res = reverse_number_1(x)
        
        # res = reverse_number_2(x)

        print(res)
'''
88
123
-123
12000
0
2147483645
2147483647
-2147483648
1563847412
-1563847412
'''