# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
# first line of input represents string s
# second line of input represents string goal

# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.



# brute force - O(N²), O(1)
def rotate_string1(s:str, goal:str) -> bool:
    n = len(s)
    
    if n != len(goal):
        return False

    for i in range(n):
        temp = ""
        
        for j in range(n):
            temp += s[(i+j) % n]
            
        if temp == goal:
            return True
    return False



# s + s trick - O(n), O(2n)
def rotate_string2(s:str, goal:str) -> bool:
    return len(s) == len(goal) and goal in s+s


        
#  
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        s = input()
        goal = input()
        
        # result = rotate_string1(s, goal)
        result = rotate_string2(s, goal)
        
        print(result)
        
        
        
"""
3
abcde
cdeab
abcde
abced
ab
"""