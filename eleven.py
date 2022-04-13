# 11. Write a Python program to get the file size of a plain file.

def file_size(fname):
        with open(fname)as f:
                f.seek(0)
                f.read()
                print("file size in bytes of a plain file:-",f.tell())
file_size("text_people.txt")