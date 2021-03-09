import os
import shutil

print("1. Current location: ", os.getcwd())
print("2. Work with: 1 -- directory")
print("              2 -- file")
x = input()
if x == '2':
    print("Choose one of the options: ")
    print("  a) delete file")
    print("  b) rename file")        
    print("  c) add content to this file")        
    print("  d) rewrite content of this file")        
    print("  e) return to the parent directory")     
    a = input()
    if a == 'a':
        os.remove(os.remove(x))
    if a == 'b':
        os.rename(x, input("enter new name: "))
    if a == 'c':
        with open(x, 'a') as f:
            f.write(input("enter content, that will be added: "))
    if a == 'd':
        with open(x, 'w') as f:
            f.write(input("enter the rewritable content: "))
    #if a == 'e':

if x == '1':
    print("Choose one of the options: ")
    print("  a) rename directory")
    print("  b) print number of files")        
    print("  c) print number of directories")        
    print("  d) list content of the directory")        
    print("  e) add file to this directory")  
    print("  f) add new directory to this directory")  
    d = input()
    if d == 'a':
        os.rename(os.remove(x))
    if d == 'b':
        d = list(os.listdir(x))
        print(len(d))
    # if d == 'c':
        
    # if d == 'd':    
    # if d == 'e':
    # if d == 'f':
    

        
        


# 1. Your current location is disk C directory. (or home directory for Mac OS, Linux)
# 2. Each time there are two options: you are either work with directory, or with file.
# 3. If your current location is file you have several options:
# a) delete file
# b) rename file
# c) add content to this file
# d) rewrite content of this file
# e) return to the parent directory
# 4. If your current location is directory you have several options:
# a) rename directory
# b) print number of files
# c) print number of directories
# d) list content of the directory
# e) add file to this directory
# f) add new directory to this directory