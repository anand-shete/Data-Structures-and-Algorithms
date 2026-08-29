# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# Constraints:
# 3 <= s.length <= 5 x 10⁴
# s only consists of 'a', 'b' or 'c' characters. 

from collections import defaultdict


# brute force - O(n²), O(n)
def number_of_subtrings_1(s: str) -> int:
    ans, n = 0, len(s)
    
    for i in range(n):
        umap = defaultdict(int)
        
        for j in range(i, n):
            umap[s[j]] += 1
            
            if umap['a'] > 0 and umap['b'] > 0 and umap['c'] > 0:
                ans += 1
                
    return ans



# sliding window - O(n), O(n)
def number_of_subtrings_2(s:str) -> int:
    left, n, res = 0, len(s), 0
    umap = defaultdict(int)
    
    for right in range(n):
        umap[s[right]] += 1
        
        while umap['a'] > 0 and umap['b'] > 0 and umap['c'] > 0:
            res += n - right
            
            umap[s[left]] -= 1
            
            left += 1
            
    return res
    


if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        s = str(input())
        
        # res = number_of_subtrings_1(s)
        # res = number_of_subtrings_2(s)
        
        print(res)
        
        
'''
5
abcabc
aaacb
abc
abcba
ccabcc
'''