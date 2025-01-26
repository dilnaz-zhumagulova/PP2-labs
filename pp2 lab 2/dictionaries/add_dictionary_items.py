thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
​#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}