#Nama = ALI MABRUR MUBAROK
#Nim = 210511112
#Kelas = TIF21C / R3

class Negara: 
    def __init__(self, name, flag): 
        self.name = name 
        self.flag = flag
        
    def get_details(self): 
        print(f"Name: {self.name}, Flag: {self.flag}") 
        
class Pemerintah(Negara): 
    def __init__(self, name, flag, lembaga, department): 
        super().__init__(name, flag) 
        self.lembaga = lembaga 
        self.department = department 
    
    def get_details(self): 
        super().get_details() 
        print(f"Lembaga: {self.lembaga}, Department: {self.department}") 
        
class PSSI(Pemerintah): 
    def __init__(self, name, flag, lembaga, department, fifa_banned): 
        super().__init__(name, flag, lembaga, department) 
        self.fifa_banned = fifa_banned
        
    def get_details(self): 
        super().get_details() 
        print(f"This country is: {self.fifa_banned}")