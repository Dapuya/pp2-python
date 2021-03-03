import os
import shutil

print("1. Current location: ", os.getcwd())
print("2. Choose one of the options:  ")
print("    1 - working with file")
print("    2 - working with directory")
n = int(input())
if n == 1 :
    print("Choose one of the options: ")
    print("  a) delete file")
    print("  b) rename file")        
    print("  c) add content to this file")        
    print("  d) rewrite content of this file")        
    print("  e) return to the parent directory")     
    a = input()
    if a == 'a':
        


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
