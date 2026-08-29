


# Worst case time complexity - O(n²)
# Avg. case time complexity - O(n²)
# Best case time complexity - O(n)
# Space complexity - O(1)
def insertion_sort(nums: list) -> None:
    # shift elements to right and insert
    
    n = len(nums)
    for i in range(1, n):
        ele = nums[i]
        j = i-1
        
        while j>=0 and nums[j]>ele:
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j+1] = ele
        
    print(*nums)
            
            
        
if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        nums = list(map(int, input().split()))
        
        insertion_sort(nums)
        
        
'''
5
3 12 2 6 24 43
-2 45 54 3 12 23
8 8 8 8 8 8 0
0 -1 -4 -4 -4 -4 0
1, 2, 3, 4, 5
'''