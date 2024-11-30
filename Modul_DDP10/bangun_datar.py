import math
         
def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling Persegi adalah {keliling}')

def p_panjang(panjang, lebar):
    luas = panjang * lebar   
    keliling = 2 * (panjang + lebar)
    print(f'luas persegi panjang {panjang} * {lebar} = {luas}')
    print (f'keliling persegi panjang {keliling}')

def l_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f'luas segitiga {0.5} * {alas} * {tinggi} = {luas}')

def l_lingkaran(jarijari):
    luas = 3.14 * jarijari * jarijari
    print(f'luas lingkaran {3.14} * {jarijari} * {jarijari} = {luas}')

def jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    print(f'luas jajar genjang {alas} * {tinggi} = {luas}')


