

# sort - O(n. log n), O(n)
def largest_element_1(nums:list) ->int:
    nums.sort()
    
    return nums[-1]
    


# optimal - O(n), O(1)
def largest_element_2(nums: list) -> int:
    return max(nums)


if __name__ == "__main__": 
    loops = int(input())

    for _ in range(loops):
        nums = list(map(int, input().split()))
        
        res = largest_element_1(nums)
        res = largest_element_2(nums)
        
        print(res)
        
        
'''
5
3 12 2 6 24 43
-2 45 54 3 12 23
-4 -1 -3 -5 -14
0 -1 -4 -4 -4 -4 0
1 2 3 4 5
'''