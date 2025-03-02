import os

if os.path.exists('dir_files/delete.txt'):
    os.remove('dir_files/delete.txt')
    print('deleted')