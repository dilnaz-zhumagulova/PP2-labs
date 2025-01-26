#What is a correct syntax for adding items to a set?
#add()

#Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)