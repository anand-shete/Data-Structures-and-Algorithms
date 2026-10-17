# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
# first line of input contains the string s

# Constraints:
# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that parentheses expression s is a VPS.



# optimal - O(N), O(1)
def maximum_nesting_depth_for_parenthesis1(s:str) -> int:
    curr, max_depth = 0, 0
    
    for ch in s:
        if ch == '(':
            curr += 1
            if curr > max_depth:
                max_depth = curr
        elif ch == ')':
            curr -= 1
            
    return max_depth


if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        s = input()
        
        result = maximum_nesting_depth_for_parenthesis1(s)
        print(result)
        
        
"""
3
(1+(2*3)+((8)/4))+1
(1)+((2))+(((3)))
()(())((()()))
"""