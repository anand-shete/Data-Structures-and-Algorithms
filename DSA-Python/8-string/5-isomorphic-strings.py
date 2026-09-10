# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# first line of input is string s while second line represents t


# Constraints:
# 1 <= s.length <= 5 * 10⁴
# t.length == s.length
# s and t consist of any valid ascii character.
from collections import defaultdict


# brute force - O(n²), O(1)
def isomorphic_strings1(s:str, t:str) -> bool:
    n = len(s)
    
    if len(s) != len(t):
        return False
    
    
    for i in range(n):
        
        for j in range(1, n):
            if s[i] == s[j] and t[i] != t[j]:
                return False
            
            if t[i] == t[j] and s[i] != s[j]:
                return False
            
    return True

            
    
    
# hashing - O(n), O(n)
def isomorphic_strings2(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    umap1 = defaultdict(str)
    umap2 = defaultdict(str)
    
    for i in range(len(s)):
        if (s[i] in umap1 and umap1[s[i]] != t[i]) or (t[i] in umap2 and umap2[t[i]] != s[i]):
            return False
        
        umap1[s[i]] = t[i]
        umap2[t[i]] = s[i]
        
    return True      
        

if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        s = str(input())
        t = input()
        
        # result = isomorphic_strings1(s,t)
        result = isomorphic_strings2(s,t)
        
        print(result)
        
        

"""
5
egg
add
f11
b23
paper
title
bbbaaaba
aaabbbba
aabbcc
aabbc
"""