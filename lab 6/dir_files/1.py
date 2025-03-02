import os

def list(x):
    print("Directories:")
    for item in os.listdir(x):
        if os.path.isdir(os.path.join(x, item)):
            print(item)
    
    print()
    print("Files:")
    for item in os.listdir(x):
        if os.path.isfile(os.path.join(x, item)):
            print(item)
    
pp=os.path.join(os.getcwd(), "")
list(pp)