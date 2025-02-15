from box import Box
# ---
# ### **Day 6: Dictionaries & Key-Value Pairs**
# - Dictionaries (`{key: value}`)
# - Dictionary Methods (`keys()`, `values()`, `items()`, `get()`)

# **Exercise:** Create a dictionary with `name`, `age`, and `city` keys.


myDic =Box({ 
    "name": "Muhammad Shahroz",
    "age": 26,
    "city": "Karachi"
})




print(myDic.name)  # Output: Muhammad Shahroz
print(myDic.age)   # Output: 26
print(myDic.city)   # Output:Karxchi



print(myDic.values())
print(myDic.items())
print(myDic.get("name"))
print(myDic.keys())
