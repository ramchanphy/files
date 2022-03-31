# 10. Write a Python program to count the frequency of words in a file.
f=open("document1.txt","r")
c=f.read()
words=c.split()
user=input("enter the word:-")
i=0
count=0
while i<len(words):
    if words[i] == user:
        count+=1
    i+=1
print(count)
f.close()