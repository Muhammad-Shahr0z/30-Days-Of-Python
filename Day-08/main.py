# ---
# ### **Day 8: Loops (for & while)**
# - `for` loop
# - `while` loop
# - `break`, `continue`

# **Exercise:** Print numbers from 1 to 10 using a `for` loop.

li : list = [1,2,3,4,5,6,7,8,9,10]
names : str= "shahroz"


for i in li:
    print(i)


i = 0
while i < li.__len__():
    print(li[i])
    i += 1


fruits = ["mango" , "orange" , "bananas","pine"]

for i in fruits:
    if i == "bananas":
        print("Loop Break")
        break
    print(i)

i = 0
while i < len(fruits):
    if fruits[i] == "bananas":
        i += 1
        continue
    print(fruits[i])
    i += 1
    
    
    










