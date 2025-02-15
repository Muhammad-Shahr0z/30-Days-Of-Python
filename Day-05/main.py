# ### **Day 5: Tuples & Sets**
# - Tuples (`()`) - Immutable Lists
# - Sets (`{}`) - Unique Values Only

# **Exercise:** Create a tuple with 3 fruits and a set with duplicate numbers.

fruits = ("Apple", "Banana", "Cherry")
numbers = {1, 2, 2, 3, 4, 4, 5}

print(fruits)
print(numbers)

tuples:tuple = ("Mango" , "Orange" , "Bananas" ,"Bananas") 

print(tuples.count("Bananas"))
print(tuples.index("Orange"))




# More methods of tuple
print(tuples[0])  # Accessing the first element
print(tuples[-1])  # Accessing the last element
print(tuples[1:3])  # Slicing the tuple
print(len(tuples))  # Getting the length of the tuple
print("Mango" in tuples)  # Checking if an element exists in the tuple

myset:set = {1, 2, 3, 4, 6, 5, 5, 5, 5}

print(myset, type(myset))

# More methods of set
myset.add(7)  # Adding an element to the set
print(myset)

myset.remove(3)  # Removing an element from the set
print(myset)

print(len(myset))  # Getting the length of the set

print(2 in myset)  # Checking if an element exists in the set

myset.clear()  # Clearing all elements from the set
print(myset)
