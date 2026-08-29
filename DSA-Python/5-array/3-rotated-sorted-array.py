# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false. There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.



# brute force - O(n²), O(1)
def rotated_sorted_array_1(nums: list[int]) -> bool:
    n = len(nums)
    
    for i in range(n):
        is_sorted = True
        
        for j in range(n-1):
            curr = nums[(i+j) % n]
            next = nums[(i+j+1) % n]
            
            if curr > next:
                is_sorted = False
            
        if is_sorted:
            return True
    
    return False



# Optimal - O(n), O(1)
def rotated_sorted_array_2(nums: list[int]) -> bool:
    dip, n = 0, len(nums)
    
    for i in range(n - 1):
        if nums[i] > nums[i+1]:
            dip += 1
            
    if nums[n-1] > nums[0]:
        dip += 1
        
    return False if dip > 1 else True
    
    
        
if __name__ == "__main__": 
    loops = int(input())

    for _ in range(loops):
        nums = list(map(int, input().split()))
        
        # res = rotated_sorted_array_1(nums)
        
        res = rotated_sorted_array_2(nums)
        
        print(res)
        
        
'''
5
3 4 5 1 2
2 1 3 4
1 1 1 1
5 4 3 2 1
1 2 3 4 5
'''