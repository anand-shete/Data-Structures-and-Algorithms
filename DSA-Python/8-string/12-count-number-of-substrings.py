# You are given a string s and a positive integer k.
# Return the number of substrings that contain exactly k distinct characters.
# first line of input is k 
# second line of input is s



# brute force - O(N²), O(N)
def count_number_of_substrings1(s:str, k:int) -> int:
    ans, n = 0, len(s)
    
    for i in range(n):
        uset = set()
        
        for j in range(i, n):
            uset.add(s[j])
            
            if len(uset) == k:
                ans += 1
                
            if len(uset) > k:
                break
    return ans

    


# sliding window - O(N), O(1)
from collections import defaultdict

def at_most(s:str, k:int) -> int:
    ans, n, left = 0, len(s), 0
    umap = defaultdict(int)
    
    if k < 1:
        return 0
    
    for right in range(n):
        umap[s[right]] += 1
        
        while len(umap) > k:
            umap[s[left]] -= 1
            if umap[s[left]] == 0:
                del umap[s[left]]
            left += 1
            
        ans += right-left+1
            
    return ans
    
    
def count_number_of_substrings2(s:str, k:int) -> int:
    return at_most(s, k) - at_most(s, k-1)
    
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        k = int(input())
        s = str(input())
        
        # result = count_number_of_substrings1(s, k)
        result = count_number_of_substrings2(s, k)
        
        print(result)
        
        
"""
2
2
pqpqs
3
abcbaa
"""