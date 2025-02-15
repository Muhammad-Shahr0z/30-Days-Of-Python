# ---
# ### **Day 7: If-Else Statements & Conditions**
# - `if`, `elif`, `else`
# - Comparison Operators (`>`, `<`, `>=`, `<=`, `==`, `!=`)
# - Logical Operators (`and`, `or`, `not`)

# **Exercise:** Take age as input and check if the user is eligible to drive.


age:int = int(input("Enter Your Age To Check Your eligible For Driving "))

if age >= 18 and age < 100:
    print("You Are eligible For Driving")
elif age < 18:
    print("You Are Not eligible For Driving")
else:
    print("Invalid Age")


print(5 != 4) #output True
print(5 == 4) #output false
print(5 <= 4) #output false
print(5 > 4) #output True
print(5 < 4) #output false


if age > 18 or age == 18:
    print("Your Are eligible , True")




