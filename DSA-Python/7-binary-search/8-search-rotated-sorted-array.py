# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Constraints:
# 1 <= nums.length <= 5000
# -10⁴ <= nums[i] <= 10⁴
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10⁴ <= target <= 10⁴



# brute force - O(n), O(1)


# binary search - O(log n), O(1)
def rotated_sorted_array(nums: list[int], target: int) -> int:
    low, high = 0, len(nums)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
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
                
    return -1




if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        target = int(input())
        nums = list(map(int, input().split()))
        
        res = rotated_sorted_array(nums, target)
        
        print(res)
        
        
'''
5
0
4 5 6 7 0 1 2
3
4 5 6 7 0 1 2
0
0
2
5 6 7 0 1 2 3 4
4
5 6 7 0 1 2 3 4
'''