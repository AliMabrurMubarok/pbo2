class Reamur:
    def __init__(self, reamur):
        self.R = reamur

    def Celcius(self):
        return 5/4 * self.R
    
    def Kelvin(self):
        return 9/4 * (self.R +32)
    
    def Fahrenheit(self):
        return 5/4 * (self.R + 273)

A = Reamur(69)
print(f" Suhu Celciusnya : {A.Celcius()}")
print(f" Suhu Kelvinnya : {A.Kelvin()}")
print(f" Suhu Fahrenheitnya : {A.Fahrenheit()}")