import string
import os

directory = r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab 6\dir_files"

os.makedirs(directory, exist_ok=True)

for i in string.ascii_uppercase:
    file_path = os.path.join(directory, f"{i}.txt")  
    with open(file_path, 'w') as file:
        file.write(f"This is {i}.txt")  

print(f"26 text files (A.txt to Z.txt) have been created in {directory} successfully!")
