# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# Constraints:
# 1 <= nums.length <= 2 * 10⁴
# -1000 <= nums[i] <= 1000
# -10⁷ <= k <= 10⁷


# brute force - O(n²), O(1)
def total_subarrays_sum_to_k_1(nums:list[int], k:int) -> int:
    n, res = len(nums), 0

    for i in range(n):
        sum = 0
        
        for j in range(i, n):
            sum += nums[j]
                
            if sum == k:
                res += 1
                
    return res



# prefix sum - O(n), O(n)
def total_subarrays_sum_to_k_2(nums:list[int], k:int) -> int:
    n, total, sum = len(nums), 0, 0
    umap = {0:1}
    
    for i in range(n):
        sum += nums[i]
        
        if sum - k in umap:
            total += umap[sum-k]
            
        umap[sum] = umap.get(sum, 0) + 1
        
    return total
    
    
    
if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        k = int(input())
        nums = list(map(int, input().split()))
        
        res = total_subarrays_sum_to_k_1(nums, k)
        res = total_subarrays_sum_to_k_2(nums, k)
        
        print(res)
        
        
'''
5
2
1 1 1 1 1
3
1 2 3
10
4 3 1 3 2 3
5
-1 -2 -3 -4 5
12
6 2 8 4 10 2
'''