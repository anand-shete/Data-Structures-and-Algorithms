# Given a binary array nums, return the maximum number of consecutive 1's in the array.



# brute force - O(n), O(1)
def maximum_consecutive_ones_1(nums:list[int]) -> int:
    cnt, max_ones = 0, 0
    
    for x in nums:
        if (x != 1):
            cnt = 0
        else:
            cnt += 1
            max_ones = max(max_ones, cnt)
            
    return max_ones
    
    

# sliding window - O(n), O(1)
def maximum_consecutive_ones_2(nums:list[int]) -> int:
    left, n, max_ones = 0, len(nums), 0
    
    for right in range(n):
        if nums[right] == 0:
            left = right + 1
        else:
            max_ones = max(max_ones, right-left+1)
            
    return max_ones



if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        res = maximum_consecutive_ones_1(nums)
        
        res = maximum_consecutive_ones_2(nums)
        
        print(res)
        
        
'''
5
1 1 0 1 1 1
1 0 1 1 0 1
1

0
'''