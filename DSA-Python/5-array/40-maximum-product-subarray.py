# Given an integer array nums, find a subarray that has the largest product, and return the product. The test cases are generated so that the answer will fit in a 32-bit integer.
# Note that the product of an array with a single element is the value of that element.

# Constraints:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.



# brute force - O(n²), O(1)
def maximum_product_subarray_1(nums: list[int]) -> int:
    max_prod, n = float('-inf'), len(nums)
    
    for i in range(n):
        prod = 1
        
        for j in range(i, n):
            prod *= nums[j]
            
            if prod > max_prod:
                max_prod = prod
            
    return max_prod




# optimal - O(n), O(1)
def maximum_product_subarray_2(nums: list[map]) -> int:
    max_prod, pre, suf, n = float('-inf'), 1, 1, len(nums)
    
    for i in range(n):
        if pre == 0:
            pre = 1
            
        if suf == 0:
            suf = 1
        
        pre *= nums[i]
        suf *= nums[n-1-i]
            
        max_prod = max(max_prod, pre, suf)
        
    return max_prod


    
    
if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = maximum_product_subarray_1(nums)
        # res = maximum_product_subarray_2(nums)
        
        print(res)
        
        
'''
5
1 2 -3 4 5
1 2 -3 0 -4 -5
0
-2
-3 -2 -1 4
'''