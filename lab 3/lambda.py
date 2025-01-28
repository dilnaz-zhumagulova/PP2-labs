#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
x = lambda a: a + 10
print(x(5))
#15

x = lambda a, b: a * b
print(x(5, 6))
#30

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
#13

#The power of lambda is better shown when you use them as an anonymous function inside another function. 
#function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#22

# same function definition to make a function that always triples the number you send in:
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
#33

#same function definition to make both functions, in the same program
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) 
print(mytripler(11))
#22
#33
