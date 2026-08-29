# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.



# brute force - O(n), O(1)
def find_min_in_rotated_sorted_array_1(nums: list[int]) -> int:
    return min(nums)



# binary search - O(log n), O(1)
def find_min_in_rotated_sorted_array_2(nums: list[int]) -> int:
    low, high = 0, len(nums)-1
    
    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
            
    return nums[low]
            
            
            
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = find_min_in_rotated_sorted_array_1(nums)
        res = find_min_in_rotated_sorted_array_2(nums)
        
        print(res)
        
        

'''
5
4 5 6 7 0 1 2
4 5 6 7 0 1 2 -1
-2
5 6 7 0 1 2 3 4
0 -1
'''