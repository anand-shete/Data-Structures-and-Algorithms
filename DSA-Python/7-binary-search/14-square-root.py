# You are given a positive integer n. Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).


# brute force - O(rt(n)), O(1)
def square_root_1(x:int) -> int:
    ans = 0
    
    if x == 1:
        return 1
    
    for i in range(x//2 + 1):
        if i**2 > x:
            break
        ans = i
    
    return ans



# binary search - O(log n), O(1)
def square_root_2(x: int) -> int:
    left, right = 0, x
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid ** 2 <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans
    
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        num = int(input())
        
        # res = square_root_1(num)
        res = square_root_2(num)
        
        print(res)
        
        
'''
5
36
28
14
4
1
'''