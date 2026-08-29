# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Modify the array in place



# O(n), O(n)
def right_rotate_by_k_1(nums:list[int], k:int):
    n = len(nums)
    k %= n
        
    nums[:] = nums[n-k:] + nums[:n-k]



# optimal - O(n), O(1)
def reverse_range(start:int, end:int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
        
    
def right_rotate_by_k_2(nums:list[int], k:int):
    n = len(nums)
    k %= n
    
    reverse_range(0, n-1)
    reverse_range(0, k-1)
    reverse_range(k, n-1)
    
    
    
if __name__ == "__main__": 
    loops = int(input())

    for _ in range(loops):
        k = int(input())
        nums = list(map(int, input().split()))
        
        # right_rotate_by_k_1(nums, k)
        
        right_rotate_by_k_2(nums, k)
        
        print(*nums)
        
        
'''
3
3
1 2 3 4 5 6 7
2
-1 -100 3 99
7
1 2
'''