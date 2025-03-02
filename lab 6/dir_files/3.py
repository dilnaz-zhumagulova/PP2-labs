import os

def check(path):
    if os.path.exists(path):
        print(path, "is exist")
        if os.path.isfile(path):
            print("Filename:", os.path.basename(path))
            print("Directory portion:", os.path.dirname(path))
        elif os.path.isdir(path):
            print("Directory:", os.path.basename(path))
            print("Directory portion:", os.path.dirname(path))
    else:
        print(path, "Doesn't exist")
    
if __name__ == "__main__":
    pp=input()
    check(pp)