import random
def roll_die(sides):
    return random.randint(1, sides)
sides = int(input("Enter number of sides on the die: "))
print("You rolled:", roll_die(sides))
