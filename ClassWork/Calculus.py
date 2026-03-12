import sympy as sp

# Define symbol
x = sp.symbols('x')

print("=== Python Calculus Solver ===")
print("Example input: x**2 + 3*x + 5")
print()

# Get expression
expr_input = input("Enter the function: ")

try:
    expr = sp.sympify(expr_input)

    # Derivative
    derivative = sp.diff(expr, x)

    # Indefinite integral
    integral = sp.integrate(expr, x)

    print("\nFunction:")
    print(expr)

    print("\nDerivative:")
    print(derivative)

    print("\nIntegral:")
    print(integral, "+ C")

except Exception as e:
    print("Invalid expression:", e)