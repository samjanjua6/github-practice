# sets: unordered collection of unique elements, mutable, no duplicate elements, and unindexed.

myset = {"apple", "banana", "cherry","apple", "banana"}
print(myset)

myset = set(["apple", "banana", "cherry"])
print(myset)

myset = set("hello")
print(myset)
# l is repeated twice, so it will only appear once in the set.

myset = set()
myset.add("apple")
myset.add("banana")
myset.add("cherry")
print(myset)

myset.remove("banana")
print(myset)

if "banana" in myset:
    print("Yes, 'banana' is in the set")
else:
    print("No, 'banana' is not in the set")

setA = {1,2,3,4,5,6,7,8,9}
setB = {5,6,7,8,9,10,11,12,13}


# difference() method returns a set that contains the difference between two sets.
#setA.difference(setB) returns a set that contains the elements that are in setA but not in setB.
diff = setA.difference(setB)
print(diff)

# difference() method returns a set that contains the difference between two sets.
#setB.difference(setA) returns a set that contains the elements that are in setB
diff = setB.difference(setA)
print(diff)

diff = setA.symmetric_difference(setB)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)

# union() method returns a set that contains all the elements from both sets, without duplicates.
union = setA.union(setB)
print(union)

#intersection() method returns a set that contains the elements that are common to both sets.
intersection = setA.intersection(setB)
print(intersection)

setA.update(setB)
print(setA)

#superset: a set that contains all the elements of another set.
if setA.issuperset(setB):
    print("setA is a superset of setB")
else:
    print("setA is not a superset of setB")

# disjoint: two sets that have no elements in common.

if setA.isdisjoint(setB):
    print("setA and setB are disjoint sets")
else:
    print("setA and setB are not disjoint sets")

