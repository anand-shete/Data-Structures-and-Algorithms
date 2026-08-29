# Given an integer array nums, find the subarray with the largest sum, and print the subarray



# brute force - O(n²), O(1)
def max_subarray_sum_1(nums:list[int]) -> None:
    n , max_sum = len(nums), float('-inf')
    start, end = 0, 0
    
    for i in range(n):
        sum = 0
        
        for j in range(i, n):
            sum += nums[j]
            
            if sum > max_sum:
                max_sum = sum
                start = i
                end = j+1
                
    for i in range(start, end):
        print(nums[i], end=' ')
    print()



# kadane - O(n), O(1)
def max_subarray_sum_2(nums:list[int]) -> None:
    n, max_sum, sum = len(nums), float('-inf'), 0
    start, temp_start, end = 0, 0, 0
    
    
    for i in range(n):
        sum += nums[i]
        
        if sum > max_sum:
            max_sum = sum
            start = temp_start
            end = i+1
            
        if sum < 0:
            sum = 0
            temp_start = i+1
            
    for i in range(start, end):
        print(nums[i], end=' ')
    print()



if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        # max_subarray_sum_1(nums)
        
        max_subarray_sum_2(nums)
        
        
'''
5
-8 -3 -6 -2 -5 -4
0 -3 0 -2 0
-2 1 -3 4 -1 2 1 -5 4 
1
5 4 -1 7 8
'''