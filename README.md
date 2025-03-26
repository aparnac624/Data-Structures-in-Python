# Data-Structures-in-Python
This repository contains Python exercises that focus on basic data structures: Lists, Dictionaries, Sets, and Tuples. The exercises cover common operations on these data structures.

Table of Contents
    1. List Operations
    2. Dictionary Operations
    3. Set Operations
    4. Tuple Operations


1. List Operations
--------------------------------------------------------
Q1: Create a list of 5 random numbers and print the list.
In this exercise, we simply created a list from range 1 to 10 and printed the original list

numbers = list(range(1,11))
print("Original list: ",numbers)

Q2: Insert 3 new values to the list and print the updated list.
We use the append() method to add 3 new numbers 11,12 and 13 to the list.

numbers.append(11)
numbers.append(12)
numbers.append(13)
print("Updated list: ",numbers)

Q3: Use a for loop to print each element in the list.
We use a for loop to iterate through the list and print each number.

print("Elements in list are below: ")
for i in numbers:
    print(i)

2. Dictionary Operations
------------------------------------------------------------------
Q1: Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
We create a dictionary with the provided key-value pairs.

dict1 = {'name': 'John', 'age':25, 'address':'New York'}
print("Original dictionary: ",dict1)

Q2: Add a new key-value pair to the dictionary with key 'phone' and value '1234567890'.
We add a new entry to the dictionary.

dict1['phone'] = '1234567890'
print("Updated dictionary: ",dict1)

3. Set Operations
---------------------------------------------------------------
Q1: Create a set with values 1, 2, 3, 4, and 5.
We create a set using curly braces {}.

set1 = {1,2,3,4,5}
print("Original set: ",set1)

Q2: Add the value 6 to the set.
We use the add() method to add a new value to the set.

set1.add(6)
print("Updated set after adding value 6: ",set1)

Q3: Remove the value 3 from the set.
We use the remove() method to delete a value from the set.

set1.remove(3)
print("Updated set after removing value 3: ",set1)

4. Tuple Operations
--------------------------------------------------------------------
Q1: Create a tuple with values 1, 2, 3, and 4.
We define a tuple using parentheses ().

tuple1 = (1,2,3,4)
print("Original tuple: ",tuple1)
print(type(tuple1))

Q2: Print the length of the tuple.
We use the len() function to get the length of the tuple.

length = len(tuple1)
print("Length of tuple =",length)

Key Concepts Explained
1. List
A list in Python is an ordered collection of items. Lists are mutable, meaning their elements can be modified. We can perform various operations like adding, removing, and iterating over the elements.

Example operations:
append(): Adds an item to the end of the list.
for loop: Allows you to iterate through the list and access each element.

2. Dictionary
A dictionary is an unordered collection of key-value pairs. Keys are unique, and they are used to access the corresponding values. Dictionaries are mutable, so you can modify their contents.

Example operations:
Adding a new key-value pair using dictionary[key] = value.
Accessing values using keys.

3. Set
A set is an unordered collection of unique elements. Sets are mutable and do not allow duplicate elements. They are useful for membership tests and eliminating duplicates.

Example operations:
add(): Adds an element to the set.
remove(): Removes an element from the set.

4. Tuple
A tuple is an ordered collection of items that are immutable. Once created, the elements of a tuple cannot be changed. Tuples are used when you need an immutable sequence of values.

Example operations:
len(): Returns the number of items in the tuple.

Conclusion
This repository contains basic exercises for understanding and manipulating Python's built-in data structures: Lists, Dictionaries, Sets, and Tuples. These data structures are fundamental to Python programming and are used in a wide range of applications.

Run the code in your Python environment (e.g., Jupyter Notebook, Python shell, etc.).


