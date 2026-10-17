# Given a string s, return the longest palindromic substring in s.
# A string is palindromic if it reads the same forward and backward.
# first line of input represents string s

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


def longest_palindromic_substring1(s:str):
    ans, n = 0, len(s)
    
    for i in range(n):
        curr = ""
        
        for j in range(i, n):
                curr += s[j]
                
                for k in range(len(curr) // 2):
                    reverse()
                    
    return ans



if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        s = input()
        
        result = longest_palindromic_substring1(s)
        
        print(result)