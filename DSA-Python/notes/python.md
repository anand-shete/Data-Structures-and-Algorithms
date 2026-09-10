### Python Large Integer Complexity (On 64-bit Systems)

Within $(-2^{30}, 2^{30})$ range, all basic arithmetic is $O(1)$ constant time (handled directly by CPU).

If an integer value goes outside $(-2^{30}, 2^{30})$, Python stops using hardware-level math and switches to arbitrary-precision array math where

- **Addition / Subtraction:** $O(n)$
- **Multiplication / Division:** $O(n^2)$

where $n$ is number of **30-bit digits** (chunks) required.

### Memory allocation

#### Immutable type

Variables are just labels and values are objects in memory.

```py
test = 1
```

Python creates an integer object 1 at a specific memory address (eg.`100`). It places the test label on it.

```py
test = 2
```

Python cannot change the value inside Address 100 because **integers are immutable**. Instead, Python creates a completely new integer object `2` at a different memory address (eg.`200`). It then rips the test label off the `1` object and sticks it onto the `2` object.

> The object `1` never changed. It still exists in memory exactly as it was until the garbage collector clears it out.

#### Mutable type

When you modify a list, the memory address stays exactly the same

```py
my_list = [1,2,3]
print(id(my_list))  # Memory address: 139782605605696

my_list.append(4)
print(my_list)
print(id(my_list)) # Memory adderss: 139782605605696
```

With mutable type like list, Python goes to the existing memory address `139782605605696` and alter its contents. The object itself was mutated.

### Range vs slice

- `range()` deals with integers.

- Slicing deals with sequence indices, where negative values are translated to positions from the end before the slice is evaluated.