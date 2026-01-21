# Among three numbers find the greatest

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

temp = num1 

if num2 > num1:
    temp = num2
if num3 > num2:
    temp = num3

print("Greatest number is", temp)