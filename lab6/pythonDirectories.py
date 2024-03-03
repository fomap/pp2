import os
import string

'''
1)

def filesAndDirectories(myPath):
    print(os.listdir(myPath))

path = "D:\\"
filesAndDirectories(path)


def files(myPath):
    onlyfiles = [f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))]
    print(onlyfiles)

path = "D:\\"
files(path)


def directories(myPath):
    dirs = [f for f in os.listdir(myPath) if os.path.isdir(os.path.join(myPath, f))]
    print(dirs)

path = "D:\\"
directories(path)


2)
def check_directory_permissions(directory_path):
   if os.path.exists(directory_path):
    permissions = os.stat(directory_path).st_mode
    print(f"Permissions of the directory: {directory_path}")
    print(f"Read permission: {'Yes' if permissions & 0o400 else 'No'}")
    print(f"Write permission: {'Yes' if permissions & 0o200 else 'No'}")
    print(f"Execute permission: {'Yes' if permissions & 0o100 else 'No'}")
   else:
     print("Directory doesn't exists")

directory_path = "D:\\web"
check_directory_permissions(directory_path)


3)
def dirExistance(myPath):
    if os.path.exists(myPath):
        print(os.path.basename(path))
        print(os.path.dirname(path))

    else:
        print("Directory doesn't exists")


path = "D:\\UNI\\beka1.psd"
dirExistance(path)


4)
with open("lab6\\test.txt", "r") as f:
    lines = len(f.readlines())
    print(lines)



5)
team7 = ["Naruto", "Sakura", "Sasuke", "Kakashi"]

with open("lab6\\test.txt", 'w') as f:
    for line in team7:
        f.write(line + '\n')


6)
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)


7)
with open('lab6\\test.txt','r') as ff, open('lab6\\second.txt','a') as sf: 
    for line in ff: 
        sf.write(line)

'''


path = "D:\\delete.txt"

def task8(myPath):
    if os.path.exists(myPath):
        permissions = os.stat(myPath).st_mode
        print(f"Permissions of the directory: {myPath}")
        print(f"Read permission: {'Yes' if permissions & 0o400 else 'No'}")
        print(f"Write permission: {'Yes' if permissions & 0o200 else 'No'}")
        print(f"Execute permission: {'Yes' if permissions & 0o100 else 'No'}")
    else:
        print("Directory doesn't exists")

    os.remove(myPath)

task8(path)