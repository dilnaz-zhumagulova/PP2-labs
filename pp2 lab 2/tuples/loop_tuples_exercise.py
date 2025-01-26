#What is a correct syntax for looping through the items of a tuple?
#for x in ('apple', 'banana', 'cherry'):
  #print(x)
  
mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1
    
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])