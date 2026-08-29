# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Constraints:
# 1 <= nums.length <= 10⁴
# -10⁴ < nums[i], target < 10⁴
# All the integers in nums are unique.
# nums is sorted in ascending order



# linear search - O(n), O(1)



# recursive - O(log n), O(log n)
def binary_search_1(nums: list[int],low:int, high:int, target:int) -> int:
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_1(nums, mid+1, high, target)
    else:
        return binary_search_1(nums, low, mid-1, target)
    
    

# binary search - O(log n), O(1)
def binary_search_2(nums: list[int], target:int) -> int:
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
        
    

if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        target = int(input())
        nums = list(map(int, input().split()))
        
        # res = binary_search_1(nums, 0, len(nums)-1, target)
        res = binary_search_2(nums, target)
        
        print(res)
        
        
'''
3
9
-1 0 3 5 9 12
2
-1 0 3 5 9 12
4
-1 3 4 6 10 11
'''