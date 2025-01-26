#Set items are unordered, unchangeable, and do not allow duplicate values.
#Once a set is created, you cannot change its items, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#{'banana', 'cherry', 'apple'}

#True and 1 is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}

#The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#{False, True, 'cherry', 'apple', 'banana'}

#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
#{'cherry', 'apple', 'banana'}
#{1, 3, 5, 7, 9}
#{False, True}
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#{True, 34, 40, 'male', 'abc'}

myset = {"apple", "banana", "cherry"}
print(type(myset))
#<class 'set'>

#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))
print(thisset)