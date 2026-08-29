# Given an integer n, return all divisors of n


# brute force - O(n), O(1)
def divisors_1(n:int) -> list:
    divs = []
    
    for i in range(1, n+1):
        if (n % i == 0):
            divs.append(i)
            
    return divs


# optimal - O(rt(n)), O(1)
def divisors_2(n:int) -> list:
    divs = []
    
    i=1
    while i*i <= n:
        if n % i == 0:
            divs.append(i)
            
            if i != n//i:
                divs.append(n//i)
                
        i+= 1
    
    return divs
    
    
if __name__=="__main__":
    n = int(input())
    
    for _ in range(n):
        n = int(input())
        
        res = divisors_1(n)
        # res = divisors_2(n)
        
        print(sorted(res))
        
'''
5
36
12
0
13
14
'''