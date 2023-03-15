class Fahrenheit:
    def __init__(self, fahrenheit):
        self.f = fahrenheit

    def Celcius(self):
        return 5/9 * (self.f - 32)
    
    def Reamur(self):
        return 4/9 * (self.f - 32)
    
    def Kelvin(self):
        return 5/9 * (self.f - 32) + 273

A = Fahrenheit(69)
print(f" Suhu Celciusnya : {A.Celcius()}")
print(f" Suhu Reamurnya : {A.Reamur()}")
print(f" Suhu Kelvinnya : {A.Kelvin()}")