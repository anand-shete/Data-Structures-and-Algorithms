# Given an array, return the second smallest and second largest element in the array. -1 if none exists



# sort function - O(n. logn), O(n)
def second_largest_and_second_smallest_1(nums: list) -> tuple:
    unique = sorted(list(set(nums)))
    
    if (len(unique)) < 2:
        return (-1, -1)
    
    return (unique[-2], unique[1])
    

    
# optimal - O(n), O(1)
def second_largest_and_second_smallest_2(nums:list) -> tuple:
    n = len(nums)
    
    if n < 2:
        return (-1, -1)
    
    small = second_small = float('inf')
    large = second_large = float('-inf')

    for i in range(n):
        if nums[i] > large:
            second_large = large
            large = nums[i]
        elif large > nums[i] > second_large:
            second_large = nums[i]

        if nums[i] < small:
            second_small = small
            small = nums[i]
        elif small < nums[i] < second_small:
            second_small = nums[i]
            
    second_small = -1 if second_small == float('inf') else second_small
    second_large = -1 if second_large == float('-inf') else second_large
    
    return (second_large, second_small)


    
if __name__ == "__main__": 
    loops = int(input())

    for _ in range(loops):
        nums = list(map(int, input().split()))
        
        res = second_largest_and_second_smallest_1(nums)
        # res = second_largest_and_second_smallest_2(nums)
        
        print(res)
        
        
        
'''
5
1 2 4 1 7 7 5
5 5 5 5

4
-10 3
'''