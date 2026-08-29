# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Constraints:
# 3 <= nums.length <= 3000
# -10⁵ <= nums[i] <= 10⁵




# brute force - O(n³), O(1)
def three_sum_1(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res = []
    uset = set()
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    uset.add(triplet)
                        
    return [list(trip) for trip in uset]




# optimal brute force - O(n²), O(n-1)
def three_sum_2(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res = set()
    
    for i in range(n):
        uset = set()
        
        for j in range(i+1, n):
            third = -(nums[i] + nums[j])
            
            if third in uset:
                res.add(tuple(sorted([nums[i], nums[j], third])))
                
            uset.add(nums[j])
    
    return [list(triplet) for triplet in res]
    
    
    

# optimal - O(n²), O(1)
def three_sum_3(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res = []
    
    nums.sort()
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i+1, n-1
        
        while left < right:
            target = nums[i] + nums[left] + nums[right]
            if target == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
                    
            elif target < 0:
                left += 1
                
            else:
                right -= 1
            
    return res




if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = three_sum_1(nums)
        # res = three_sum_2(nums)
        res = three_sum_3(nums)
        
        print(res)
        print()
        
        
'''
4
-1 0 1 2 -1 -4
0 1 1
0 0 0
-2 0 0 0 2
'''