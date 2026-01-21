# Print a number table till 10


num = int(input("Enter the number for a table: "))

i = 1
print("Using while loop")
while i <= 10:
    print(num,"x",i,"=",num * i)
    i += 1

print("Using for loop")
for i in range(1, 11):
    print(num,"x",i,"=",num * i)