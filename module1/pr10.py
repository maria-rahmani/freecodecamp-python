list1 = ["Mike", "", "", "Emma", "Kelly", "", "Brad"]

print(list1) 

while "" in list1:
    list1.remove("")

print(list1)