f = open("demofile.txt", "r")
f.seek(2)
print(f.readline())