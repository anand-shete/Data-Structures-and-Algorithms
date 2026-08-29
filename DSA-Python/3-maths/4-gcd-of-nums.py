# Given two integers n1 and n2, find their greatest common divisor


# sub-optimal - O(min(n1, n2)), O(1)
def gcd_of_nums_1(n1:int, n2:int) ->int:
    gcd = 1
    mini = min(n1,n2)
    
    for i in range(1, mini+1):
        if (n2 % i == 0 and n1 % i == 0):
            gcd = i
            
    return gcd



# euclidean - O(log(min(n1, n2))) O(1)
def gcd_of_nums_2(n1:int, n2:int) ->int:
    
    while n2:
        n1, n2 = n2, n1%n2
        
    return n1


if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        n1, n2 = map(int, input().split())
        
        # res = gcd_of_nums_1(n1, n2)
        
        res = gcd_of_nums_2(n1, n2)
        
        print(res)
    
    
'''
4
9 12
12 9
15 20
12 6
'''