# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order
# Constraints:
# 2 <= nums.length <= 10⁴
# -10⁹ <= nums[i] <= 10⁹
# -10⁹ <= target <= 10⁹



# brute force - O(n²), O(1)
def two_sum_1(nums:list[int], target:int) -> tuple:
    n = len(nums)
    
    for i in range(n):
        comp = target - nums[i]
        
        for j in range(i+1, n):
            if nums[j] == comp:
                return (i, j)

    return ()



# hashing - O(n), O(n)
def two_sum_2(nums: list[int], target:int) -> tuple:
    n = len(nums)
    umap = {}
    
    for i in range(n):
        comp = target - nums[i]
        
        if comp in umap:
            return (i, umap[comp])
    
        umap[nums[i]] = i
        
    return ()



    
if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        target = int(input())
        nums = list(map(int, input().split()))
        
        res = two_sum_1(nums, target)
        
        res = two_sum_2(nums, target)
        
        print(res)
        
        
    # print(two_sum_2(list(range(100000)), 199997))
        


'''
4
9
2 7 11 15
9
7 2 11 15
6
3 2 4
6
3 3
'''