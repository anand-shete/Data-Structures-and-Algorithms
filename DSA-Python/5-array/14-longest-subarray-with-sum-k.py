# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0



# brute force - O(n²), O(1)
def len_of_longest_subarray_having_sum_k_1(nums: list[int], k:int) -> int:
    max_len, n = 0, len(nums) 
    
    for i in range(n):
        sum = 0
        
        for j in range(i, n):
            sum += nums[j]
            
            if (sum == k):
                max_len = max(max_len, j-i+1)
                
    return max_len


    
# prefix sum - O(n), O(n)
def len_of_longest_subarray_having_sum_k_2(nums:list[int], k:int) -> int:
    max_len, n, curr_sum = 0, len(nums), 0
    umap = {0:-1}
    
    for i in range(n):
        curr_sum += nums[i]
        
        if curr_sum - k in umap:
            max_len = max(max_len, i - umap[curr_sum - k])
        
        
        if curr_sum not in umap:
            umap[curr_sum] = i
            
    return max_len
            
            
            
if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        k = int(input())
        nums = list(map(int, input().split(' ')))
        
        res = len_of_longest_subarray_having_sum_k_1(nums, k)
        
        # res = len_of_longest_subarray_having_sum_k_2(nums, k)
        
        print(res)
        
        
        
'''
5
15
10 5 2 7 1 9
6
3 2 1
3
0 0 1 0 0 1 0 1 2 0 0 1
3
4 -1
8
6 -2 2 -8 1 7 4 -10
'''