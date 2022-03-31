# 12. Write a Python program to write a list to a file.
list=["India","Korea","Japan","China","Pakistan"]
f=open("next_text.txt","w")
# c=f.read()
i=0
while i<len(list):
    f.write(list[i])
    f.write("\n")
    print(f.write)
    i+=1
f.close()

