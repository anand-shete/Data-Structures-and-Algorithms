# Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.



# brute force - O(n²), O(1)
def length_of_longest_subarray_with_zero_sum_1(nums:list[int]) -> int:
    max_len, n = 0, len(nums)
    
    for i in range(n):
        sum = 0
        
        for j in range(i, n):
            sum += nums[j]
            
            if sum == 0:
                max_len = max(max_len, j-i+1)
                
    return max_len




# prefix sum - O(n), O(n)
def length_of_longest_subarray_with_zero_sum_2(nums:list[int]) -> int:
    max_len, sum, n = 0, 0, len(nums)
    umap = {0:-1}
    
    for i in range(n):
        sum += nums[i]
        
        if sum in umap:
            max_len = max(max_len, i-umap[sum])
            
        if sum not in umap:
            umap[sum] = i

    return max_len

            
            
            
    
    
if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        res = length_of_longest_subarray_with_zero_sum_1(nums)
        res = length_of_longest_subarray_with_zero_sum_2(nums)
        
        print(res)
        

'''
5
9 -3 3 -1 6 -5
6 -2 2 -8 1 7 4 -10
0 0 0 0 -1 -1 2
-3 -1 -2 3 2 1
0 0 0 0 0
'''