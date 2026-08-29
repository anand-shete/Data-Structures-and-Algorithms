# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



# brute force - O(n²), O(1)
def majority_element_1(nums: list[int]) -> int:
    n, major, max_cnt = len(nums), 0, 0
    
    for i in range(n):
        cnt = 0
        
        for j in range(i, n):
            if nums[i] == nums[j]:
                cnt += 1
                
        if cnt > max_cnt:
            max_cnt = cnt
            major = nums[i]
            
    return major if max_cnt > n//2 else -1



# hashing - O(n), O(n)
def majority_element_2(nums:list[int]) -> int:
    n, major = len(nums), 0
    
    umap = {}
    
    for x in nums:
        umap[x] = umap.get(x, 0) + 1
        
    for (k,v) in umap.items():
        if v > n//2:
            return k
        
    return -1



# booyer moores voting algorithm - O(n), O(1)
def majority_element_3(nums:list[int]) -> int:
    n, cnt, major = len(nums), 0, 0
    
    for i in range(n):
        if cnt == 0:
            major = nums[i]
            cnt = 1
        elif major == nums[i]:
            cnt += 1
        else:
            cnt -= 1
            
    cnt = nums.count(major)
    
    return major if cnt > n//2 else -1
        
        
    

if __name__ == "__main__":
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split(' ')))
        
        res = majority_element_1(nums)
        
        res = majority_element_2(nums)
        
        res = majority_element_3(nums)
        
        print(res)
        
        
        
'''
5
2 1 2 3 2
7
1 2 3 4 4 4 4
-1 -1 -1 2 3
1 2 1 2 1 2 2
'''