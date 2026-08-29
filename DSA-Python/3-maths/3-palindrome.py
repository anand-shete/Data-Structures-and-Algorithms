# Given an integer x, return true if x is a palindrome, and false otherwise.



# string - O(log_10 x), O(log_10 x)
def check_palindrome_1(x:int) ->bool:
    rev = str(x)[::-1]
    
    return True if rev == str(x) else False


# optimal - O(log_10 x), O(1)
def check_palindrome_2(x:int) ->bool:
    rev = 0
    temp = x
    
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
        
    return True if rev == x else False
        
    
    
if __name__ == "__main__":
    n = int(input())
    
    for i in range(n):
        x = int(input())
        res = check_palindrome_1(x)
        
        res = check_palindrome_2(x)
        
        print(res)
        
        
    
    
'''
7
0
121
-121
-2147483648
2147483647
2147483645
123456789987654321
'''