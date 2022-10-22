


from telnetlib import PRAGMA_HEARTBEAT


print("                DATA KARYAWAN               ")
print("________________________________________________")

nama=input("NAMA  :")
golongan=input("GOLONGAN [A,B,C] : " )
jamkerja=int(input("Total jam kerja :"))

if  golongan=='A':
    gajipokok=500000
    tunjangan=0.1*gajipokok 
    lembur=5000
elif golongan=='B':
    gajipokok=700000
    tunjangan=0.15*gajipokok 
    lembur=7500
elif golongan=='C':
    gajipokok=900000
    tunjangan=0.2*gajipokok 
    lembur=10000

if jamkerja>200:
   jamlembur=jamkerja-200


biayalembur=jamlembur *lembur


gaji=gajipokok+tunjangan+biayalembur
print("          PERHITUNGAN GAJI KARYAWAN        ")
print("_____________________________________________")

print("GAJI POKOK =",gajipokok)
print("TUNJANGAN =",tunjangan)
print("LEMBUR =",biayalembur)
print("_______________________________________________")
print("TOTAL =",gaji)