# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.



# brute force - O(n²), O(1)
def single_number_1(nums:list[int]) -> int:
    n = len(nums)
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if nums[i] == nums[j]:
                cnt += 1
                
        if cnt < 2:
            return nums[i]
        
    return -1



# hashing - O(n), O(n)
def single_number_2(nums: list[int]) -> int:
    umap = {}
    
    for x in nums:
        umap[x] = umap.get(x, 0) + 1
        
    for (k,v) in umap.items():
        if v < 2:
            return k
    
    return 1
    
    

# xor approach - O(n), O(1)
def single_number_3(nums: list[int]) -> int:
    xor = 0
    
    for x in nums:
        xor ^= x
        
    return xor



if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split(' ')))
        
        res = single_number_1(nums)
        
        res = single_number_2(nums)
        
        res = single_number_3(nums)
        
        print(res)