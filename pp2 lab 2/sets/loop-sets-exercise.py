#What is a correct syntax for looping through the items of a set?
for x in {'apple', 'banana', 'cherry'}:
  print(x)

myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)

#Sets are unordered, so when you loop through the items, the order will be totally random.
#TRUE