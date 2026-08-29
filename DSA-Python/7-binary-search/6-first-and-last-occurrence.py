# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Constraints:
# 0 <= nums.length <= 10⁵
# -10⁹ <= nums[i] <= 10⁹
# nums is a non-decreasing array.
# -10⁹ <= target <= 10⁹




# brute force - O(n), O(1)


# binary search - O(log n), O(1)
def first_and_last_occurrence(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    first, last = -1, -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] < target:
            low = mid + 1
        else:
            first = mid
            high = mid - 1
          
          
    low, high = 0, len(nums)-1  
    
    while low <=high:
        mid = (low + high) // 2
        
        if nums[mid] <= target:
            last = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return first, last



if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        target = int(input())
        nums = list(map(int, input().split()))
        
        res = first_and_last_occurrence(nums, target)
        
        print(res)
        
        
'''
2
13
3 4 13 13 13 20 40
60
3 4 13 13 13 20 40
'''