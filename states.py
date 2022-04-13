fname=open("delhi.txt","w")
gname=open("shimla.txt","w")
hname=open("jaipur.txt","w")
f=open("text_people.txt","r")
c=f.readlines()
i=0
while i<len(c):
    if "delhi" in c [i]:
        fname.write(c[i])
        # fname.write("\n")
    elif "shimla" in c[i]:
        gname.write(c[i])
        # gname.write("\n")
    else:
        hname.write(c[i])
        # hname.write("\n")
    i+=1
f.close()
fname.close()
hname.close()
gname.close()
        
