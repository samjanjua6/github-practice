mylist = ["banana", "apple", "cherry"]
print(mylist)

mylist2 = [5,"banana", True, 3.14,"banana"]
print(mylist2)

#you can append items to the list using the append() method

item = mylist[2]

print(item)

item = mylist[-2]
print(item)

for i in mylist:
    print(i)

if("banana" in mylist):
    print("Yes, 'banana' is in the fruits list")
else:
    print("No, 'banana' is not in the fruits list")

print(len(mylist))

mylist.append("orange")
print(mylist)
#using append() method you can add an item at the end of the list

mylist.insert(1, "kiwi")
print(mylist)
#using insert() method you can add an item at the specified index

item = mylist.pop()
print(item)

print(mylist)

item = mylist.remove("apple")
print(item)

# item = mylist.clear()
# print(mylist)

item = mylist.sort()
print(mylist)

new_list = sorted(mylist)
print(mylist)
print(new_list)

mylist.reverse()
print(mylist)

mylist = [0] * 5
print(mylist)
# by using * operator you can create a list with the same value repeated multiple times

mylist2 = [1, 2, 3, 4, 5]
new_list = mylist2.copy()

print(mylist2)

mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)

a = mylist[2:5]
print(a)

a= mylist[:4]
print(a)

a = mylist[5:]
print(a)

a= mylist[-4:-1]
print(a)

a = mylist[::2]
print(a)

a= mylist[1::2]
print(a)

list_org = ["banana", "apple", "cherry"]
list_cpy = list_org.copy()
list_cpy.append("date")
print(list_org)
print(list_cpy)
