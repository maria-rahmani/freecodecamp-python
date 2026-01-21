# Lists
# Dynamic, heterogeneous, referential arrays

l = [0, 5, 10, 15, 20, 25, 30]

# len(l) -> Returns length of l

# Indexing: Access a single item. Supports positive and negative indexing
# Slicing: Access a section of the List. Can take upto 3 arguments (start, end, jump)
# print(l[1:-2:2])

# del l[3] -> Deletes a single item
# del l -> Deletes the list

# +: Concatenates 2 lists
# *: Duplicates the list n times

# in: Membership operator which checks if an object is present in the list
# not in: not of in operator
# print(10 not in l)

def square(x):
    return x * x

l3 = [1, 4, 2, 3, 7, 0]

l3.append(10)
l3.extend(l)
l3.insert(2, 500)
# l3.remove(0)
l3.pop()
# l3.clear()
# l3.sort(reverse=True)

l4 = [1, 2, -3, 4, -2, 1, 0]

l4.sort(key=square, reverse=True)

l3.reverse()

l5 = l3.copy()

# print(l5)

def factorial(n):
    if n == 0: return 1
    ans = 1.0
    for i in range(1, n + 1):
        ans *= i
    return ans

x = 1

lst = [x**i / factorial(i) for i in range(100)]


print(sum(lst))

l6 = [1, 2, 3, 4, 5]

