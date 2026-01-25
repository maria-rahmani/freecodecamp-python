dict = {'name' : 'Maria', 'age' : 22 }
dict2 = {'name' : 'Maria'}
print(dict)
print(dict.keys())

if dict2.issubset(dict):
    print("not a subset of first dictionary");
else:
    print("A subset of first dictionary"); 