#8. Write a python program to find the longest words.             
f=open("longest_word.txt")
f1=f.read()
words=f1.split()
print(words)
i=0
max=0
for i in words:
    if len(i)>max:
        max=len(i)
        a=i
print(max,a)


