# Arithmetic Operators
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Floor Division (//)
# Modulo (%)
# Exponentiation (**)
print("4/3 =", 4/3)
print("4//3 =", 4//3)
print("2**3 =", 2**3)
print()



# Assignment operators
# Addition assignment (+=)
# Subtraction assignment (-=)
# Multiplication assignment (*=)
# Division assignment (/=)
# Floor Division assignment (//=)
# Modulo assignment (%=)
# Exponentiation assignment(**=)



# Comparison Operators
# Equal to (==)
# Not Equal to (!=)
# Greater than (>)
# Less than (<)
# Greater than or Equal to (>=)
# Less than or Equal to (<=)



# Logical Operators
# AND (and): Both True, then True. If first condition is False, and does not check the second condition
# OR (or): Both False, then False. If first condition is True, or will not check the second condition
# NOT (not): Negate the operand
print(True and True)
print(False or False)
print(not True)
print()



# Bitwise Operators
# Bitwise AND (&): Both bits at same position 1, then 1
print('8 & 1:', 8 & 1)

# Bitwise OR (|): Both bits at same position 0, then 0
print('8 | 1:', 8 | 1)

# Bitwise XOR (^) or Exclusive OR: Both bits same, then 0
print('8 ^ 0:', 8 ^ 0)

# Bitwise NOT (~) operator flips every bit in the operand’s binary representation. For unsigned integers, this simply inverts the bits. For signed integers (two’s complement), it produces the value -(x + 1).
print('~5:', ~5)
print('~-6:', ~-6)

# Bitwise Left shift (<<) shifts bits to left by n places and add zeroes
# Left shift means multiply by 2^n where n is numver of bits shifted
print('3 << 4:', 3 << 4)
print('-3 << 1:', -3 << 2)

# Bitwise Right shift (>>) operator shifts the bits to the right, and any bits that overflow are discarded
# Right shift means integer floor division by powers of 2:  floor( x/(2^n) ) where n is number of bit to shift
print('3 >> 1:', 3 >> 1)
print()



# Ternary operator
result = 100 if False else 4
print(result)
print()




# Membership Operators
# In (in): Checks if a value exists inside a collection (Array, Set, Hash Map)
str = "Harry"
print("end in friend:", "end" in "friend")

# Not In (not in): Checks if an element is not present in a collection.
print("u not in love:", "u" not in "love")
print()




# Identity Operators
# Is (is): Checks if two variables point to the exact same memory address
# Is Not (is not): Oppsite if 'is' operator
x = 34
y = 34
print(x is y)
print()



# Walrus operator (:=) assigns the value and immediately passes that value forward
ptr = 0
while (ptr := ptr+1) <= 5:
    print(ptr)