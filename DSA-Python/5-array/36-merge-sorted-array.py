# You are given two integer arrays 'nums1' and 'nums2', sorted in non-decreasing order, and two integers 'm' and 'n', representing the number of elements in 'nums1' and 'nums2' respectively
# Merge 'nums1' and 'nums2' into a single array sorted in non-decreasing order
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n

# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10⁹ <= nums1[i], nums2[j] <= 10⁹


# brute force - O(m+n. log(m+n)), O(1)
def merge_sorted_array_1(nums1:list[int], m:int, nums2:list[int], n:int) -> None:
    
    nums1[m:] = nums2
    nums1.sort()



# two pointers - O(n), O(1)
def merge_sorted_array_2(nums1:list[int], m:int, nums2:list[int], n:int) -> None:
    i, j, k = m-1, m+n-1, n-1
    
    while k >= 0:
        if i>=0 and nums1[i] > nums2[k]:
            nums1[j] = nums1[i]
            i -= 1
        else:
            nums1[j] = nums2[k]
            k -= 1
            
        j -= 1
            
    
            

if __name__ == "__main__":
    loop = int(input())

    for _ in range(loop):
        m , n = list(map(int, input().split()))
        
        nums1 = list(map(int, input().split()))
        nums2 = list(map(int, input().split()))
        
        # merge_sorted_array_1(nums1, m, nums2, n)
        merge_sorted_array_2(nums1, m, nums2, n)
        
        print(*nums1)