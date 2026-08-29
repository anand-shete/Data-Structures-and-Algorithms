

# Worst case time complexity - O(n²)
# Avg. case time complexity - O(n²)
# Best case time complexity - O(n²)
# Space complexity - O(1) 
def selection_sort(nums:list) -> None:
    # find minimum and swap with start index
    n = len(nums)
    
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if nums[j] < nums[mini]:
                mini = j
            
        nums[mini], nums[i] = nums[i], nums[mini]
            
    print(*nums)
    
    
    
if __name__ == "__main__": 
    loops = int(input())
    
    for _ in range(loops):
        nums = list(map(int, input().split()))
        
        selection_sort(nums)
        
        
        
'''
5
3 12 2 6 24 43
-2 45 54 3 12 23
8 8 8 8 8 8 0
0 -1 -4 -4 -4 -4 0
1, 2, 3, 4, 5
'''