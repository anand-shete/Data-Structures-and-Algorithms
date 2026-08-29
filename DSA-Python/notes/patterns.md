# Leetcode Patterns

[Core Leetcode patterns and problems](https://leetcode.com/discuss/post/8330844/all-leetcode-patterns-that-you-need-to-k-smrv/)

## Concepts

**Subarray** : Contigious part of an array
**Subsequence** : Non-contigious part of an array but preserve order
**Lower Bound of x**: First element `>=x`
**Upper Bound of x**: First element `>x`
**Permutation of n**: Contains all integers from 1 to n exactly once

> Total possible substrings are $\frac{n(n+1)}{2}$
> Total possible subsequences for a string are $2^n$

#### Range vs slice

- `range()` deals with integers.

- Slicing deals with sequence indices, where negative values are translated to positions from the end before the slice is evaluated.

### Popular Algorithms

| Algorithm           | Approach                            | Example Problems                       |
| ------------------- | ----------------------------------- | -------------------------------------- |
| Kandane             | Maximize running sum containing -ve | `Max subarray`, `Max product subarray` |
| Dutch National Flag | Use 3 pointers to sort 3 elements   | `Sort 0,1 and 2`                       |
| Boyer Moore Voting  | Element present more than n/2 times | `Majority element`                     |

## Memorize Patterns

### Arrays

1. Use `unordered_map` to store frequency or `vector  <int>` if constrains are less.
2. Use 2 pointers for sorted arrays. Even if unsorted, `sort()` can give `n.log(n)` time complexity.
3. For subarrays, sum till current (prefix sum) can be stored in hashmap

### Binary Search

- Data must be sorted in predictable order
- Search space must be **monotonic** in nature (strict increase or strict decrease)
- Watch for phrases like `maximum of minimum`, `minimum of maximum`, etc.

1. A rotated sorted array will remain sorted even after its divided into 2 parts.

### Strings

1. Use `vector` instead of a hashing to store frequency if constraints low.
2. To covert char `x` to int, do `x - '0'`
3. Use `s1 += s2` than `s1 = s1 + s1` (slow)

### Sliding window

- Question demands substring or subarray in a arrays,
- All elements are **positive**
- Monotonic nature (strictly increasing or decreasing)

1. For sliding window frequncy problems, the frequency tracks no. of elements inside the sliding window
2. `count += right-left+1` will give all possible subarrays ending at right

### Prefix Sum

- Negative values are being used
- Track current sum that sums/divides till k

1. Current sum = k + Previous sum

### Array notes

1. Use `pass by value` with vectors
2. If problem constraints are low(`0 < nums[i] <= 100`), use vector to store freq instead of hashmap.
3. C++ automatically converts `int` (smaller data type) to `long long` internally while storing in map,set, comparing, etc.
4. To get a positive mathematically modulo in c++, use formula `(a % b + b) % b`

### Linked List

1. Last node points to `nullptr` in LL. You cannot read val from `nullptr`
2. Since we like C++, manually delete memory leaks in LL problems
3. Mostly two pointers can be used to solve LL.

### Recursion

- For recursive algorithms, time complexity calculation is standard
- Space complexity usually comes from the **call stack depth** w.r.t. input size
- Space complexity = memory per frame \* call stack depth.

### Bit masking

- Check if bit set: `mask & (1 << i)`
- Turn a bit ON: `mask | (1 << i)`
- Turn a bit OFF: `mask & ~(1 << i)`
