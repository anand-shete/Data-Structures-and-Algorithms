# Time complexity

Time complexity is essentially a way to measure how the runtime of an algorithm increases as the amount of data (input size) grows.

## Notations

1. **Big O ($O$) – The Upper Bound**

- Big O notation describes the worst-case scenario. It is a guarantee that the algorithm will never take more time than this bound.
- Example: For a linear search in an array of size $n$, the worst case is the item being at the very end. This is $O(n)$.

2. **Big Omega ($\Omega $) – The Lower Bound**

- Big Omega describes the best-case scenario. It represents the minimum time an algorithm will take for a given input size.
- Example: For that same linear search, the best case is finding the item at the very first position, which is $\Omega(1)$.

3. **Big Theta ($\Theta $) – The Tight Bound**

- Big Theta is the most precise. It defines the exact growth rate by acting as both an upper and lower bound.
- An algorithm is $\Theta(f(n))$ only if it is both $O(f(n))$ and $\Omega(f(n))$.
- Example: Merge Sort consistently takes the same amount of effort regardless of how sorted the data is, so it is defined as $\Theta(n \log n)$

### Examples

In general, `estimate total operations as the input size n grows`

1. O(1) – Constant Time

- E.g. Checking if a number is even or odd. It doesn't matter if the number is `2` or `2,000,000,000,000`; the computer only looks at the last digit.

2. $O(n)$ – Linear Time

- Searching a name in an unsorted list. You might have to look at every single name from start to finish.

When you're dealing with 10 items, the difference between $O(n)$ and $O(n^2)$ is negligible (10 vs 100 operations). But when you're dealing with 1 million items, $O(n)$ is a split second, while $O(n^2)$ could take days to finish

## Time Complexity order

| Time Complexity | Term                  |
| --------------- | --------------------- |
| $O(1)$          | Constant              |
| $O(\log n)$     | Logarithmic           |
| $O(\sqrt{n})$   | Square root           |
| $O(n)$          | Linear                |
| $O(n \log n)$   | Linearithmic          |
| $O(n\sqrt{n})$  | $n$ times square root |
| $O(n^2)$        | Quadratic             |
| $O(n^3)$        | Cubic                 |
| $O(2^n)$        | Exponential           |
| $O(n!)$         | Factorial             |
| $O(n^n)$        | Super-exponential     |

> Logarithmic time complexity $O(\log n)$ means that the input gets divided (shrunk) by a constant factor (usually 2 or 10) in every step.

## Amortized Time Complexity

- Amortized time complexity is used when an algorithm has one very _expensive_ operation that happens rarely, while the rest of the operations are very cheap.
- eg. While adding elements to vector, it usually takes $O(1)$ time because there are empty slots. But what happens when the vector is full?  
  _Expensive step_: The computer has to create a new, bigger array (usually double the size) and copy every single old item into the new one. This single step is $O(n)$.  
  _Cheap step_: Because the array just doubled in size, you now have a ton of empty space. The next many adds will be back to $O(1)$. Hence, its called Ammortized $O(n)$ time complexity

## Space Complexity

Refers to the `memory space that a code uses while being executed`

- **Auxillary space**: Exclude the input and output space
- **Total space complexity**: Input space + Output space + Auxillary space

| Operation / Data Type | Space Complexity  | Notes                                  |
| --------------------- | ----------------- | -------------------------------------- |
| int, char, bool       | $O(1)$            | Fixed amount of memory                 |
| vector<int> v(n)      | $O(n)$            | Stores $n$ elements in memory          |
| unordered_map         | $O(n)$            | Stores $n$ key-value pairs             |
| Recursion             | $O(\text{depth})$ | Each call adds a frame to the stack    |
| Merge Sort            | $O(n)$            | Requires a temporary array to merge    |
| In-place sorting      | $O(1)$            | Uses the original array (eg. Heapsort) |

## Calculate Range of data types

$$
sizeof(int) = 4 \\
4\ bytes = 4\times 8 = 32\ bits \\
2^{32}\ in\ case\ of\ unsigned\ int \\
-2^{31}\ to\ 2^{31} - 1\ in\ case\ of\ signed\ bit
$$

> **Windows Rule**: On Windows (both 32-bit and 64-bit), $int$ and $long$ are identical (4 bytes) means $-2^{31}$ to $2^{31}-1$
> **Linux/macOS Rule**: On 64-bit Linux and macOS, $int$ is $4\ bytes$, but long scales to $8\ bytes$. This expands the $long$ range significantly to roughly $\pm 9 \times 10^{18}$.

## Utilize constraints

**$10^8$ Rule**: Most online judges (LeetCode, Codeforces, or GFG) have a `1 second runtime limit`, which roughly equates to $10^{8}$ operations.

| Input Size ($n$)       | Complexity            |
| ---------------------- | --------------------- |
| $n > 10^7$             | $O(\log n)$ or $O(1)$ |
| $n \leq 10^6$          | $O(n)$                |
| $n \leq 10^5$          | $O(n \log n)$         |
| $n \leq 5 \times 10^3$ | $O(n^2)$              |
| $n \leq 500$           | $O(n^3)$              |
| $n \leq 20$            | $O(2^n)$              |
| $n \leq 10$            | $O(n!)$               |

> If input size $n$ is $10^5$ and you use an $O(n^2)$ algorithm, you're doing $10^{10}$ operations. A standard CPU will take roughly 100 seconds to finish that. You will get a TLE (Time Limit Exceeded).

## Data Structures and Algorithms Mantra

1. Never spend `> 30 mins` on a problem thinking about solution.
2. Understand, Memorize pattern and move on.
3. Do not focus on acheiving `100%` Runtime on Leetcode.
