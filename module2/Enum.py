# If we want to keep track of the index of each element of the list, we do 
x = [8, 3, 2, 9, 4]
y = ["I", "Love", "You", "Munnu", "Gunnu"]
index = 0

for i in x:
    print(f'Index {index} has element {i}')
    index += 1

# With Enumerate function
print(list(enumerate(x)))
print(list(enumerate(x, 5)))

# Using Zip function
print(list(zip(x, y)))

# Another way to use Zip function
for Id, name in zip(x, y):
    print(Id, "->", name)