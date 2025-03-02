def list_to_file(file_path, d):
    with open(file_path, 'w') as file:
        for item in d:
            file.write(str(item) + '\n') 

mylist = ['BLA BLA', 'dilnaz', 'Qwerty', 'idk']
file_path = "5task.txt"
list_to_file(file_path, mylist)
print(f"Now list is in file with name {file_path}")
