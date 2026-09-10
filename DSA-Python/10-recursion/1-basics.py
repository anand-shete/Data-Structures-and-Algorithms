# Print your name `n` times using recursion - O(N), O(N)
def print_name(n:int) -> None:
    global cnt
    if n < 1:
        return
    
    print("anand")
    
    print_name(n-1)
    
    
    
# Print from 1 to N using recursion - O(N), O(N)
def print_1_to_N(i:int, n:int):
    if i > n:
        return
    
    print(i)
    i+=1
    
    print_1_to_N(i, n)
    
    
    
# Print 1 to N using backtracking - O(N), O(N)
def print_1_to_N_backtracking(n:int):
    if n < 1:
        return
    
    print_1_to_N_backtracking(n-1)
    print(n)
    
    
    
# Print from N to 1 using recursion - O(N), O(N)
def print_N_to_1(n:int):
    if n < 1:
        return
    
    print(n)
    
    print_N_to_1(n-1)
    
    
    
# Print from N to 1 using backtracking - O(N), O(N)
def print_N_to_1_backtrack(i:int, n:int):
    if i > n:
        return
    
    print_N_to_1_backtrack(i+1, n)
    print(i)



# Print list using single parameter - O(N), O(N)
def print_list(n:int):
    if n < 1:
        return
    
    print(n, end=" ")
    print_list(n-1)
    
    
    
print_name(5)
# print_1_to_N(1, 10)
# print_1_to_N_backtracking(10)
# print_N_to_1(10)
# print_N_to_1_backtrack(1, 10)
# print_list(3)