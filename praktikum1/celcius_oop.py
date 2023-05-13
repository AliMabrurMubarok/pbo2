#nama : ALI MABRUR MUBAROK
#nim  : 210511112

class Celciius:
    def __init__(self, celcius):
        self.c = celcius

    def Fahrenheit(self):
        return 9/5 * self.c
    
    def Reamur(self):
        return 4/5 * self.c
    
    def Kelvin(self):
        return self.c + 273

A = Celciius(69)
print(f" Suhu Fahrenheitnya : {A.Fahrenheit()}")
print(f" Suhu Reamurnya : {A.Reamur()}")
print(f" Suhu Kelvinnya : {A.Kelvin()}")