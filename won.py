f=open("won.txt","r")
c=f.read()
a=""
b=[]
i=0
while i<len(c):
    if c[i]>="A" and c[i]<="Z":
        d=c[i].lower()
        a+=d
    else:
        e=c[i].upper()
        a+=e
    i+=1
j=0
while j<len(a):
    if a[j]>="A" and a[j]<="Z":
        b.append(j)
    j+=1
print(a)
print(b)

