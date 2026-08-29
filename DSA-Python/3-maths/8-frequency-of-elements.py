# Given an array, print the number of occurences of each element in array



# brute force - O(n²), O(n)
def frequency_of_elements_1(nums: list) -> None:
    n = len(nums)
    visited = [False] * n
    
    for i in range(n):
        cnt = 0
            
        if visited[i] == True:
            continue
        
        for j in range(i, n):
            
            if nums[i] == nums[j]:
                visited[j] = True
                cnt += 1
        
        print(nums[i], '=>', cnt)
        
    print()
    
    
# hashing - O(n), O(n)
def frequency_of_elements_2(nums: list) -> None:
    umap = {}
    
    for x in nums:
        umap[x] = umap.get(x, 0) + 1
        
    for (k, v) in umap.items():
        print(k, '=>', v)
        
    print()
    
    
if __name__ == "__main__": 
    n = int(input())
    
    for i in range(n):
        nums = list(map(int, input().split()))
        
        # frequency_of_elements_1(nums)
        
        frequency_of_elements_2(nums)
        
        
'''
3
1 2 3 4

3 3 3 3 -1 -1 2
'''