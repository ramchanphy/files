# f = open("demofile2.txt", "w")
# f.write("Now the file has more content!")
# f.write("I'm working ")
# f.close()

# f = open("demofile.txt", "r")
# f.seek(2)
# print(f.readline())

# 9. Write a Python program to count the number of lines in a text file. 
f=open("document1.txt","r")
c=f.readlines()
i=0
count=0
while i<len(c):
    count+=1
    i+=1
print(count)
