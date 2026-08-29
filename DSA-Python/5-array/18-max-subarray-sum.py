# Given an integer array nums, find the subarray with the largest sum, and return its sum.



# brute force - O(n²), O(1)
def max_subarray_sum_1(nums:list[int]) -> int:
    n , max_sum = len(nums), float('-inf')
    
    for i in range(n):
        sum = 0
        
        for j in range(i, n):
            sum += nums[j]
            
            if sum > max_sum:
                max_sum = sum
                
    return max_sum



# kadane - O(n), O(1)
def max_subarray_sum_2(nums:list[int]) -> int:
    n, max_sum, sum = len(nums), float('-inf'), 0
    
    for x in nums:
        sum += x
        
        if sum > max_sum:
            max_sum = sum
            
        if sum < 0:
            sum = 0
            
    return max_sum



if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        res = max_subarray_sum_1(nums)
        
        res = max_subarray_sum_2(nums)
        
        print(res)
        