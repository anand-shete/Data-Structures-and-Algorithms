# Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.



# brute force - O(n), O(1)
def times_array_is_rotated_1(nums: list[int]) -> int:
    min_idx, n = 0, len(nums)
    
    for i in range(1, n):
        if nums[i] < nums[min_idx]:
            min_idx = i
            
    return min_idx



# binary search - O(log n), O(1)
def times_array_is_rotated_2(nums: list[int]) -> int:
    low, high = 0, len(nums)-1
    
    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
            
    return low
    
    
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        res = times_array_is_rotated_1(nums)
        # res = times_array_is_rotated_2(nums)
        
        print(res)
        
        
'''
5
4 5 6 7 0 1 2 3
3 4 5 1 2
5 4 3 2 1
3 2 1 5 4
1 2 3 4 5
'''