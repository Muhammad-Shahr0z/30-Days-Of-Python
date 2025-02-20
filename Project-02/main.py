import questionary

# First Number Selection
a = int(input("Enter Your First Digit "))

# Second Number Selection
b = int(input("Enter Your Second Digit "))

# Operator Selection
operator = questionary.select(
    "Select an operator:",
    choices=["+", "-", "*", "/"]
).ask()


# Function for Calculation
def calculation(a: int, b: int):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b if b != 0 else "Error: Division by zero is not allowed."


# Print Result
print(f"\nResult: {a} {operator} {b} = {calculation(a, b)}")
