# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.

# Constraints:
# 1 <= nums.length <= 5000
# -10⁴ <= nums[i] <= 10⁴
# nums is guaranteed to be rotated at some pivot.
# -10⁴ <= target <= 10⁴



# brute force - O(n), O(1)


# binary search - O(n), O(1)
def search_rotated_sorted_array(nums: list[int], target:int) -> bool:
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return True
        elif nums[low] == nums[mid] and nums[mid] == nums[high]:
            low += 1
            high -=1
        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1 
            else:
                high = mid - 1
    
    
    return False
    
    
    
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        target = int(input())
        nums = list(map(int, input().split()))
        
        res = search_rotated_sorted_array(nums, target)
        
        print(res)
    
'''
7
0
5 6 6 7 0 1 2 4 4 4
7
5 6 6 7 0 1 2 4 4 4
2
2 2 2 2 2 2
0
1 1 1 0 1
0
1 0 1 1 1
3
2 5 6 0 0 1 2
1
1 1 1 1 1 1 1
'''