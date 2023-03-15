class Buku :
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    def info (self):
        print(f"Judul : {self.judul}\nPenulis : {self.penulis}")
bukuA = Buku('Manusia Setengah Salmon', 'Raditya Dika')
bukuA.info()