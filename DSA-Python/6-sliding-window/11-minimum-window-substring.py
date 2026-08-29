# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.


# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 10⁵
# s and t consist of uppercase and lowercase English letters.

from collections import Counter


# brute force - O(n²), O(n)
def minimum_window_substring_1(s:str, t:str) -> str:
    n = len(s)
    ans = ""
    
    freq1 = Counter(t)
        
    for i in range(n):
        freq2 = Counter()
        curr_len = 0
        
        for j in range(i, n):
            ch = s[j]
            freq2[ch] += 1
            
            if ch in freq1 and freq1[ch] == freq2[ch]:
                curr_len += 1
                
            if curr_len == len(freq1):
                curr = s[i:j+1]
                
                if not ans or len(curr) < len(ans):
                    ans = curr
            
    return ans




def minimum_window_substring_2(s:str, t:str) -> str:
    left, curr_len, n, = 0, 0, len(s)
    ans = ""
    freq1 = Counter(t)
    freq2 = Counter()
    
    for right in range(n):
        freq2[s[right]] += 1
        
        if freq1[s[right]] == freq2[s[right]]:
            curr_len += 1
            
        while curr_len == len(freq1):
            curr = s[left:right+1]

            if ans == "" or len(curr) < len(ans):
                ans = curr
                
            freq2[s[left]] -= 1
            if freq2[s[left]] < freq1[s[left]]:
                curr_len -= 1
                
            left += 1   
            
            
    return ans
            
    
    

if __name__ == "__main__": 
    cases = int(input())

    for _ in range(cases):
        t = str(input())
        s = str(input())
        
        # res = minimum_window_substring_1(s, t)
        res = minimum_window_substring_2(s, t)
        
        print(res)
        
'''
5
ABC
ADOBECODEBANC
a
a
aa
a
abcd
z
ab
acdfbaaacbab
'''