#Nama : ALI MABRUR MUBAROK
#Nim : 210511112
#Kelas : TIF21C

class Rumahsakit:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def dirawat(self):
        print(self.nama, "sedang dirawat")

class Pasien(Rumahsakit):
    def __init__(self, nama, alamat, penyakit):
        super().__init__(nama, alamat)
        self.penyakit = penyakit

    def pulang(self):
        print(self.nama, "telah dipulangkan")

pasien1 = Pasien("naruto", "konoha", "asamlambung")
pasien1.dirawat()
pasien1.pulang()