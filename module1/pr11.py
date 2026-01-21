list1 = [1, 2, 2, 3, 1, 4, 5, 4]
print(list1)

for i in list1: 
    while list1.count(i) > 1: list1.remove(i)

print(list1)