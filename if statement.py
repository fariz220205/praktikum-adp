x=int(input("masukan nilai anda : "))
y=input("apakah anda lulus kelas? (y/n) :")
if x >= 70 :
    y=True
    print("anda lulus kelas dan adp")
elif 70 > x >= 50 :
    y=False
    print("anda lulus adp tetapi tidak lulus kelas")
elif x <= 30 :
    y=True
    print("anda tidak lulus adp tetapi lulus kelas")
else :
    print("anda tidak lulus kelas dan adp")