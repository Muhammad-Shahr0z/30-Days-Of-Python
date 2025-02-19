# ---
# ### **Day 9: Functions & Arguments**
# - Defining Functions (`def function_name():`)
# - Parameters & Arguments
# - Return Statement

# **Exercise:** Create a function that returns the sum of two numbers.

def greet():
    print(f"Hello, Shahroz")

greet()


def greetWithName(name:str):
    print(f"Hello , {name}")

greetWithName("Muhammad Shahroz")


def add(a:int , b:int):
    return a+b

print(add(25 ,25))