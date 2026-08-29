# Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.
# Constraints:
# 1 <= nums.length <= 5 * 10⁴
# -10⁹ <= nums[i] <= 10⁹



# brute force - O(n²), O(1)
def majority_element_1(nums: list[int]) -> list[int]:
    n = len(nums)
    res = []
    
    for i in range(n):
        count = 0
        
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
                
        if count > n//3 and nums[i] not in res:
            res.append(nums[i])
            
    return res



# hashmap - O(n), O(1)
def majority_element_2(nums:list[int]) -> list[int]:
    n = len(nums)
    umap = {}
    res = []
    
    for x in nums:
        umap[x] = umap.get(x, 0) + 1
        
    for k,v in umap.items():
        if v > n//3:
            res.append(k)
            
    return res
    
    

# boyer moore voting - O(n), O(1)
def majority_element_3(nums: list[int]) -> list[int]:
    n, cnt1, cnt2, ele1, ele2 = len(nums), 0, 0, float('-inf'), float('-inf')
    res = []
    
    for i in range(n):
        if cnt1 == 0 and ele2 != nums[i]:
            cnt1 += 1
            ele1 = nums[i]
        elif cnt2 == 0 and ele1 != nums[i]:
            cnt2 += 1
            ele2 = nums[i]
        elif nums[i] == ele1:
            cnt1 += 1
        elif nums[i] == ele2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
            
    cnt1, cnt2 = 0, 0
    
    for x in nums:
        if x == ele1:
            cnt1 += 1
        elif x == ele2:
            cnt2 += 1
            
    if cnt1 > n//3:
        res.append(ele1)
    if cnt2 > n//3:
        res.append(ele2)
        
    return res
      
        
    

if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        nums = list(map(int , input().split()))
        
        res = majority_element_1(nums)
        res = majority_element_2(nums)
        res = majority_element_3(nums)
        
        print(res, end='\n\n')
        


'''
5
3 2 3
4
1 2
3 3 1 1 1 2 2 2
5 5 6 6 5 4 5 6
'''