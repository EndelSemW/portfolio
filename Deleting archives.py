import re
import os

name="test.txt"
path="C:/Users/Reinaldo/Documents/Projects/Portfolio/"

if os.path.exists(path + name):
    print("File exists")
else:
    file=open(path + name, "x")
    file.close()
    print("File created")

if os.path.exists(path + name):
    os.remove(path+name)
    print("File removed")
else:
    print("File does not exist")
