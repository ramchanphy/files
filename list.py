# 5. Write a Python program to read a file line by line and store it into a list.
f=open("demofile.txt","r")
a=f.readlines()
print(a)
f.close()