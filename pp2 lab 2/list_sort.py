thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#[23, 50, 65, 82, 100]

#sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

def myfunc(n):
  return abs(n - 50)

#Sort the list based on how close the number is to 50:
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#[50, 65, 23, 82, 100]

#By default the sort() method is case sensitive, 
#resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#['Kiwi', 'Orange', 'banana', 'cherry']

# if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#['banana', 'cherry', 'Kiwi', 'Orange']

#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#['cherry', 'Kiwi', 'Orange', 'banana']