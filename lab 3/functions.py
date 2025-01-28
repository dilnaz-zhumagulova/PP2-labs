#A function is a block of code which only runs when it is called.
def my_function():
  print("Hello from a function")
my_function()

#Information can be passed into functions as arguments.
#You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Emil Refsnes
#Tobias Refsnes
#Linus Refsnes


def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
#Emil Refsnes

#If you try to call the function with 1 or 3 arguments, you will get an error:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
#TypeError: my_function() missing 1 required positional argument: 'lname'

#If the number of arguments is unknown, add a * (Arbitrary Arguments, *args) before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#The youngest child is Linus

#You can also send arguments with the key = value syntax.(keyword arguments or kwargs)
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#The youngest child is Linus

#If the number of keyword arguments is unknown, add a double ** before the parameter name: (Arbitrary Keyword Arguments, **kwargs)
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
#His last name is Refsnes

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#I am from Sweden
#I am from India
#I am from Norway
#I am from Brazil

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
#apple
#banana
#cherry

#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#15
#25
#45

#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
def my_function(x, /):
  print(x)
my_function(3)
#3

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments: 
def my_function(x):
  print(x)

my_function(x = 3)
#3

#But when adding the , / you will get an error if you try to send a keyword argument:
def my_function(x, /):
  print(x)

my_function(x = 3)
#TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x'

#Keyword-Only Arguments
def my_function(*, x):
  print(x)
my_function(x = 3)
#3

#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)
my_function(3)
#3

#But with the *, you will get an error if you try to send a positional argument:
def my_function(*, x):
  print(x)
my_function(3)
#TypeError: my_function() takes 0 positional arguments but 1 was given

#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)
#26

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
#Recursion Example Results:
#1
#3
#6
#10
#15
#21