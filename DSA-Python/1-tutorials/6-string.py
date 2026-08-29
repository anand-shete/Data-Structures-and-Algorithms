# Strings are Immutable sequences of unicode characters


# create strings
a = 'Anand'
b = "Anand"
c = '''Anand'''


# access character - O(1)
print("character at index 0 from start:", a[0])
print("indexing starts from -1 in end:", a[-1])


# convert to ascii - O(1)
print("char 'A' value in ascii:", ord('A'))
print("ascii value of 65 in char:", chr(65))


# length of string - O(1)
s = "python"
print("length of string python:", len(s))


# empty string - O(1)
s= ""
print("is s empty:", not s)
print()


# slice string - s[start:stop:step] - O(k)
# slice always creates a copy since strings are immutable
# if step > 0, start default: 0, stop default: len(string) else stop=end-1
# if step < 0, start default: -1, stop default: -(len(string)+1) else stop=end+1
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
print("all chars lowercase:", name.islower())
print("all chars uppercase:", name.isupper())
print("all chars are alphanumeric:", name.isalnum())
print("all chars are alphabets:", name.isalpha())
print("all chars are digits:", name.isdigit())
print("remove whitespace:",name.strip())
print()


# index of first occurrence - O(n.m)
a = "banana"
print("index of first occurrence 'na':", a.find("na"))
print("index of first occurrence 'a':", a.find("a"))
print("index which does not exists:", a.find("absent"))
print()


# count number of occurrences - O(n)
print("number of occurrences of 'a':", a.count("a"))
print()


# string concatenation - O(n1 + n2)
print("concat strings:", 'Hello ' + 'World')
print()


# repeat string - O(n * k)
a = "hello "
print("repeat string:", a * 3)
print()


# lexicographic comparison - O(min(n1, n2)) but O(1) if lengths differ or first character mismatch
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