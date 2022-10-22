print( "            DATA NILAI MAHASISWA           ")
print("_________________________________________________")
nama=(input("Nama :"))
tugas=float(input("Tugas :"))
uts=float(input("UTS :"))
uas=float(input("UAS :"))
print("_____________________________________________________")

na=(tugas *0.25)+(uas*0.35)+(uas*0.40)

print("                  NILAI AKHIR DAN GRED          ")
print("__________________________________________________")

print("NAMA :",nama)
print("NILAI AKHIR :",na)


if na >= 75:
    print("GRADE : A ")

elif na>=60:
    print("GRADE : B")

elif na>= 51 :
    print("GRADE : C")
elif na< 45 :
    print("GRADE: D")
