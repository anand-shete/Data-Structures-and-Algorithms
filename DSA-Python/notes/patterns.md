## References

[Core Leetcode patterns and problems](https://leetcode.com/discuss/post/8330844/all-leetcode-patterns-that-you-need-to-k-smrv/)

## Concepts

**Subarray** : Contigious part of an array
**Subsequence** : Non-contigious part of an array but preserve order
**Lower Bound of x**: First element `>=x`
**Upper Bound of x**: First element `>x`
**Permutation of n**: Contains all integers from 1 to n exactly once

> Total possible substrings are $\frac{n(n+1)}{2}$
> Total possible subsequences for a string are $2^n$

## Algorithms

| Algorithm           | Approach                            | Example Problems                       |
| ------------------- | ----------------------------------- | -------------------------------------- |
| Kandane             | Maximize running sum containing -ve | `Max subarray`, `Max product subarray` |
| Dutch National Flag | Use 3 pointers to sort 3 elements   | `Sort 0,1 and 2`                       |
| Boyer Moore Voting  | Element present more than n/2 times | `Majority element`                     |

# Leetcode Patterns

Here are most popular leetcode patterns I experienced

## \* pattern question

- For any pattern, break it into smaller parts and identify the number of spaces, and the number of stars/numbers only and design a logic
- Think about the spaces and think about how will you print them.
- Use one-based indexing because it is simple to print i stars on the i-th column (`1` to `n+1`)

## Arrays

1. Use `dict` to store frequency of elements, `list` if constrains are less.
2. Use 2 pointers for sorted arrays. Converting to sorted can give `n.log(n)` time complexity.
3. For subarrays, sum till current element (prefix sum) can be stored in hashmap

## Binary Search

- Checking an element must split space into two clean halves (all pass then all fail or reverse)
- Watch for phrases like `maximum of minimum`, `minimum of maximum`, etc.

> A rotated sorted array will remain sorted even after its divided into 2 parts.

## Strings

1. Use `list` instead of a hashing to store frequency if constraints low.
2. For fast concatenation, append to list and use `"".join()` and avoid `+=` in loop

## Sliding window

- Question demands substring or subarray in a array/string
- Only **non-negative numbers**
- The tracked quantity (sum, count, distinct-elements, etc.) must move monotonically as the window expands/shrinks — not the array values themselves

1. For sliding window frequncy problems, the frequency tracks no. of elements inside the sliding window
2. `count += right-left+1` will give all possible subarrays ending at right

### A note on `at_most(k) - at_most(k-1)`

Plain sliding window works because **"at most K" is monotonic** — grow the window, the count-of-distinct-things never goes down; shrink it, never goes up. That monotonicity is what lets you safely move left/right pointers and trust the answer.

Exactly K has no such monotonicity. Hence to solve problems like find **exactly K elements** that satisfy a condition, we use

**Exact count = (count of windows with ≤ K) − (count of windows with ≤ K-1)**

e.g. How many people are 25 y.o. = (count of people ≤ 25) - (count of people ≤ 24)

## Prefix Sum

- Negative values are being used
- Track current sum that sums/divides till k

1. Current sum = k + Previous sum

## Linked List

1. Last node points to `None` in LL. You cannot read val from `None`
2. Mostly two pointers can be used to solve LL.

## Recursion

- For recursive algorithms, time complexity calculation is standard
- Space complexity usually comes from the **call stack depth** w.r.t. input size
- Space complexity = memory per frame x call stack depth.

> Python's default recursion limit (~1000) can throw `RecursionError` on deep recursion even when logic is correct — use `sys.setrecursionlimit()` or convert to iterative if needed

## Bit masking

- Check if bit set: `mask & (1 << i)`
- Turn a bit ON: `mask | (1 << i)`
- Turn a bit OFF: `mask & ~(1 << i)`
