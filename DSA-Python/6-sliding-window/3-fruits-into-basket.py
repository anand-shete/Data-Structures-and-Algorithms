# Problem Statement: There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree. The goal is to gather as much fruit as possible, adhering to the owner's stringent rules :
# There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.
# Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.
# Once reaching a tree with fruit that cannot fit into any basket, stop.
# Return the maximum number of fruits that can be picked.



# brute force - O(n²), O(n)
def fruits_into_basket_1(nums: list[int]) -> int:
    max_fruits, n = 0, len(nums)
    
    for i in range(n):
        hashset = set()
        fruits = 0
        
        for j in range(i, n):
            hashset.add(nums[j])
            
            if len(hashset) > 2:
                break
            
            fruits += 1
            
        max_fruits = max(max_fruits, fruits)
        
    return max_fruits



# sliding window - O(n), O(1) since hashmap contains at most 3 elements
def fruits_into_basket_2(nums: list[int]) -> int:
    left, max_fruits, n = 0, 0, len(nums)
    umap = {}
    
    for right in range(n):
        umap[nums[right]] = umap.get(nums[right], 0) + 1
        
        while len(umap) > 2:
            umap[nums[left]] -= 1
            if umap[nums[left]] == 0:
                del umap[nums[left]]
            left += 1
            
        max_fruits = max(max_fruits, right - left + 1)
        
    return max_fruits
        
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = fruits_into_basket_1(nums)
        # res = fruits_into_basket_2(nums)
        
        print(res)
        
        
        
'''
5
1 2 1
1 2 3 2 2
1 1 2 2 2 3 3 3 
1 2 3 3 3 1 1 2
1 2 3 4 5 6
'''