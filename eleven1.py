def file_size(fname):
    with open(fname) as f:
        data=f.read()
        f.read()
        print("size od the file:",f.tell())
        print(data)
file_size("text_people.txt")

