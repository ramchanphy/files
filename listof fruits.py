list=["apple","mango","banana","pineapple"]
f=open("list1.txt","w+")
i=0
while i<len(list):
    f.write(list[i])
    f.write("\n")
    f.seek(0)
    d=f.read()
    i+=1
print(d)
f.close()