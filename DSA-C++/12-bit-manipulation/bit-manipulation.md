### Decimal to Binary

1. Divide number by $2$
2. Keep diving until quotient reaches $0$
3. Write numbers from bottom (Least Significant Bit) to top (Most Significant Bit)

$10_{10} = 1010$

### Binary to Decimal

1. Use $2^{n}$ where $n$ is the current index from $0$ in right to left
2. Multiply each $2^{n}$ with current binary number

$1101_2$ = $13_{10}$

### Representing +ve numbers in C++

Computers use binary because their fundamental building blocks are transistors, which have two states:

1. ON respresents $1$
2. OFF represents $0$

All data types are translated into binary for processing by the compiler.
So, a decimal value of $5$ is represented as $00000000000000000000000000000101$ (32 bits or 4 bytes) in memory. In this representation leftmost bit $0$ is called as the **Most Significant Bit** (or MSB) and rightmost bit $1$ is called as the **Least Significant bit**.

> If number is not declared as `unsigned`, the MSB bit is the **sign bit**

### Representing -ve numbers in C++

#### 1's complement

1's complement is a method used to represent **signed numbers**. Steps involved

1. Flip each bit

Example
$5$ is represented as $00000101$ in 8-bit notation.
1's complement is $11111010$.

Hence, computer stores $-5$ as $11111010$ in 1's complement.

#### 1's complement drawbacks

While one's complement is simpler to obtain (just invert the bits), it has two primary disadvantages that make it less practical for general-purpose computing compared to two's complement:

1. **Dual representation of zero**
   In one's complement, both positive zero $0000$ and negative zero $1111$ exist.
2. **End-around carry in addition**
   When performing addition with one's complement, if a carry is generated from the most significant bit (MSB), it needs to be added back to the least significant bit (LSB) of the sum, a process called end-around carry. This extra step makes the arithmetic hardware more complex and less efficient.

#### 2's complement

Two’s complement is inherently a system designed to represent **signed integers**. Steps involved are

1. Take the 1's complement
2. Add $1$ to the 1's complement

Example
$6$ is represented as $00000110$ in 8 bit notation
1's complement is $11111001$
Add 1 to 1's complement is $11111010$ which is $-6$

Hence, $6$ is represented as $11111010$ in 2's complement

> Leftmost bit is sign bit, which tells us if the decimal equivalent is +ve ($0$ in leftmost bit) or -ve ($1$ in in leftmost bit)

> All modern hardware use 2's complement to store **signed integers**

### Operators

#### AND Operator

Both T, then T

#### OR Operator

Both F, then F

#### XOR Operator

Both same, then $0$

### NOT Operator

Invert Bits

> To print the output, computer converts binary to decimal no. If sign bit is $1$, convert to 2's complement

#### Right Shift Operator

Shift bits to right and push given no. of bits off the cliff
**$num >> k = \frac{num}{2^{k}}$** for positive numbers

> For negative signed integers, C++ performs an arithmetic right shift, which fills the vacant left positions with 1s instead of 0s to preserve the negative sign.

#### Left Shift Operator

Shift bits to left and push given no. of bits off the cliff
**$num << k = {num}\times2^{k}$**

### Tricks

- Largest number that can be store in binary signed integer representation is $2^{31}-1$ represented as $011111....$
- Smallest number which can be stored in binary singed integer representation is $-2^{31}$ represented as $10000.....$

- Swap Two Numbers Without a Third Variable
  A = A ^ B
  B = A ^ B
  A = A ^ B

- Check if the i-th Bit is Set
  (1 << i) & num → set if result ≠ 0
  (num >> i) & 1 → set if result ≠ 0

- Set the i-th Bit
  num | (1 << i)

- Clear the i-th Bit
  num & ~(1 << i)

- Toggle the i-th Bit
  num ^ (1 << i)
