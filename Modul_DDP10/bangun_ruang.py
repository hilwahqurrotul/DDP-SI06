import math

def luas_kubus(sisi):
    luas = 6 * sisi * sisi
    print(f'Luas Kubus {6} * {sisi} * {sisi} = {luas}')

def luas_balok (panjang, lebar, tinggi):
    luas = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
    print(f'Luas Balok {2} * ({panjang*lebar} + {panjang*tinggi} + {lebar*tinggi})= {luas}')

def luas_tabung (jarijari, tinggi):
    luas = 2 * 3.14 * jarijari * (jarijari+tinggi)
    print(f'Luas Tabung {2} * {3.14} * {jarijari} * ({jarijari+tinggi}) = {luas}')

def luas_prisma(luas_alas, keliling_alas, tinggi):
    luas = (2 * luas_alas) + (keliling_alas*tinggi)
    print(f'Luas Prisma {(2 * luas_alas)} + {(keliling_alas*tinggi)} = {luas}')

def luas_bola(jarijari):
    luas = 2 * 3.14 * jarijari
    print(f'Luas Bola {2} * {3.14} * {jarijari} = {luas}')
