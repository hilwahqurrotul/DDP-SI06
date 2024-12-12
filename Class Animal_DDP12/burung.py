from animals import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

print('-----------Cetak Burung----------')
print('-----------Objek Pertama---------')
beo = burung('Burung beo', 'biji-bijian', 'udara', 'bertelur', 'biru dan kuning', 'halo')
beo.cetak_burung()

print('-----------Objek Kedua---------')
perkutut = burung('Burung perkutut', 'biji-bijian', 'udara', 'bertelur', 'hitam dan abu', 'kukukuku')
perkutut.cetak_burung()