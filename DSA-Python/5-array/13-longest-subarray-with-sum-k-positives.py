# Given an array nums of size n and an integer k containing non-zero integers, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0



# brute force - O(n²), O(1)
def len_of_longest_subarray_with_sum_k_1(nums: list[int], k:int) -> int:
    max_len, n = 0, len(nums) 
    
    for i in range(n):
        curr_sum = 0
        
        for j in range(i, n):
            curr_sum += nums[j]
            
            if curr_sum == k and j-i+1 > max_len:
                max_len = j-i+1
            
    return max_len



# prefix sum - O(n), O(1)
def len_of_longest_subarray_with_sum_k_2(nums:list[int], k:int) -> int:
    curr_sum, max_len, n = 0, 0, len(nums)
    umap = {0:-1}
    
    for i in range(n):
        curr_sum += nums[i]
        
        if curr_sum - k in umap:
            max_len = max(max_len, i-umap[curr_sum-k])

        if curr_sum not in umap:
            umap[curr_sum] = i
        
    return max_len



# sliding window - O(n), O(n)
def len_of_longest_subarray_with_sum_k_3(nums:list[int], k:int) -> int:
    sum , max_len, n = 0, 0, len(nums)
    left = 0
    
    for right in range(left, n):
        sum += nums[right]
        
        while sum > k:
            sum -= nums[left]
            left += 1
            
        max_len = max(max_len, right-left+1)
    
    return max_len


    
if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        k = int(input())
        nums = list(map(int, input().split()))
        
        res = len_of_longest_subarray_with_sum_k_1(nums, k)
        
        res = len_of_longest_subarray_with_sum_k_2(nums, k)
        
        # res = len_of_longest_subarray_with_sum_k_3(nums, k)
        
        print(res)
        
        
'''
3
15
10 5 2 7 1 9
6
3 2 1
3
0 0 1 0 0 1 0 1 2 0 0 1
'''