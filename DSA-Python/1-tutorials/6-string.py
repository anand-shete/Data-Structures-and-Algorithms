# Strings are Immutable sequences of unicode characters


# create strings
a = 'Anand'
b = "Anand"
c = '''Anand'''


# access character - O(1)
print("indexing starts at 0 from start:", a[0])
print("indexing starts at -1 from end:", a[-1])
print()


# convert to ascii - O(1)
print("char 'A' value in ascii:", ord('A'))
print("ascii value of 65 in char:", chr(65))


# conversion between int and str - O(n²) where n is length of string
# python limits int and str conversions to maximum 4300 digits (default)
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


# slice string - s[start:stop:step] - O(k) where k is length of sliced string
# slice always creates a copy since strings are immutable
# if step > 0, start default: 0, stop default: len(string) else stop-1
# if step < 0, start default: -1, stop default: -len(string)-1 else stop+1
a = "0123456789"
print("entire copy:", a[::])
print("slice from [0,7):", a[:7])
print("slice from idx 7 to end:", a[7:])
print("slice from idx [2, 7):", a[2:7])
print("slice from idx -4 to end:", a[-4:])
print("print every 2nd char:", a[::2])
print("slice every 2nd char from [0,7):", a[0:7:2])
print("start and stop at defaults direction -ve:", a[::-1])
print("start from idx 2 step -1:", a[2:-11:-1])
print("same str above chained slice:", a[::-1][-3:])
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