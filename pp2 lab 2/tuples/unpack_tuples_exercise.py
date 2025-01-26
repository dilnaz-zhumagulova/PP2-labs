#What will be the value of y?
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
#banana

#What will be the value of y?
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
#['banana', 'cherry']

#What will be the value of y?
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
#['banana', 'cherry']