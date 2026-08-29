# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
# - For example, the next permutation of arr = [1,2,3] is [1,3,2].
# - Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# - While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.


# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

from itertools import permutations



# brute force - O(n!.n), O(n!.n)
def next_permutation_1(nums: list[int]) -> list[int]:
    perms = sorted(set(permutations(nums)))
    
    for i in range(len(perms)):
        if perms[i] == tuple(nums):
            if i == (len(perms)-1):
                return list(perms[0])
            else:
                return list(perms[i+1])
    
    return nums



# optimal - O(n), O(n)
def next_permutation_2(nums: list[int]) -> list[int]:
    index = -1
    n = len(nums)
    
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            index = i
            break
            
    if index == -1:
        return nums[::-1]
    
    for i in range(n-1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break
        
    return nums[:index+1] + nums[index+1:][::-1]

    

if __name__ == "__main__":
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        res = next_permutation_1(nums)
        
        res = next_permutation_2(nums)
        
        print(*res)
        
        
'''
5
1 2 3
3 2 1
2 3 1
1 1 5
5 5 1
'''