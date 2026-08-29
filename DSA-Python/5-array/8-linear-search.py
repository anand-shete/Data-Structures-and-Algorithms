# Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.



# O(n), O(1)
def linear_search(nums:list[int], target:int) -> bool:
    
    for x in nums:
        if (x == target):
            return True
        
    return False


if __name__ == "__main__":
    loops = int(input())

    for _ in range(loops):
        target = int(input())
        
        nums = list(map(int, input().split()))
        
        res = linear_search(nums, target)
        
        print(res)
        
        
        
'''
5
3
1 2 3 4 5
5
5 4 3 2 1
-3
0 0 -1 -3 -2 0 
-1
0
-1
'''