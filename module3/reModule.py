import re

name = "Maria Rahmani"
#print(re.search('m\d', name, re.IGNORECASE))
#print(re.search('me', name))

book = "It ends with us 567"
print(re.search('\d+', book))