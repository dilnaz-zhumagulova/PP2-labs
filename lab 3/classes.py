#To create a class, use the keyword class:
class MyClass:
  x = 5
print(MyClass)  #<class '__main__.MyClass'>

#Create object
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x) #5

#Use the __init__() function to assign values to object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#John
#36

#The __str__() Function
#The string representation of an object WITHOUT the __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1) #<__main__.Person object at 0x15039e602100>

#The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"    
p1 = Person("John", 36)
print(p1) #John(36)

#Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
p1.myfunc() #Hello my name is John

#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
    
  def myfunc(abc):
    print("Hello my name is " + abc.name)
    
p1 = Person("John", 36)
p1.myfunc() #Hello my name is John

#Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
p1.age = 40
print(p1.age) #40

#Delete Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
del p1.age
print(p1.age) #AttributeError

#Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
del p1
print(p1) #Nameerror

#The pass Statement
class Person:
  pass
# having an empty class definition like this, would raise an error without the pass statement