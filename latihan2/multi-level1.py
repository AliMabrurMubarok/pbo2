#Nama = ALI MABRUR MUBAROK
#Nim = 210511112
#Kelas = TIF21C / R3

class Tumbuhan: 
    def __init__(self, name): 
        self.name = name 
        
    def fotosintesis(self): 
        print("Tumbuhan ini sedang Fotosintesis") 
        
class Berbatang(Tumbuhan): 
    def __init__(self, name, kayu): 
        super().__init__(name) 
        self.kayu = kayu
        
    def kayu(self): 
        print("Tumbuhan berkayu") 
        
class Mangga(Berbatang): 
    def __init__(self, name, kayu, buah): 
        super().__init__(name, kayu) 
        self.buah = buah
    
    def buah(self): 
        print("Tumbuhan ini berbuah")