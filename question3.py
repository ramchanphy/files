banks_list=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("banks.txt",'w')
for i in banks_list:
    (f.write(i+"\n"))
