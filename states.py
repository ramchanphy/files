fname=open("delhi.txt","a")
gname=open("shimla.txt","a")
hname=open("jaipur.txt","a")
f=open("text_people.txt","r")
c=f.readlines()
i=0
while i<len(c):
    if "delhi" in c [i]:
        fname.write(c[i])
        fname.write("\n")
    elif "shimla" in c[i]:
        gname.write(c[i])
        gname.write("\n")
    else:
        hname.write(c[i])
        hname.write("\n")
    i+=1
f.close()
fname.close()
hname.close()
gname.close()
        
