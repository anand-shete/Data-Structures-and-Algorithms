# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Constraints:
# 1 <= nums.length <= 10⁵
# 0 <= k <= nums.length
# nums[i] is either 0 or 1.



# brute force - O(n²), O(1)
def maximum_consecutive_ones_1(nums: list[int], k: int) -> int:
    max_ones, n = 0, len(nums)
    
    for i in range(n):
        zeroes = 0
        
        for j in range(i, n):
            if nums[j] == 0:
                zeroes += 1
                
            if zeroes > k:
                break
                
            max_ones = max(max_ones, j-i+1)
        
    return max_ones




# sliding window - O(n), O(1)
def maximum_consecutive_ones_2(nums: list[int], k:int) -> int:
    max_ones, n, left, zeroes = 0, len(nums), 0, 0
    
    for right in range(n):
        if nums[right] == 0:
            zeroes += 1
            
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
            
        max_ones = max(max_ones, right-left+1)
        
    return max_ones
         
    


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        k = int(input())
        nums = list(map(int, input().split()))
        
        res = maximum_consecutive_ones_1(nums, k)
        res = maximum_consecutive_ones_2(nums, k)
        
        print(res)
        
        

'''
5
2
1 1 1 0 0 0 1 1 1 1 0
3
0 0 1 1 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1
0
1 1 1
1
0
1
1 0 0 1 0 1
'''