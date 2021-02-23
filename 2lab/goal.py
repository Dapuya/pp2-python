
command = str(input())  
command = command.replace("G", "G")
command = command.replace("()", "o")
print(command.replace("(al)", "al"))


# G    --->  G
# ()   --->  o
# (al) --->  al