import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('Copied successfully!')
    else:
        print('Error: Source file does not exist.')

f1 = r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab 6\dir_files\7text.txt"
f2 = r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab 6\dir_files\7.2text.txt"

copy(f1, f2)
