# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.


# Constraints:
# 1 <= nums.length <= 10⁵
# 0 <= nums[i] <= 10⁵


# brute force - O(n²), O(1)
# hashing - O(n), O(n)
from collections import Counter
def single_element_in_sorted_array_1(nums: list[int]) -> int:
    n = len(nums)
    
    count = Counter(nums)
    
    for k,v in count.items():
        if v < 2:
            return k
        
    return -1



# xored - O(n), O(1)
def single_element_in_sorted_array_2(nums: list[int]) -> int:
    n, xor = len(nums), 0
    
    for x in nums:
        xor ^= x
        
    return xor
    
    
    
# binary search - O(log n), O(1)
def single_element_in_sorted_array_3(nums: list[int]) -> int:
    n = len(nums)
    low, high = 1, n - 2
    
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    
    while low <= high:
        mid = (low + high) // 2
        
        if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
            low = mid + 1
        else:
            high = mid - 1
            
    return nums[low]
    
    
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = single_element_in_sorted_array_1(nums)
        # res = single_element_in_sorted_array_2(nums)
        res = single_element_in_sorted_array_3(nums)
        
        print(res)