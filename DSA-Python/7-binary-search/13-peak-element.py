# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

# Constraints:
# 1 <= nums.length <= 1000
# -2³¹ <= nums[i] <= 2³¹ - 1
# nums[i] != nums[i + 1] for all valid i.



# O(n), O(1)
def peak_element_1(nums: list[int]) -> int:
    n, peak = len(nums), 0
    
    for i in range(1, n-1):
        if nums[i-1] < nums[i] > nums[i+1]:
            peak = i
            
    if nums[n-1] > nums[n-2]:
        peak = n-1
            
    return peak



# binary search - O(log n), O(1)
def peak_element_2(nums: list[int]) -> int: 
    low, high = 0, len(nums)-1

    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] < nums[mid+1]:
            low = mid + 1
        else:
            high = mid
        
    return high
        
        

if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = peak_element_1(nums)
        # res = peak_element_2(nums)
        
        print(res)
        
        
'''
5
1 3 5 4 2
1
7 8 9 10
1 2 3 2 4 3 5 6 8 7 6 1
5 4 3 2 1
'''