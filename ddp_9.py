#Nomor 1
print('\n----Celcius ke Fahrenheit----')
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)

#Nomor 2
print('\n----Mencari bilangan genap----')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

#Nomor 3
print('\n----Melihat keterangan lulus atau tidak lulus----')
#rata rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 70:
        print("LULUS")
    else:
        print("GAGAL")
skor(80)
skor(60)

#Nomor 4
print('\n----Mencetak bilangan ganjil----')
def bil_ganjil(ganjil):
    for i in range(1, ganjil+1, 2):
        print(i, end=" ")
bil_ganjil(20)