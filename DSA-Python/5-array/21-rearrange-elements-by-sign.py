# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should return the array of nums such that the array follows the given conditions:
# 1. Every consecutive pair of integers have opposite signs.
# 2. For all integers with the same sign, the order in which they were present in nums is preserved.
# 3. The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


# Constraints:
# 2 <= nums.length <= 2 * 105
# nums.length is even
# 1 <= |nums[i]| <= 105
# nums consists of equal number of positive and negative integers.



# optimal 1 - O(n), O(n)
def rearrange_elements_by_sign_1(nums:list[int]) -> list[int]:
    pos, neg, = [], []
        
    for i in range(len(nums)):
        if nums[i] < 0:
            neg.append(nums[i])
        else:
            pos.append(nums[i])
            
    pos.reverse()
    neg.reverse()

    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = pos.pop()
        else:
            nums[i] = neg.pop()
            
    return nums
    
    
    
# optimal 2 - O(n), O(n)
def rearrange_elements_by_sign_2(nums:list[int]) -> list[int]:
    pos_idx, neg_idx, n = 0, 1, len(nums)
    ans = [0] * len(nums)
    
    for i in range(n):
        if nums[i] > 0:
            ans[pos_idx] = nums[i]
            pos_idx += 2
        else:
            ans[neg_idx] = nums[i]
            neg_idx += 2
        
    return ans


    
if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        # res = rearrange_elements_by_sign_1(nums)
        res = rearrange_elements_by_sign_2(nums)
        
        print(*res)
        
        
'''
5
3 1 -2 -5 2 -4
-1 1
-3 -4 -2 1 2 4
1 2 3 -3 -4 -2
-3 -3 -3 3 3 3
'''