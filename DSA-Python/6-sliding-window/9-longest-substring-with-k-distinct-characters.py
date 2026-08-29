# Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.



# brute force - O(n²), O(k)
def longest_substring_with_k_distinct_characters_1(s:str, k:int) -> int:
    n, max_len = len(s), 0
    
    for i in range(n):
        uset = set()
        curr_len = 0
        
        for j in range(i, n):
            uset.add(s[j])
                
            if len(uset) > k:
                break
            
            curr_len += 1
        
        max_len = max(max_len, curr_len)
        
    return max_len




# sliding window - O(n), O(n)
def longest_substring_with_k_distinct_characters_2(s:str, k:int) -> int:
    max_len, left, n = 0, 0, len(s)
    umap = {}
    
    for right in range(n):
        umap[s[right]] = umap.get(s[right], 0) + 1
        
        while len(umap) > k:
            umap[s[left]] -= 1
            if umap[s[left]] == 0:
                del umap[s[left]]
            left += 1
            
        max_len = max(max_len, right-left+1)
        
    return max_len
    
    
    
    
if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        k = int(input())
        s = str(input())
        
        res = longest_substring_with_k_distinct_characters_1(s, k)
        # res = longest_substring_with_k_distinct_characters_2(s, k)
        
        print(res)
        
        
'''
4
2
aababbcaacc
3
abcddefg
0
aabbccdd
1
abbbbbccd
'''