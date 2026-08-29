# A dictionary is an ordered, mutable collection of data values used to store data values in key:value pairs, where each key must be unique and hashable (immutable).
# Python hashmap preserves insertion order


# create dict
umap = {
    11:34,
    23:45,
    34:92,
    57:99
}
print(umap)
print()


# access values - O(1)
print("value of 11:", umap.get(11))
print("return default value if key not found:", umap.get(99, 0))
print("raise KeyError if key not found:", umap[23])
print()


# check if key exists  - O(1)
print('check key 34 exists:', 34 in umap)
print()


# [] adds key-value pair or update existing - O(1)
umap[13] = 51
umap[34] = 56
print(umap)
print()


# length of hashmap - O(1)
print('length of hashmap:',len(umap))
print()


# remove pair from hashmap - O(1)
# del[key] and pop(key) raise KeyError if key not exists
del umap[34]
print('delete key name:',umap)
print('delete and return value of 13:', umap.pop(13))
print()


# remove recently inserted pair - O(1)
# popitem raise error if dictory is empty
print("delete and return recent inserted:", umap.popitem())
print('\n')

# clear entire map - O(n)
# print('clear map:', umap.clear())


# view objects of all keys - O(1)
# print(umap)
print("keys of umap:", umap.keys())
print()


# view object of all values - O(1)
print("values of umap:", umap.values())
print()


# view object of all key-value pairs as tuple - O(1)
print("key-value pairs:", umap.items())
print('\n')


# merge 2 dictionary - O(m)
dict2 = { 1:2, 3:4 }
umap.update(dict2)
print("merge two dictionary:", umap)
print('\n')



# iterate dictionary - O(n)
for k,v in umap.items():
    print(f'{k}=>{v}')