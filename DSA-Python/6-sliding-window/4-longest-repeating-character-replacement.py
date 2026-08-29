# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length



# brute force - O(n²), O(1)
def longest_repeating_character_replacement_1(s: str, k:int) -> int:
    max_len, n = 0, len(s)

    for i in range(n):
        max_freq = 0
        freq = [0] * 26
        
        for j in range(i, n):
            idx = ord(s[j]) - ord('A')
            freq[idx] += 1
            
            max_freq = max(max_freq, freq[idx])
            
            if j-i+1 - max_freq <= k:
                max_len = max(max_len, j-i+1)
                
    return max_len
            
        

# sliding window - O(n), O(1)
def longest_repeating_character_replacement_2(s:str, k:int) -> int:
    left, max_len, n = 0, 0, len(s)
    freq = [0] * 26
    max_freq = 0
    
    for right in range(n):
        idx = ord(s[right]) - ord('A')
        freq[idx] += 1
        
        max_freq = max(max_freq, freq[idx])
        
        while right-left+1 - max_freq > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1
            
        max_len = max(max_len, right-left+1)
        
    return max_len
    


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        k = int(input())
        s = str(input())
        
        # res = longest_repeating_character_replacement_1(s, k)
        res = longest_repeating_character_replacement_2(s, k)
        
        print(res)
        
        
        
'''
5
1
BAAAB
1
AABABBA
3
ABCDEF
2
AABBACCAA
1
AB
'''