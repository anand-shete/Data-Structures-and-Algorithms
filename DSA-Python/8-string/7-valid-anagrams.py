# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
# first line of input is a
# second line of input is t

# Constraints:
# 1 <= s.length, t.length <= 5 * 10⁴
# s and t consist of lowercase English letters


# brute force - O(N), O(1)
def valid_anagram1(s:str, t:str) -> bool:
    n = len(t)
    freq = [0] * 26
    
    if len(s) != n:
        return False
    
    for ch in s:
        freq[ord(ch)-ord('a')] += 1
        
    for ch in t:
        idx = ord(ch)-ord('a')
        
        if freq[idx] > 0:
            freq[idx] -= 1
        
    return sum(freq) == 0



# Counter data strcuture - O(N), O(1)
from collections import Counter
def valid_anagram2(s:str, t:str) -> bool:
    return Counter(s) == Counter(t)


    
if __name__=="__main__":
    t = int(input())
    
    for _ in range(t):
        s = input()
        t = input()
        
        # result = valid_anagram1(s,t)
        result = valid_anagram2(s,t)
        
        print(result)
        
        
        
        
"""
3
anagram
nagaram
rat
car
a
b
"""