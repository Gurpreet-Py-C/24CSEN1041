age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print(f"You are not eligible. Wait {18 - age} more year(s).")