
f=open("text_people.txt","r")
c=f.readlines()
i=0
count=0
while i<len(c):
    count+=1
    i+=1
print(count)
f.close()
    