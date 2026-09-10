## Recursion

Recursion is a programming technique where a function calls itself to solve a problem until base case is reached.

> If there is no condition to stop the recursive calls, the calls will run indefinitely until the stack runs out of memory which is called as stack overflow leading to segmentation fault.

## Time Complexity

To find the time complexity of a recursive function, you need to calculate the total number of times the recursive function is called and multiply it by the time complexity of a single call (excluding the recursive step itself).

$$\text{Total Time Complexity} = \text{Number of Recursive Calls} \times \text{Time Spent per Call}$$

### Quick Reference

When recursion gets more complex (like dividing the problem in half or making multiple branches), use these patterns:

| Recursion Pattern | Example Relationship          | Time Complexity        | Common Algorithm         |
| ----------------- | ----------------------------- | ---------------------- | ------------------------ |
| Linear            | Decreases by 1 (N → N-1)      | $\mathbf{O(N)}$        | Factorial, Linear Search |
| Logarithmic       | Divided by 2 (N → N/2)        | $\mathbf{O(\log N)}$   | Binary Search            |
| Tree / Branching  | Makes 2 calls (N → 2 × (N-1)) | $\mathbf{O(2^N)}$      | Fibonacci (naive)        |
| Divide & Conquer  | 2 halves + linear merge       | $\mathbf{O(N \log N)}$ | Merge Sort, Quick Sort   |

Would you like to see how to calculate the space complexity of these recursive functions using the call stack, or analyze a trickier example like Fibonacci?

## Space Complexity

To find the space complexity of a recursive function, you must calculate the maximum amount of memory used by the call stack at any single moment during execution.

$$\text{Total Space Complexity} = \text{Maximum Stack Depth} \times \text{Memory Spent per call}$$

### Quick Reference

| Code Pattern                                       | Maximum Stack Depth                | Space Complexity     |
| -------------------------------------------------- | ---------------------------------- | -------------------- |
| Decrements by 1 ($N \rightarrow N-1$)              | $N$                                | $\mathbf{O(N)}$      |
| Divides by 2 ($N \rightarrow N/2$)                 | $\log_2 N$                         | $\mathbf{O(\log N)}$ |
| Fibonacci / Binary Tree                            | Height of the tree ($N$)           | $\mathbf{O(N)}$      |
| Creating an array of size $N$ inside a linear loop | $N$ frames $\times$ $N$ size array | $\mathbf{O(N^2)}$    |

Would you like to explore Tail Call Optimization (TCO), which allows some languages to run specific recursive functions in $O(1)$ space, or should we practice calculating both time and space on a completely new algorithm?
