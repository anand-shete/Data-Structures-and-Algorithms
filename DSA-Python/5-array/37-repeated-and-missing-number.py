# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
# Note: You are not allowed to modify the original array.




# brute force - O(n²), O(1)
def repeated_and_missing_number_1(nums:list[int]) -> tuple[int]:
    n = len(nums)
    repeated, missing = nums[0], nums[0]
    
    for i in range(1, n+1):
        cnt = nums.count(i)

        if cnt == 0:
            missing = i
        if cnt > 1:
            repeated = i
            
    return repeated, missing


    
    
# hashing - O(n), O(n)
def repeated_and_missing_number_2(nums:list[int]) -> tuple[int]:
    repeated, missing = nums[0],nums[0]
    n = len(nums)
    umap = {}
    uset = set()
    
    for x in nums:
        umap[x] = umap.get(x, 0) + 1
        uset.add(x)        
        
    for k,v in umap.items():
        if v > 1:
            repeated = k
            
    for i in range(1, n+1):
        if i not in uset:
            missing = i
            
    return (repeated, missing)
    
    
    
    
# optimal - O(n), O(1)
def repeated_and_missing_number_3(nums: list[int]) -> tuple[int]:
    n = len(nums)
    
    sum_n = n * (n+1) // 2
    sum_nsq = n * (n+1) * (2*n+1) // 6
    
    sum_nums = sum(nums)
    sum_nums_sq = sum(x*x for x in nums)
    
    # r - m
    diff_val = sum_nums - sum_n
    print('diff',diff_val)
    
    # r² - m²
    diff_sq = sum_nums_sq - sum_nsq
    
    # r + m = r² - m² // r - m
    sum_val = diff_sq // diff_val
    print('sum',sum_val)
    
    repeated = (sum_val + diff_val) // 2
    missing = repeated - diff_val
    
    return repeated, missing



if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = repeated_and_missing_number_1(nums)
        # res = repeated_and_missing_number_2(nums)
        res = repeated_and_missing_number_3(nums)
        
        print(*res)
    
    
'''
4
3 5 4 1 1
1 2 3 6 7 5 7
1 1
3 1 3
'''