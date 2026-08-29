# Given a string 's', find the length of the longest substring without duplicate characters.

# Constraints:
# 0 <= s.length <= 5 * 10⁴
# s consists of English letters, digits, symbols and spaces



# brute force - O(n²), O(n)
def longest_substring_without_repetition_1(s:str) -> int:
    n , max_len = len(s), 0
    
    for i in range(n):
        curr_len = 0
        freq = [0] * 128
        
        for j in range(i,n):
            ascii = ord(s[j])
            
            if freq[ascii] == 1:
                break
            
            freq[ascii] += 1

        curr_len = sum(freq)
        max_len = max(max_len, curr_len)
                
        
    return max_len
        
        
        
# hashing - O(n), O(n)
def longest_substring_without_repetition_2(s:str) -> int:
    n, max_len, left = len(s), 0, 0
    uset: set[int] = set()
    
    for right in range(n):
        
        while s[right] in uset:
            uset.remove(s[left])
            left += 1
        
        uset.add(s[right])
        max_len = max(max_len, right-left+1)
    
    return max_len
        
    


# optimal hashing - O(n), O(1)
def longest_substring_without_repetition_3(s:str) -> int:
    n, max_len, left = len(s), 0, 0
    freq = [-1] * 128
    
    for right in range(n):
        ascii = ord(s[right])
        
        if freq[ascii] >= left:
            left = freq[ascii] + 1
            
        freq[ascii] = right
        
        max_len = max(max_len, right-left+1)
        
    return max_len
        


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        s = str(input())

        # res = longest_substring_without_repetition_1(s)
        # res = longest_substring_without_repetition_2(s)
        res = longest_substring_without_repetition_3(s)
        
        print(res)
        
        
        
'''
5
abcabcbb
bbbbb
pwwkew
dvdf
bbbbb
'''