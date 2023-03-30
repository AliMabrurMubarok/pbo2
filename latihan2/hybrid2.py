#Nama = ALI MABRUR MUBAROK
#Nim = 210511112
#Kelas = TIF21C / R3

class Tumbuhan: 
    def __init__(self, name, age, color): 
        self.name = name 
        self.age = age 
        self.color = color 
    
    def get_info(self): 
        print("Name:", self.name) 
        print("Age:", self.age) 
        print("Color:", self.color) 
        
# Single Inheritance 
class Berbatang(Tumbuhan): 
    def __init__(self, name, age, color, berkayu): 
        super().__init__(name, age, color)
        self.berkayu = berkayu
    
    def get_info(self): 
        super().get_info() 
        print("Berbatang:", self.berkayu)

# Single Inheritance 
class Berongga(Tumbuhan): 
    def __init__(self, name, age, color, jenis, daun): 
        super().__init__(name, age, color) 
        self.jenis = jenis 
        self.daun = daun 
    
    def get_info(self): 
        super().get_info() 
        print("jenis :", self.jenis) 
        print("Berdaun :", self.daun) 
        
# Multiple Inheritance 
class Padi(Berongga, Berbatang): 
    def __init__(self, name, age, color, jenis, daun, berkayu, panen): 
        Berongga.__init__(self, name, age, color, jenis, daun) 
        Berbatang.__init__(self, name, age, color, berkayu) 
        self.panen = panen 
        
    def get_info(self): 
        super().get_info() 
        print("Berbatang :", self.berkayu) 
        print("Dipanen Pada :", self.panen)
