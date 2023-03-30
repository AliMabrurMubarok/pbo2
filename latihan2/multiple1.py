#Nama : ALI MABRUR MUBAROK
#Nim : 210511112
#Kelas : TIF21C

class tumbuhan:
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    def display_info(self): 
        print(f"Nama: {self.nama}") 
        print(f"Type: {self.tipe}")

class berbuah:
    def __init__(self, daun, batang):
        self.daun = daun
        self.batang = batang

    def display_info(self): 
        print(f"Daun: {self.daun}") 
        print(f"Batung: {self.batang}")

class berbiji:
    def __init__(self, akar, bunga):
        self.akar = akar
        self.bunga = bunga

    def display_info(self): 
        print(f"Akar: {self.Akar}") 
        print(f"Bunga: {self.Bunga}")

class Mangga(tumbuhan, berbuah, berbiji):
    def __init__(self, nama, tipe, daun, batang, akar, bunga):
        tumbuhan.__init__(self, nama, tipe)
        berbuah.__init__(self, daun, batang)
        berbiji.__init__(self, akar, bunga)

    def display_info(self): 
        super().display_info() 
        print(f"Daun: {self.daun}") 
        print(f"Batang: {self.batang}") 
        print(f"Akar: {self.akar}") 
        print(f"Bunga: {self.bunga}")

tumbuhan1 = Mangga("Mangga", "buah", "hijau", "kasar", "serabut", "kuning")
tumbuhan1.display_info()