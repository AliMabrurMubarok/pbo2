#Nama = ALI MABRUR MUBAROK
#Nim = 210511112
#Kelas = TIF21C / R3

class Tumbuhan:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def get_nama(self):
        return self.nama

    def get_warna(self):
        return self.warna

class berbiji(Tumbuhan):
    def __init__(self, nama, warna, biji):
        super().__init__(nama, warna)
        self.biji = biji

    def get_biji(self):
        return self.biji

class berbuah(Tumbuhan): 
    def __init__(self, nama, warna, buah):
        super().__init__(nama, warna) 
        self.buah = buah
    
    def get_buah(self): 
        return self.buah
        
# Hierarchical Inheritance 
class Semangka(berbuah): 
    def __init__(self, nama, warna, buah, batang): 
        super().__init__(nama, warna, buah)
        self.batang = batang
        
    def get_batang(self): 
        return self.batang
