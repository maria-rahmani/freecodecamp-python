dictionary = {
    'Name' : 'Maria Rahmani',
    'Age' : 22,
    'Course' : 'BCA'
}

print(dictionary)
# print(dictionary['Name'])
# print(dictionary.get('Age', 'Not a valid key'))
# print(dictionary.keys())
# print(dictionary.values())
#print(dictionary.items())
#print(dictionary.clear())
#print(dictionary.pop('Course'))
#print(dictionary)
#print(dictionary.popitem()) --> removes the last inserted item
dictionary.update({'Age' : 22, 'Age' : 25})
for elements in dictionary.values():
    print(elements)
print(dictionary)
