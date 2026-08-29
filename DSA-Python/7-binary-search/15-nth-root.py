# Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.



# brute force - O(m), O(1)
def nth_root_of_m_1(m:int, n:int) -> int:
    ans = 0
    
    for i in range(m+1):
        if i**n == m:
            return i
        
        if i**n > m:
            break
        
    return -1



# binary search - O(n.logm), O(1)
def nth_root_of_m_2(m:int, n:int) -> int:
    low, high = 0, m // 2 + 1
    
    if n == 1:
        return m
    
    if m == 1:
        return 1
    
    while low <= high:
        mid = (low + high) // 2
        
        ans = 1
        for _ in range(n):
            ans *= mid
            if ans > m:
                break
            
        if ans == m:
            return mid
        
        if ans > m:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

    


if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        n, m = list(map(int, input().split()))
        
        # res = nth_root_of_m_1(m, n)
        res = nth_root_of_m_2(m, n)
        
        print(res)
        
        

'''
5
3 27
4 69
5 32
2 1
3 216
'''