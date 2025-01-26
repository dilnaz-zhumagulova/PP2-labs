#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)
#('apple', 'banana', 'cherry')

#we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#apple
#banana
#cherry

#The number of variables must match the number of values in the tuple, 
#if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#apple
#banana
#['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#apple
#['mango', 'papaya', 'pineapple']
#cherry