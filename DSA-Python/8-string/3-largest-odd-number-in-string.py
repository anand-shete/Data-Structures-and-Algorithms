# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

# Constraints:
# 1 <= num.length <= 10⁵
# num only consists of digits and does not contain any leading zeros.
# first line of input is num string



# brute force - O(n²), O(n) where n is length of string
def largest_odd_number_in_string1(num:str) -> str:
    n = len(num)
    ans = "0"
    
    for i in range(n):
        curr = ""
        
        for j in range(i,n):
            curr += num[j]
            
            if int(curr) % 2 == 1 and int(curr) > int(ans):
                ans = curr
                
    return "" if ans == "0" else ans



# optimal - O(n), O(1) where n is length of string
def largest_odd_number_in_string2(num:str) -> str:
    n = len(num)
    
    for i in range(-1, -n-1, -1):
        if num[i] in {'1', '3', '5','7', '9'}:
            return num[:n+i+1]
        
    return ""
        
    

    
    
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        num = str(input())
        
        # result = largest_odd_number_in_string1(num)
        result = largest_odd_number_in_string2(num)
        
        print(result)
        
        
"""
5
52
4206
35427
1
9999
"""