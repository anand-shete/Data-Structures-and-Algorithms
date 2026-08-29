# Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
# The union of two arrays can be defined as the common and distinct elements in the two arrays.
# NOTE: Elements in the union should be in ascending order.


# hashing - O(k.log(k)), O(n) 
# k is total unique elements accross both arrays
def union_of_sorted_arrays_1(nums1:list[int], nums2:list[int]) -> list[int]:
    uset1 = set(nums1)
    uset2 = set(nums2)
    
    return sorted(uset1.union(uset2))
    
    
    
    
# two pointers - O(n), O(1)
def union_of_sorted_arrays_2(nums1:list[int], nums2:list[int]) -> list[int]:
    n1, n2 = len(nums1), len(nums2)
    l1, l2 = 0, 0
    ans = []
    
    while l1 < n1 and l2 < n2:
        if nums1[l1] < nums2[l2]:
            if not ans or ans[-1] != nums1[l1]:
                ans.append(nums1[l1])
            l1 += 1
        elif nums1[l1] > nums2[l2]:
            if not ans or nums2[l2] != ans[-1]:
                ans.append(nums2[l2])
            l2 += 1
        else:
            if not ans or nums1[l1] != ans[-1]:
                ans.append(nums2[l2])
            l1 += 1
            l2 += 1 
            
    
    while l1 < n1:
        if not ans or nums1[l1] != ans[-1]:
            ans.append(nums1[l1])
        l1 += 1
            
        
    while l2 < n2:
        if not ans or nums2[l2] != ans[-1]:
            ans.append(nums2[l2])
        l2 += 1

    return ans

    
    
if __name__ == "__main__": 
    loops = int(input())

    for _ in range(loops):
        nums1 = list(map(int, input().split()))
        nums2 = list(map(int, input().split()))
        
        # ans = union_of_sorted_arrays_1(nums1, nums2)
        ans = union_of_sorted_arrays_2(nums1, nums2)
        
        print(*ans)
        
'''
4
0 1 2 3 4 5 6 8
-100 -1 3 99
0
-4 -3 -2 -1

-1
1 2 3 4 5 6
3 4 5 6 7 8
'''