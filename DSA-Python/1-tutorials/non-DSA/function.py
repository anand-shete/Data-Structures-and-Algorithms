# Python generator expressions are a compact, memory-efficient way to create iterators using a single line of code.

# They do not use extra memory like list comprehensions
square_list = [x**2 for x in range(6)]
print(square_list)
print()


square_gen = (x**2 for x in range(6))
print(next(square_gen))

for x in square_gen:
    print(x ,end=' ')
print('\n')



# check if any element meets condition
nums = [-2, -4, -1, 3, 10]
is_neg = any(x < 0 for x in nums)
print('is any element negative in nums:',is_neg)



# check if all element satisfy condition
is_neg = all(x < 0 for x in nums)
print('are all elements negative in nums:',is_neg)
print()


# transformation
raw_prices = ["$10.50", " $22.00 ", "$4.99"]
clean_prices = (float(price.strip().replace("$", "")) for price in raw_prices)
for price in clean_prices:
    print(price, end='  ')