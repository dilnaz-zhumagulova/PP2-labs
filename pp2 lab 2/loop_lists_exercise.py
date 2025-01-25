#What is a correct syntax for looping through the items of a list?
for x in ['apple', 'banana', 'cherry']:
  print(x)

#Insert the missing part of the while loop below to loop through the items of a list.
mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1
  
#What is a correct syntax for looping through the items of a list?
[print(x) for x in ['apple', 'banana', 'cherry']]