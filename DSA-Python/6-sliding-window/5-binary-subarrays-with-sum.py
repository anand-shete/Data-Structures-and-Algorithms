# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# Constraints:     
# 1 <= nums.length <= 3 * 10⁴
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length



# brute force - O(n²), O(1)
def binary_subarrays_with_sum_1(nums: list[int], goal: int) -> int:
    total, n = 0, len(nums)
    
    for i in range(n):
        sum = 0
        
        for j in range(i, n):
            sum += nums[j]
            
            if sum == goal:
                total += 1
                
    return total

    
    
# prefix sum - O(n), O(n)
def binary_subarrays_with_sum_2(nums: list[int], goal: int) -> int:
    total, sum, n = 0, 0, len(nums)
    umap = {0:1}
    
    for i in range(n):
        sum += nums[i]
        
        if sum-goal in umap:
            total += umap[sum-goal]
            
        umap[sum] = umap.get(sum, 0) + 1
        
    return total
            
            

# sliding window - O(n), O(1)
def subarray_end_in_k(nums: list[int], k:int) -> int:
    if k < 0:
        return 0
    
    left, n, curr_sum = 0, len(nums), 0
    subarrays = 0
    
    for right in range(n):
        curr_sum += nums[right]
        
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
            
        subarrays += right-left+1
        
    return subarrays
        
    
def binary_subarrays_with_sum_3(nums: list[int], goal: int) -> int:
    # subarrays_ending_in2 - subarray_end_in_1 = subarrays_with_sum_2
    return subarray_end_in_k(nums, goal) - subarray_end_in_k(nums, goal-1)
    
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        goal = int(input())
        nums = list(map(int, input().split()))
        
        # res = binary_subarrays_with_sum_1(nums, goal)
        # res = binary_subarrays_with_sum_2(nums, goal)
        res = binary_subarrays_with_sum_3(nums, goal)
        
        print(res)
        
        
'''
5
2
1 0 1 0 1
0
0 0 0 0 0
1
1 0
0
0
5
1 1 1 0 1 0
'''