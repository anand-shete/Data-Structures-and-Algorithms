# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.
# first line of input is string s

# Constraints:
# 1 <= s.length <= 5 * 10⁵
# s consists of uppercase and lowercase English letters and digits.


from collections import Counter
# sorting - O(N.log(K)), O(K) where N=length of input string, K=number of unique characters
def sort_characters_by_frequency(s:str) -> str:
    ans = ""
    
    sorted_pairs = sorted(Counter(s).items(), key=lambda pair: pair[1], reverse=True)
    result = []
    
    for char, freq in sorted_pairs:
        result.append(char * freq)
        
    return "".join(result)


# bucket sort - TODO for revision
# def 

if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        s = input()
        
        result = sort_characters_by_frequency(s)
        print(result)
        
        
"""
4
tree
cccaaa
Aabb
aa3AAbb2BB1
"""