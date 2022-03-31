f=open("text.txt","w")
f.write("come_world.txt")
f=open("text.txt","r")
c=f.read()
words=c.split()
s="."
i=0
while i<len(words):
    j=0
    while j<len(words[i]):
        if words[i][j]==s:
            break
        else:
            print(words[i][j],end="")
        j+=1
    i+=1
f.close()