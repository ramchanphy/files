long=open("longest_word.txt","r")
str=long.read()
words=str.split()
max_long=len(max(words,key=len))
for word in words:
    if len(word)==max_long:
        longest=word
print(longest)
print(len(words))