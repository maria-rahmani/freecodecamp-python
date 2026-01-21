# Calculate compound interest A = P(1 + r/n)^(nt)

P = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
n = float(input("Enter number of time amount is compounded annually: "))
t = float(input("Enter years: "))

A = P * (1 + r/n) ** (n * t)

print("Compound Interest:", A)