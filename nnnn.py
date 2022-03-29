# 4. Write a Python program to read last n lines of a file.
f=open("demofile.txt","r")
c=f.readlines()[-1]
print(c)
f.close()

    