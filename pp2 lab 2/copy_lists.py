thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#['apple', 'banana', 'cherry']

#another way
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#slice(:) operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)