def fun(fname):
    with open(fname)as f:
        c=f.read()
        d=c.split()
        count=0
        i=0
        while i<len(d):
            j=0
            while j<len(d[i]):
                if d[i][j]=="a" or d[i][j]=="m" or d[i][j]=="A" or d[i][j]=="M":
                    count+=1
                j+=1
            i+=1
        print(count)
fun("STORY.TXT")
