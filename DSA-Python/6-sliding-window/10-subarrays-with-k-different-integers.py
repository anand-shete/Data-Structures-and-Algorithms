# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

# Constraints:
# 1 <= nums.length <= 2 * 10⁴
# 1 <= nums[i], k <= nums.length

from collections import defaultdict


# brute force - O(n²), O(k)
def subarrays_with_k_different_integers_1(nums: list[int], k:int) -> int:
    ans, n = 0, len(nums)
    
    for i in range(n):
        uset = set()
        
        for j in range(i, n):
            uset.add(nums[j])
            
            if len(uset) == k:
                ans += 1
                
    return ans



# sliding window - O(n), O(n)
def at_most(nums: list[int], k:int) -> int:
    left, count, n = 0, 0, len(nums)
    freq = defaultdict(int)

    for right in range(n):
        if nums[right] not in freq:
            k -= 1
            
        freq[nums[right]] += 1
        
        while k < 0:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                k += 1
                del freq[nums[left]]
            left += 1
            
        count += right - left + 1
        
    return count

# exactly K = at most K - at most K-1
def subarrays_with_k_different_integers_2(nums: list[int], k:int) -> int:
    return at_most(nums, k) - at_most(nums, k-1)
            
    
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        k = int(input())
        nums = list(map(int, input().split()))
        
        # res = subarrays_with_k_different_integers_1(nums, k)
        res = subarrays_with_k_different_integers_2(nums, k)
        
        print(res)
        
        
'''
2
2
1 2 1 2 3
3
1 2 1 3 4
'''