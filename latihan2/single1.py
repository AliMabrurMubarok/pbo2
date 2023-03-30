#Nama : ALI MABRUR MUBAROK
#Nim : 210511112
#Kelas : TIF21C

class Karyawan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def misi(self):
        print(f"{self.nama} sedang menjalankan misi.")

class Kerjaan(Karyawan):
    def __init__(self, nama, jenis, status):
        super().__init__(nama, jenis)
        self.status = status

    def cuti(self):
        print(f"{self.nama} sebagai {self.jenis} sedang cuti.")

kerja1 = Kerjaan("Sujiwo", "teknisi", "karyawan")
kerja1.misi()
kerja1.cuti()