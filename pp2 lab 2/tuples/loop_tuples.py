thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple
#banana
#cherry

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#Use the range() and len() functions to create a suitable iterable.

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1