from animals import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, cara_menyerang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ular = warna_ular
        self.cara_menyerang = cara_menyerang

    def cetak_ular(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna_ular} dan hewan ini menyerang dengan cara {self.cara_menyerang}')

print('-----------Cetak Ular----------')
print('-----------Objek Pertama---------')
cobra = ular('ular cobra', 'daging', 'air', 'bertelur', 'hitam', 'menyuntikan bisa')
cobra.cetak_ular()

print('-----------Objek Kedua---------')
piton = ular('ular piton', 'hewan', 'darat', 'bertelur', 'coklat dan hitam', 'melilit mangsanya')
piton.cetak_ular()   