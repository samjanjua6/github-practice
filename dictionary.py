#dictionary : key-value pairs, unordered, mutable, and indexed.
#  Dictionaries are written with curly brackets, and they have keys and values.

mydict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "name": "ali",
    "age": 28,
    "city": "mandi"
}

print(mydict)

mydict2 = dict(key1="value1", key2="value2", key3="value3", name="ali", age=28, city="mandi")
print(mydict2)

#for dict() you dont need to use curly brackets, 
# but you need to use the dict() function and pass the key-value pairs as arguments.

value = mydict["key1"]
print(value)

mydict["email"]="ali@example.com"
print(mydict)

del mydict["age"]
print(mydict)

mydict.pop("city") 
print(mydict)

mydict.popitem() #removes the last inserted item
print(mydict)

if "name" in mydict:
    print("Yes, 'name' is a key in the dictionary")
else:
    print("No, 'name' is not a key in the dictionary")

try:
    print(mydict["age"])
except KeyError:
    print("Key 'age' not found in the dictionary")

for key in mydict.keys():
    print(key, mydict[key])

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict_cpy = mydict.copy()
print(mydict_cpy)

mydict_cpy["email"] = "ma@example.com"
print(mydict_cpy)
print(mydict)

mydict.update({"email": "aliraza@gmail.com"})
print(mydict)

mydict.update(mydict_cpy)
print(mydict)

