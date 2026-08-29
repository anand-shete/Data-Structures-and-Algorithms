# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be `k`​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements `k`.
# The first `k` elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index `k - 1` can be ignored.



# Two pointers - O(n), O(n)
def remove_duplicates_in_place(nums:list[int]):
    j = 1
    
    for i in range(1, len(nums)):
        if nums[j-1] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            
    return j
    
    
    
if __name__ == "__main__":
    loops = int(input())

    for _ in range(loops):
        nums = list(map(int, input().split()))
        
        res = remove_duplicates_in_place(nums)
        
        print(res)
        
        
'''
3
1 1 2
0 0 1 1 1 2 2 3 3 4
1 2 2 2 3 3 4
'''