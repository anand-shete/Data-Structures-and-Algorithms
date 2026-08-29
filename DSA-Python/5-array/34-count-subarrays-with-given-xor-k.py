# Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k




# brute force - O(n²), O(1)
def total_subarrays_with_given_xor_k_1(nums: list[int], k:int) -> int:
    max_count, n = 0, len(nums)
    
    for i in range(n):
        xor = 0
        
        for j in range(i, n):
            xor ^= nums[j]
            
            if xor == k:
                max_count += 1
                
    return max_count



# prefix sum - O(n), O(n)
def total_subarrays_with_given_xor_k_2(nums:list[int], k:int) -> int:
    max_count, xor, n = 0, 0, len(nums)
    umap = {0:1}
    
    for i in range(n):
        xor ^= nums[i]
        
        if xor^k in umap:
            max_count += umap[xor^k]
            
        umap[xor] = umap.get(xor, 0) + 1
        
    return max_count
    
    

if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        k = int(input())
        nums = list(map(int, input().split()))
        
        res = total_subarrays_with_given_xor_k_1(nums, k)
        res = total_subarrays_with_given_xor_k_2(nums, k)
        
        print(res)
        
        

'''
2
6
4 2 2 6 4
5
5 6 7 8 9
'''