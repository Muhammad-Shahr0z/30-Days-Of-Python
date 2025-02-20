# ---
# ### **Day 10: Lists with Loops**
# - Loop through Lists
# - List Comprehensions (`[x for x in list if condition]`)

# **Exercise:** Print the squares of all numbers in a list.


numbers: list[int] = [1, 2, 3, 4, 5]

squares:list[int] = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]

squares.pop()
print(squares)  # Output: [1, 4, 9, 16, 25]



