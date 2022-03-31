f=open("name.txt","w+")
f.write("My name is Ramchanphy")
f.write("Python is Great")
f.seek(0)
c=f.read()
words=c.split()
a=[]
b=[]
i=0
while i<len(words):
    j=0
    while j<len(words[i]):
        if words[i][j]>="A" and words[i][j]<="Z":
            a.append(words[i][j])
        else:
            b.append(words[i][j])
        j+=1
    i+=1
print(a)
print(b)
