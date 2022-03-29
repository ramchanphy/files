# 2. Write a Python program to read first n lines of a file
f = open("demofile1.txt", "r")
c=f.readlines()[0]
print(c)
f.close()