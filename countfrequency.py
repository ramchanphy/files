f=open("demofile3.txt","r")
c=f.read()
s=c.split()
i=0
count=0
user=input("enter the word:-")
while i<len(s):
    if user in s[i]:
        count+=1
    i+=1
print(count)
f.close()
