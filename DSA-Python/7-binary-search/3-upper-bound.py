# Given a sorted array of N integers and an integer x, write a program to return first element > x



# linear search - O(n), O(1)


# binary search - O(log n), O(1)
def upper_bound(nums: list[int], x:int) -> int:
    low, high = 0, len(nums) - 1
    ans = float('-inf')
    
    while low <= high:
        mid = (low + high) // 2
        
        if x < nums[mid]:
            ans = nums[mid]
            high = mid - 1
        else:
            low = mid + 1
            
    return ans



if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        x = int(input())
        nums = list(map(int, input().split()))
        
        res = upper_bound(nums, x)
        
        print(res)
        
        
        
'''
5
9
-1 0 3 5 9 12
2
-1 0 3 5 9 12
4
-1 3 4 6 10 11
2
1 2 2 3
3
3
'''