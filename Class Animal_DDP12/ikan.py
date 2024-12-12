from animals import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna_ikan} dan hewan ini berjenis {self.jenis_ikan}')

print('-----------Cetak Ikan----------')
print('-----------Objek Pertama---------')
mujaer = ikan('ikan mujaer', 'pelet', 'air', 'bertelur', 'abu', 'air tawar')
mujaer.cetak_ikan()

print('-----------Objek Kedua---------')
arwana = ikan('ikan arwana', 'jangkrik', 'air', 'bertelur', 'merah dan emas', 'air tawar')
arwana.cetak_ikan()   