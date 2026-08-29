# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Constraints:
# 1 <= s.length <= 10⁴
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.



# brute force - O(n), O(n)
def reverse_words_in_string_1(s: str) -> str:
    words = []
    word = ""
    
    for ch in s:
        if ch != ' ':
            word += ch
        elif word:
            words.append(word)
            word = ""
            
    if word:
        words.append(word)
    
    words.reverse()
    return ' '.join(words)
            


# optimal - O(n), O(1)
def reverse_words_in_string_2(s: str) -> str:
    ans = ''
    start = end = len(s)-1
    
    while end >= 0:
        while end >= 0 and s[end] == ' ':
            end -= 1
            
        if end < 0:
            break
        
        start = end
        while start > 0 and s[start] != ' ':
            start -= 1
            
        word = s[start+1:end+1]
        
        if ans != "":
            ans += " "
            
        ans += word
        
    return ans



if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        s = str(input())
        
        # res = reverse_words_in_string_1(s)
        res = reverse_words_in_string_2(s)
        
        print(res)
        

'''
5
the sky is blue
  hello world  
a good   example
   the sky is blue   
hello
'''