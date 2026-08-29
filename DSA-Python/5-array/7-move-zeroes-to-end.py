# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.



# brute force - O(n), O(n)
def move_zeroes_to_end_1(nums: list[int]):
    cnt, n = 0, len(nums)
    temp = []
    
    
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])
            cnt += 1
    
    for i in range(len(temp), n):
        temp.append(0)
        
    nums[:] = temp[:]
        
        
    
# optimal - O(n), O(1)
def move_zeroes_to_end_2(nums:list[int]):
    n = len(nums)
    i = 0
    
    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        
                

if __name__ == "__main__": 
    loops = int(input())

    for _ in range(loops):
        nums = list(map(int, input().split()))
        
        # move_zeroes_to_end_1(nums)
        
        move_zeroes_to_end_2(nums)
        
        print(*nums)
        
        
'''
5
0 1 0 3 12
0
1 2 0 0 5

0 0 -1 -3 -2 0 
'''