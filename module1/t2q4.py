# Fibonacci upto n terms

num = int(input("Enter number of terms: "))
currentTerm = 0
nextTerm = 1

print("Fibonacci upto",num,"terms:")
for i in range(num):
    temp = currentTerm
    currentTerm = nextTerm
    nextTerm = temp + currentTerm
    print(temp)