from re import A


print("              menghitung berat bada ideal             ")
print("________________________________________________________")

nama=(input("NAMA : "))
tinggi=int (input("MASUKKAN TINGGI BADAN (CM) :"))

berat=(tinggi-100)-((tinggi-100)*10/100)

print("saudara "+str (nama))
print ("jadi berat ideal anda adalah  :"+str (berat))

