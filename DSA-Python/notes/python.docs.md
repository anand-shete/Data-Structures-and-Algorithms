## Identifiers

Identifiers are names given to variables, functions, classess and modules. They must follow Python's identifier naming rules:

- No numbers at start of identifiers
- Cannot use special characters except `_`
- Cannot use reserved keywords as identifiers

## Loops

1. Use `while` loops when the no. of interations to perform is dynamic. eg. skip looping some elements while counting no. of occurrences

2. Use for loops when no. of interations to perform in same. eg. tranversing an array. If any single condition is not present in `for` loop, that means the value is dynamic and you must resort to `while` loops.

## Modules

Module in python is a single `.py` file containing code

## Packages

A package in python is a collection of multiple modules grouped together

## ASLR

Address Space Layout Randomization (ASLR) is a computer security technique that randomizes the locations of a program's memory in your RAM each time it runs. In Python, this happens entirely in the background to protect the underlying C-based interpreter execution environment.

## _Short circuit_

Short-circuiting is a compiler optimization where a logical expression stops evaluating as soon as the final outcome is guaranteed. In C++, this behavior only applies to `&&` and `||`. E.g. `if (cond1 || cond2)` even if cond2 is undefined, c++ will short circut and execute if loop if cond 1 returns `true`.

## _Stack_

Stack behaves as a execution **call stack.** When a function is called, a new stack frame is created to manage execution flow and hold local object references. When the function returns, its stack frame is instantly destroyed. Python stack frames only store references (pointers) to objects

## _Heap_

All objects (integers, strings, lists, custom classes) are dynamically allocated on the heap. Python automatically handles allocation and deallocation using a built-in Garbage Collector (primarily via Reference Counting). When an object's reference count drops to zero, its heap memory is instantly reclaimed, preventing memory leaks.

## _Segmentation fault_

A segmentation fault (or `segfault`) is a specific runtime error that occurs when a program attempts to access a restricted memory location it does not have permission to read, write, or executeal memory access.

## _Dangling pointer_

If you delete node in linked list but forget to update adjacent node, it will still hold the exact memory address where deleted node used to live. This creates what is called a Dangling Pointer which leads to `Segmentation fault`.

## _Stack overflow_

It basically occurs when a program tries to use more memory on the call stack than was allocated for it. It is as specific type of buffer overflow that can trigger a segmentation fault. Most commonly caused by infinite or excessively deep recursion, or by allocating local variables that are too large for the stack.

## Expression Notations

1. **Infix Rule**
   `[Operand 1] [Operator] [Operand 2]` For e.g. `A+B`

2. **Prefix Rule**:
   `[Operator] [Operand 1] [Operand 2]` For e.g. `+AB`

3. **Postfix Rule** / **Reverse Polish Notation**
   `[Operand 1] [Operand 2] [Operator]` For e.g. `AB+`

## Recursion

Recursion is a programming technique where a function calls itself to solve a problem until base case is reached.

> If there is no condition to stop the recursive calls, the calls will run indefinitely until the stack runs out of memory which is called as stack overflow leading to segmentation fault.

## Backtracking recusion

Backtracking recursion is an algorithmic technique used to find solutions to problems by systematically exploring all possible paths or configurations. It is fundamentally a type of recursion, but the print line would be kept after the function call inside the recursive function contrary to the forward recursion approach.
