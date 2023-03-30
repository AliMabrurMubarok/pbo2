#Nama = ALI MABRUR MUBAROK
#Nim = 210511112
#Kelas = TIF21C / R3

class Seseorang: 
    def __init__(self, name, umur, gender): 
        self.name = name 
        self.umur = umur 
        self.gender = gender 
    
    def get_info(self): 
        print("Name:", self.name) 
        print("Umur:", self.umur) 
        print("Jenis Kelamin:", self.gender) 
        
# Single Inheritance 
class Pejabat(Seseorang): 
    def __init__(self, name, umur, gender, NIP): 
        super().__init__(name, umur, gender)
        self.NIP = NIP
    
    def get_info(self): 
        super().get_info() 
        print("NIP:", self.NIP)

# Single Inheritance 
class Aparat(Seseorang): 
    def __init__(self, name, umur, gender, kode_aparat, pangkat): 
        super().__init__(name, umur, gender) 
        self.kode_aparat = kode_aparat 
        self.pangkat = pangkat 
    
    def get_info(self): 
        super().get_info() 
        print("Kode Aparat:", self.kode_aparat) 
        print("Pangkat:", self.pangkat) 
        
# Multiple Inheritance 
class Tni(Aparat, Pejabat): 
    def __init__(self, name, umur, gender, kode_aparat, pangkat, NIP, perwira): 
        Aparat.__init__(self, name, umur, gender, kode_aparat, pangkat) 
        Pejabat.__init__(self, name, umur, gender, NIP) 
        self.perwira = perwira 
        
    def get_info(self): 
        super().get_info() 
        print("Pangkat:", self.pangkat) 
        print("kode:", self.kode_aparat)
