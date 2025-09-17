#The Dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key-value pair.

dict = {'name': 'vasu', 'age': 20}
print(type(dict))

print("dict['name'] = ", dict['name'])
print("dict['key'] = ", dict['key'])  #KeyError: 'key'
print("dict['age'] = ", dict['age'])   