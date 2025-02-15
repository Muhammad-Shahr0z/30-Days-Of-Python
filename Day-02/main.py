### **Day 2: Basic Operators & Input**
# - Arithmetic Operators (`+`, `-`, `*`, `/`, `%`)
# - User Input (`input()`)
# - Type Conversion (`int()`, `float()`, `str()`)

# **Exercise:** Take two numbers as input and print their sum and product.


num1:int = int(input("Enter Your First Number " ))
num2:int = int(input("Enter Your Second Number " ))

result:int = num1 + num2
result2:int = num1 - num2
result3:int = num1 * num2
result4:int = num1 / num2

print(f""" 

Add {result}
Sub {result2}
Mul {result3}
Div {result4}

""")




string:str = str(result)
number:int = int(string)


print(f'{string , type(string)} , {number , type(number)}')
