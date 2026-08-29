# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



# brute force - O(n²), O(1)
def find_missing_number_1(nums:list) -> int:
    n = len(nums)
    j = 1
    
    for cnt in range(n+1):
        present = False
        
        for num in nums:
            if num == cnt:
                present = True
                break
            
        if not present:
            return cnt
        
    return -1



# hashing - O(n), O(n)
def find_missing_number_2(nums:list) -> int:
    n = len(nums)
    uset = set()
    
    for x in nums:
        uset.add(x)
        
    for i in range(n+1):
        if i not in uset:
            return i
        
    return -1



# sum difference - O(n), O(1)
def find_missing_number_3(nums:list) -> int:
    n = len(nums)
    
    return ((n * (n+1)) // 2) - sum(nums)

    

if __name__=="__main__":
    loop = int(input())
    
    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        res = find_missing_number_1(nums)
        
        res = find_missing_number_2(nums)
        
        res = find_missing_number_3(nums)
        
        print(res)
        
        
'''
5
0 1
9 6 4 2 3 5 7 0 1
1

3 0 1
'''