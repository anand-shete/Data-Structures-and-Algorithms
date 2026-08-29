# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Constraints:
# 1 <= nums.length <= 200
# -10⁹ <= nums[i] <= 10⁹
# -10⁹ <= target <= 10⁹




# brute force - 
def four_sum_1(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    uset = set()
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i]+nums[j]+nums[k]+nums[l] == target:
                        quadruplet = tuple(sorted((nums[i], nums[j], nums[k], nums[l])))
                        uset.add(quadruplet)
                    
    return [list(quad) for quad in uset]
    
    
    

# suboptimal solution - O(n³), O(n)
def four_sum_2(nums: list[int], target:int) -> list[list[int]]:
    n = len(nums)
    uset = set()
    
    for i in range(n):
        for j in range(i+1, n):
            temp = set()
            
            for k in range(j+1, n):
                fourth = target - nums[i] - nums[j] - nums[k]
                
                if fourth in temp:
                    quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                    uset.add(quad)
                    
                temp.add(nums[k])
                
    return [list(quad) for quad in uset]

    
    
    
# optimal - O(n³), O(1)
def four_sum_3(nums: list[int], target:int) -> list[list[int]]:
    n = len(nums)
    res = []
    
    nums.sort()
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
        
            left, right = j+1, n-1
            
            while left < right:
                sumed = nums[i] + nums[j] + nums[left] + nums[right]
                
                if sumed == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
                elif sumed < target:
                    left += 1
                    
                else:
                    right -= 1
                    
    return res
    
    

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        target = int(input())
        nums = list(map(int, input().split()))
        
        # ans = four_sum_1(nums, target)
        # ans = four_sum_2(nums, target)
        ans = four_sum_3(nums, target)
        
        print(ans)
        print()