# Given an integer array nums of size n, return all the leaders in the array. A leader is an element that is greater than or equal to every element to its right.
# The rightmost element is always considered a leader because there are no elements to its right.
# Return the leaders in the same order as they appear in the array.


# Constraints:
# 1 <= n <= 10⁵
# -10⁹<= nums[i] <= 10⁹



# brute force - O(n²), O(1)
def leaders_of_array_1(nums:list[int]) -> list[int]:
    ans = []
    n = len(nums)
    
    for i in range(n):
        greater = False
        
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                greater = True
                break
                
        if not greater:
            ans.append(nums[i])
        
    return ans



# optimal - O(n), O(1)
def leaders_of_array_2(nums:list[int]) -> list[int]:
    n = len(nums)
    maxi = nums[n-1]
    ans = [maxi]
    
    for i in range(n-2, -1, -1):
        if nums[i] >= maxi:
            ans.append(nums[i])
            maxi = nums[i]
            
    ans.reverse()
    return ans
    


if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        # ans = leaders_of_array_1(nums)
        # ans = leaders_of_array_2(nums)
    
        print(*ans)
    
    
'''
5
10 22 12 3 0 6
4 4 2 1
1 2 3 4
5 5 5 5
1 2 3 4 5
'''