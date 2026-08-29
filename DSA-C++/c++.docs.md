### ASLR

ASLR (Address Space Layout Randomization) is a computer security technique that prevents hackers from exploiting memory vulnerabilities. It randomizes the locations of program's memory to a completely new location in your RAM each time program runs.

### Stack

Whenever a varible is created, `int x = 34` it lives on the stack. The computer manages it for you. When your function ends, this memory is instantly destroyed. Stack starts at top of memory,

### Heap

When you create memory in Heap using the new keyword `int* x = new int(5)`, you are fully responsible for it. It stays alive until you manually destroy it using `delete`. If you forget, it causes a **memory leak**. Heap start at bottom in memory and grows upward.

### Segmentation fault

A segmentation fault (or `segfault`) is a specific runtime error that occurs when a program attempts to access a restricted memory location it does not have permission to read, write, or executeal memory access.

## Dangling pointer

If you delete node but forget to update adjacent node, it will still hold the exact memory address where deleted node used to live. This creates what is called a Dangling Pointer which creates `Segmentation fault`.

### Short circuit

Short-circuiting is a compiler optimization where a logical expression stops evaluating as soon as the final outcome is guaranteed. In C++, this behavior only applies to `&&` and `||`. E.g. `if (cond1 || cond2)` even if cond2 is undefined, c++ will short circut and execute if loop if cond 1 returns `true`.

### Stack overflow

It basically occurs when a program tries to use more memory on the call stack than was allocated for it. It is as specific type of buffer overflow that can trigger a segmentation fault. Most commonly caused by infinite or excessively deep recursion, or by allocating local variables that are too large for the stack.

### Loops

1. Use while loops when the no. of interations to perform is dynamic. eg. skip looping some elements while counting no. of occurrences

2. Use for loops when no. of interations to perform in same. eg. tranversing an array. If any single condition is not present in for loop, that means the value is dynamic and u must resort to while loops.

### \* pattern question

- For any pattern, break it into smaller parts and identify the number of spaces, and the number of stars/numbers only and design a logic
- Think about the spaces and think about how will you print them.
- Use one-based indexing because it is simple to print i stars on the i-th column (i=1 to i<=n)

### Expression Notations

1. **Infix Rule**
   `[Operand 1] [Operator] [Operand 2]`
   e.g. `A+B`
2. **Prefix Rule**:
   `[Operator] [Operand 1] [Operand 2]`
   e.g. `+AB`
3. **Postfix Rule** / **Reverse Polish Notation**
   `[Operand 1] [Operand 2] [Operator]`
   e.g. `AB+`

### Recursion

Recursion is a programming technique where a function calls itself to solve a problem. It works by breaking down a complex problem into smaller, self-similar subproblems, and the function calls itself to solve these smaller parts. This continues until a base case is reached. If there is no condition to stop the recursive calls, the calls will run indefinitely until the stack runs out of memory which is called as stack overflow leading to segmentation fault.
A base case is always necessary for the recursion to stop.

### Backtracking recusion

Backtracking recursion is an algorithmic technique used to find solutions to problems by systematically exploring all possible paths or configurations. It is fundamentally a type of recursion, but the print line would be kept after the function call inside the recursive function contrary to the forward recursion approach.
