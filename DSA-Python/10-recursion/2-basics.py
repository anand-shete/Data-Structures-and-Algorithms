# Sum of first N natural numbers 
# Parametrised recursion (backtracking) - O(N), O(N) where N = input
def sum_of_N1(i:int, ans:int):
    if i < 1:
        print(ans)
        return
    
    sum_of_N1(i-1, ans+i)
    
    
# Functional recursion - O(N), O(N) where N = input
def sum_of_N2(n:int):
    if n < 1:
        return 0
    
    return n + sum_of_N2(n-1)



# Factorial of N
# parameterised recursion - O(N), O(N) where N = input number
def factorial1(i:int, n:int):
    if n < 2:
        print(i)
        return
    
    factorial1(i*n, n-1)
    
    
# functional recursion - O(N), O(N) where N = input number
def factorial2(n:int):
    if n < 2:
        return 1
    
    return n * factorial2(n-1)



# Reverse array parameterized recursion - O(N), O(N) where N=length of input array
def reverse_array(left:int, right:int, arr:list[int]) -> None:
    if left >= right:
        return
    
    arr[left], arr[right] = arr[right], arr[left]
    
    reverse_array(left+1, right-1, arr)
    



# palindrome parameterized recursion - O(N), O(N) where N=length of string
def check_palindrome(left:int, right:int, string:str):
    if left >= right:
        return True
    
    if string[left] != string[right]:
        return False
    
    return check_palindrome(left+1, right-1, string)
    
    

# sum_of_N1(3, 0)
# print(sum_of_N2(10))
# factorial1(1, 5)
# print(factorial2(5))

arr = [1,2,3,4,5]
reverse_array(0, len(arr)-1, arr)
# print(arr)

string = "maam"
result = check_palindrome(0, len(string)-1, string)
print(result)