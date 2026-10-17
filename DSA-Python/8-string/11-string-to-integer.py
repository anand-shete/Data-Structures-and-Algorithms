# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-2³¹, 2³¹ - 1], then round the integer to remain in the range. Specifically, integers less than -2³¹ should be rounded to -2³¹, and integers greater than 2³¹ - 1 should be rounded to 2³¹ - 1.
# Return the integer as the final result.
# first line of the input contains the string s

# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.



# brute force - O(N), O(1)
def string_to_integer(s:str) -> int:
    i, n = 0, len(s)
    ans = 0
    
    while i < n and s[i] == " ":
        i += 1
        
    sign = 1
    if i < n and (s[i] == "+" or s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i += 1
        
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')
        ans = ans*10 + digit
        
        i += 1
        
    INT_MIN, INT_MAX = -2**31, 2**31-1

    if sign * ans > INT_MAX:
        return INT_MAX
    if sign * ans < INT_MIN:
        return INT_MIN
    
    return sign * ans
    
    

if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        s = input()
        
        result = string_to_integer(s)

        print(result)
        
        
"""
6
42
 -00042
1337c0d3
0-1
words and 987
-91283472332
"""