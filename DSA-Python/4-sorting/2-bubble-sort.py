

# Worst case time complexity - O(n²)
# Avg. case time complexity - O(n²)
# Best case time complexity - O(n)
# Space complexity - O(1)
def bubble_sort(nums:list) -> None:
    # bubble every element to correct place
    n = len(nums)
    
    swapped = False
    for i in range(1, n):
        for j in range(n-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
        
    print(*nums)
    
    
if __name__ == "__main__": 
    n = int(input())

    for _ in range(n):
        nums = list(map(int, input().split()))

        bubble_sort(nums)
        
        
'''
5
3 12 2 6 24 43
-2 45 54 3 12 23
8 8 8 8 8 8 0
0 -1 -4 -4 -4 -4 0
1, 2, 3, 4, 5
'''