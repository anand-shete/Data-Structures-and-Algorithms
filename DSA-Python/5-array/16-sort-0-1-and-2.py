# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.



# brute
def main(nums:list) -> None:
    n = len(nums)
    low, mid, high = 0, 0, n-1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            
            
            
            
if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int, input().split()))
        
        main(nums)
        
        print(*nums)
        
        
'''
5
2 0 2 1 1 0
2 0 1
0
0 0 1 1 2 2
2 2 2 1 1 0 0 0
'''