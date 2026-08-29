# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Constraints:
# 1 <= nums.length <= 5 * 10⁴
# 1 <= nums[i] <= 10⁵
# 1 <= k <= nums.length



# brute force - O(n²), O(1)
def count_nice_subarrays_1(nums: list[int], k:int) -> int:
    max_cnt, n = 0, len(nums)
    
    for i in range(n):
        cnt = 0
        
        for j in range(i, n):
            if nums[j] % 2 == 1:
                cnt += 1
            
            if cnt == k:
                max_cnt += 1
                
            if cnt > k:
                break
            
    return max_cnt



# prefix sum - O(n), O(n)
def count_nice_subarrays_2(nums: list[int], k:int) -> int:
    max_cnt, n = 0, len(nums)
    odds = 0
    umap = {0: 1}
    
    for i in range(n):
        if nums[i] % 2 == 1:
            odds += 1
            
        if odds-k in umap:
            max_cnt += umap[odds-k]
            
        umap[odds] = umap.get(odds, 0) + 1
        
    return max_cnt
    


# sliding window - O(n), O(1)
def count_nice_subarrays_3(nums: list[int], k:int) -> int:
    return at_most(nums, k) - at_most(nums, k-1)


def at_most(nums: list[int], k:int) -> int:
    left, res, n = 0, 0, len(nums)
    
    for right in range(n):
        if nums[right] % 2 == 1:
            k -= 1
            
        while k < 0:
            if nums[left] % 2 == 1:
                k += 1
            left += 1
            
        res += right-left+1
        
    return res
    
    
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        k = int(input())
        nums = list(map(int, input().split()))
        
        # res = count_nice_subarrays_1(nums, k)
        # res = count_nice_subarrays_2(nums, k)
        res = count_nice_subarrays_3(nums, k)
        
        print(res)
        
        
'''
5
3
1 1 2 1 1
1
2 4 6
2
2 2 2 1 2 2 1 2 2 2
3
1 2 1 2 1
1
1 1 0
'''