#A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')

#Tuple items are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry', 'apple', 'cherry')

#To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3

#tuple with 1 item
thistuple = ("apple",)
print(type(thistuple))
#<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#<class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
#('apple', 'banana', 'cherry')
#(1, 5, 7, 9, 3)
#(True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#('abc', 34, True, 40, 'male')

#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
#('apple', 'banana', 'cherry')
