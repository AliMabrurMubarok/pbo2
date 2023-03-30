#Nama = ALI MABRUR MUBAROK
#Nim = 210511112
#Kelas = TIF21C / R3

class AkunShopee: 
    def __init__(self, nomor_akun, alamat): 
        self.nomor_akun = nomor_akun 
        self.alamat = alamat
    
    def get_nomor_akun(self): 
        return self.nomor_akun 
        
    def get_alamat(self): 
        return self.alamat
        
class AkunTopup(AkunShopee): 
    def __init__(self, nomor_akun, alamat, topup): 
        super().__init__(nomor_akun, alamat) 
        self.topup = topup 
        
    def get_topup(self): 
        return self.topup

class Akunchekout(AkunShopee): 
    def __init__(self, nomor_akun, alamat, chekout): 
        super().__init__(nomor_akun, alamat) 
        self.chekout = chekout
        
    def get_checkout(self): 
        return self.chekout
        
# Hierarchical Inheritance 
class Pembeli(Akunchekout): 
    def __init__(self, nomor_akun, alamat, chekout, tujuan):
        super().__init__(nomor_akun, alamat, chekout) 
        self.tujuan = tujuan
        
    def get_tujuan(self): 
        return self.tujuan