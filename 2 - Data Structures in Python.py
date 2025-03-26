# Topic: List 
# Exercise 
# Q1. Create a list of 5 random numbers and print the list. 
numbers = list(range(1,11))
print("Original list: ",numbers)

# Q2. Insert 3 new values to the list and print the updated list. 
numbers.append(11)
numbers.append(12)
numbers.append(13)
print("Updated list: ",numbers)

# Q3. Try to use a for loop to print each element in the list. 
print("Elements in list are below: ")
for i in numbers:
    print(i)


Output :
Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Updated list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Elements in list are below: 
1
2
3
4
5
6
7
8
9
10
11
12
13

------------------------------------------------------------------------------------------------------------------

# Topic: Dictionary 
# Exercise 
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively. 
dict1 = {'name': 'John', 'age':25, 'address':'New York'}
print("Original dictionary: ",dict1)

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'. 
dict1['phone'] = '1234567890'
print("Updated dictionary: ",dict1)


Output :
Original dictionary:  {'name': 'John', 'age': 25, 'address': 'New York'}
Updated dictionary:  {'name': 'John', 'age': 25, 'address': 'New York', 'phone': '1234567890'}


-------------------------------------------------------------------------------------------------------------------

# Topic: Set 
# Exercise 
# Q1. Create a set with values 1, 2, 3, 4, and 5. 
set1 = {1,2,3,4,5}
print("Original set: ",set1)

# Q2. Add the value 6 to the set created in Q1.
set1.add(6)
print("Updated set after adding value 6: ",set1)

# Q3. Remove the value 3 from the set created in Q1. 
set1.remove(3)
print("Updated set after removing value 3: ",set1)


Output :
Original set:  {1, 2, 3, 4, 5}
Updated set after adding value 6:  {1, 2, 3, 4, 5, 6}
Updated set after removing value 3:  {1, 2, 4, 5, 6}


-----------------------------------------------------------------------------------------------------------------------

# Topic: Tuple 
# Exercise 
# Q1. Create a tuple with values 1, 2, 3, and 4. 
tuple1 = (1,2,3,4)
print("Original tuple: ",tuple1)
print(type(tuple1))

# Q2. Print the length of the tuple created in Q1.
length = len(tuple1)
print("Length of tuple =",length)


Output :
Original tuple:  (1, 2, 3, 4)
<class 'tuple'>
Length of tuple = 4