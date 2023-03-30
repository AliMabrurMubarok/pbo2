#Nama : ALI MABRUR MUBAROK
#Nim : 210511112
#Kelas : TIF21C

class pakaian:
    def __init__(self, nama, merk):
        self.nama = nama
        self.merk = merk

    def display_info(self): 
        print(f"Nama: {self.nama}") 
        print(f"Merk dari: {self.merk}")

class panjang:
    def __init__(self, ukuran, bahan):
        self.ukuran = ukuran
        self.bahan = bahan

    def display_info(self): 
        print(f"Ukuran: {self.ukuran}") 
        print(f"Bahan: {self.bahan}") 

class pendek: 
    def __init__(self, genre, harga):
        self.genre = genre
        self.harga = harga

    def display_info(self): 
        print(f"Genre: {self.genre}") 
        print(f"Harga: {self.harga}") 

class Adidas(pakaian, panjang, pendek):
    def __init__(self, nama, merk, ukuran, bahan, genre, harga):
        pakaian.__init__(self, nama, merk)
        panjang.__init__(self, ukuran, bahan)
        pendek.__init__(self, genre, harga)

    def display_info(self):
        super().display_info()
        print(f"Ukurannya: {self.ukuran}")
        print(f"Bahan: {self.bahan}")
        print(f"Genrenya: {self.genre}")
        print(f"Harga senilai: {self.harga}")

Baju1 = Adidas("Baju", "Carvil", 67, "katun", "santai", 200000)
Baju1.display_info()
