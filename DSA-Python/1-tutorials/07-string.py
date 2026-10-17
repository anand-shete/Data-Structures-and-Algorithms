# Strings are Immutable sequences of unicode characters


# create strings
a = 'Anand'
b = "Anand"
c = '''Anand'''


# access character - O(1)
print("char at index 0:", a[0])
print("python adds len(string) to -ve indexes:", a[-1])
print()


# convert to ascii - O(1)
print("char 'A' value in ascii:", ord("A"))
print("ascii value of 65 in char:", chr(65))


# conversion between int and str - O(n²) where n is length of string
print('convert 34 to string:',str(34))
print('convert string to int:',int("34"))
print()


# length of string - O(1)
s = "python"
print("length of string python:", len(s))


# empty string - O(1)
s= ""
print("is s empty:", not s)
print()


# s[start:stop:step] - O(k) where k is length of sliced string (slice always create copy)
# if step > 0, start defaults to 0,     stop defaults to len(string)
# if step < 0, start defaults to -1,    stop defaults to -len(string)-1
# start and given index and take every `step`-th char, exclude stop
a = "0123456789"
print("entire copy:", a[::])
print("slice from [0,7):", a[:7])
print("slice from idx 7 to end:", a[7:])
print("slice from idx 7 to end:", a[7:10])
print("slice from idx 7 to end (wrong becuase walk not possible):", a[7:0])
print("slice from idx [2, 7):", a[2:7])
print("slice from idx -4 to end:", a[-4:])
print("print every 2nd char:", a[::2])
print("slice every 2nd char from [0,7):", a[0:7:2])
print("start and stop at defaults direction -ve:", a[::-1])
print("start from idx 2 step -1:", a[2:-11:-1])
print("same str above chained slice:", a[::-1][-3:])
print()


# sort string
# python strings are immutable, so avoid using += in loops for string concat
s = "   "
print("standard sort places upercase before lowercase:","".join(sorted(s)))
print("sort regardless of case:", "".join(sorted(s, key=str.lower)))
print("sort but place lowercase before uppercase:", "".join(sorted(s, key=lambda ch:ch.isupper())))
print()


# split string - O(n)
a = "  Hello    World   "
print("default split:", a.split())
print("split by space:", a.split(' '))
print('\n')


# string functions - O(n)
name = "   Anand    "
print("convert to uppercase:", name.upper())
print("convert to lowercase:", name.lower())
print("are all chars lowercase:", name.islower())
print("are all chars uppercase:", name.isupper())
print("are all chars are alphanumeric:", name.isalnum())
print("are all chars are alphabets:", name.isalpha())
print("are all chars are digits:", name.isdigit())
print("trim whitespace:",name.strip())
print()


# index of first occurrence - O(len(str1).len(str2))
a = "banana"
print("index of first occurrence 'na':", a.find("na"))
print("index of first occurrence 'a':", a.find("a"))
print("index which does not exists:", a.find("absent"))
print()


# count number of occurrences - O(len(str1))
print("number of occurrences of 'a':", a.count("a"))
print()


# string concatenation - O(len(str1) + len(str2))
print("concat strings:", 'Hello ' + 'World')
print()


# repeat string - O(len(str) * k)
a = "hello "
print("repeat string:", a * 3)
print()


# lexicographic comparison - O(min(len(str1), len(str2))) but O(1) if lengths differ or first character mismatch
s1 = "apple"
s2 = "banana"
print('s1 == s2', s1 == s2)
print('s1 != s2', s1 != s2)
print('s1 > s2', s1 > s2)
print('s1 < s2', s1 < s2)
print()


# f-Strings (Python 3.6+)
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old")   