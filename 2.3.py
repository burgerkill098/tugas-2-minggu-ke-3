
print ("             mencari bilangan terbesar           ")
print("______________________________________________________")

bil1=int(input("masukkan bilangan pertama :"))
bil2=int(input("masukkan bilangan ke dua :"))
bil3=int(input("masukkan bilangan ke tiga :"))


if (bil1>bil2) or (bil1>bil3) :
    print("bilangan terbesar adalah :",bil1)
elif (bil2>bil1) or (bil2>bil3):
     print("bilangan terbesar adalah :",bil2)
elif ( bil3>bil1) or (bil3>bil2):
    print("bilangan terbesar adalah :",bil3)
