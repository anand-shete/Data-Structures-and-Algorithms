import math
import sys
# Given an integer num, return the number of digits in num



# string - O(n), O(n)
def count_digit_1(num:int):
    string = str(num)
    return len(string)


# sub-optimal - O(log_10 n), O(1)
def count_digit_2(num:int):
    digit = 0
    temp = abs(num)

    if num == 0:
        return 1

    while temp > 0:
        digit += 1
        temp //= 10

    return digit
    

# log function - O(1), O(1)
def count_digit_3(num:int):
    if num == 0:
        return 1
    
    return math.floor(math.log10(abs(num))) + 1



if __name__ =="__main__":
    for line in sys.stdin:
        line = line.strip()
        
        n = int(line)
        
        # res = count_digit_1(n)
        
        # res = count_digit_2(n)
        
        res = count_digit_3(n)

        print(res)
        
        
'''
34
4567
12
1
0
'''