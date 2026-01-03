num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation: +, -, *, /")
operation = input("Enter choice: ")
if operation == '+':
	result = num1 + num2
elif operation == '-':
	result = num1 - num2
elif operation == '*':
	result = num1 * num2
elif operation == '/':
	if num2 != 0:
		result = num1 / num2
		else:
		result = "Invalid Operation"
print(f"Result: {result}")