### **Day 3: Strings & String Methods**
# - String Concatenation
# - String Methods (`upper()`, `lower()`, `title()`, `strip()`, `replace()`)
# - String Formatting (`f"Hello {name}"`)

# **Exercise:** Take a user name input and print it in uppercase & lowercase.


my_name:str = "MuhamMad"
last_Name:str = "ShAhroZ"

Full_Name = my_name +" "+ last_Name ; 

print(Full_Name)

my_name:str = "MuHammAd ShAHroZ"

print(my_name.capitalize())
print(my_name.upper())
print(my_name.lower())
print(my_name.title())


print(f"My Name is {my_name.title()}")


name:str = input("Enter Your Name ")

print(name.lower() , name.upper())


text = "   Hello, World!    "
print(text.strip())


# strings are immutable 
# replace 
print(text.replace("World" , Full_Name))









