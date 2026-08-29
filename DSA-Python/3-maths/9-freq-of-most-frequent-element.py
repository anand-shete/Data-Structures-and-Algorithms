# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array 'nums' and an integer 'k'. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most 'k' operations.


# brute force - O(n²), O(1)
def freq_of_most_frequent_1(nums:list, k:int) -> int:
    n = len(nums)
    ans = 1
    nums.sort()
    
    for i in range(n):
        cost = 0
        
        for j in range(i-1, -1, -1):
            cost += nums[i] - nums[j]
            
            if cost > k:
                break
            
            ans = max(ans, i-j+1)

    return ans


# sliding window - O(n.log n), O(n)
def freq_of_most_frequent_2(nums:list, k:int) -> int:
    left, curr_sum, maxFreq, n = 0, 0, 0, len(nums)
    
    nums.sort()
    
    for right in range(n):
        curr_sum += nums[right]
        
        while curr_sum + k < nums[right] * (right-left+1):
            curr_sum -= nums[left]
            left += 1
            
        maxFreq = max(maxFreq, right-left+1)
    
    return maxFreq


# prefix sum + binary search


if __name__ == "__main__": 
    n = int(input())
    
    for _ in range(n):
        k = int(input())
        nums = list(map(int, input().split()))
        
        # res = freq_of_most_frequent_1(nums, k)
        # res = freq_of_most_frequent_2(nums, k)
        
        print(res)
        
        
'''
3
5
1 2 4
5
1 4 8 13
2
3 9 6
'''