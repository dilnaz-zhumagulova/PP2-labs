#what will be a correct syntax for printing the name 'May'?
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers['c2']['name']) #answer

a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])

#. A dictionary can only have one level of nested dictionaries.
#False