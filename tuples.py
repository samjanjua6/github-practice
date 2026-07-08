#tuples : ordered, immutable,allows duplicate elements
#generally declared using parentheses but can also be declared without parentheses

mytuple = ("apple", "banana", "cherry",2)
print(mytuple)

mytuple = "apple", "banana", "cherry"
print(mytuple)
print(type(mytuple))

# mytuple.append("date") #tuples are immutable, so this will raise an error

item = mytuple[0:2]
print(item)

item = mytuple[-2:-1]
print(item)

for i in mytuple:
    print(i)
if "banana" in mytuple:
    print("Yes, 'banana' is in the tuple")
else:
    print("No, 'banana' is not in the tuple")

tuple1 = ("a", "b", "c","c", "d", "e")
print(tuple1)

print(tuple1.count("c")) #count the number of times a specified value occurs in a tuple

print(len(tuple1)) #return the number of items in a tuple

print(tuple1.index("c")) #return the index of the first occurrence of a specified value in a tuple

#we can convert a tuple into a list and then modify it, and then convert it back to a tuple

my_list = list(mytuple)
print(my_list)


my_tuple = tuple(my_list)
print(my_tuple)

#slicing with tuples

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[2:5]
print(b) 

#tuples can be nested, meaning you can have a tuple inside another tuple.
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)

my_tuple = (1, 2, 3, 4, 5)
#unpacking a tuple means assigning the values of a tuple to multiple variables in a single statement.
x, y, z, w, v = my_tuple
print(x, y, z, w, v)

#another example of unpacking a tuple
#the number of variables must match the number of elements in the tuple, otherwise it will raise a ValueError.
my_tuple = "ali",28,"mandi"
name, age,city = my_tuple
print(name) 
print(age)
print(city)

my_tuple = (1, 2, 3, 4, 5)
i1, *i2, i3 = my_tuple
print(i1) #1
print(i2) #[2, 3, 4]
print(i3) #5

#compare tuple and a list
#because a tuple immutable, it is generally faster than a list.
#  Tuples are also more memory efficient than lists, and they are good for big data sets
#  as they require less memory to store the same number of elements.
#  However, lists are more flexible than tuples, 
# as they can be modified after creation.


import sys
my_list = [0,1,2,"hello",True,False]
my_tuple = (0,1,2,"hello",True,False)

print("List size in bytes:", sys.getsizeof(my_list)) #104 bytes
print("Tuple size in bytes:", sys.getsizeof(my_tuple)) # 88 bytes

#tuples use less memory than lists because they are immutable,
#  meaning that their size is fixed and cannot be changed after creation.

