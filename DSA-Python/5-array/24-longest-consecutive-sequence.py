# Given an unsorted array of integers nums, return the length of the long consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.


# Constraints:

# 0 <= nums.length <= 10⁵
# -10⁹ <= nums[i] <= 10⁹  



# O(n.logn), O(1)
def longest_consecutive_sequence_1(nums: list[int]) -> int:
    if not nums:
        return 0
    
    cnt, longest = 1,1
    nums.sort()
    
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i] + 1:
            cnt += 1
        elif nums[i+1] == nums[i]:
            continue
        else:
            longest = max(longest, cnt)
            cnt = 1
     
    if cnt > longest:
        longest = cnt
         
    return longest

    

# O(n), O(n)
def longest_consecutive_sequence_2(nums:list[int]) -> int:
    uset = set()
    n, longest = len(nums), 0
    
    for x in nums:
        uset.add(x)
        
    for x in uset:
        if x-1 not in uset:
            counter = 1
            
            while x + 1 in uset:
                counter += 1
                x += 1
            
            longest = max(longest, counter)
            
    return longest
    
    
    
if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        # res = longest_consecutive_sequence_1(nums)
        
        res = longest_consecutive_sequence_2(nums)
        
        print(res)
        

'''
5

42
7 7 7 7 7
0 3 7 2 5 8 4 6 0 1
2 -1 1 0 -1 -2
'''