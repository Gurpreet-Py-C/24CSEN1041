a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
	print(f"{a} is larger")
elif b > a:
	print(f"{b} is larger")
else:
	print("Both are equal")