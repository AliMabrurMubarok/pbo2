class Kelvin:
    def __init__(self, kelvin):
        self.K = kelvin

    def Celcius(self):
        return self.K - 273
    
    def Reamur(self):
        return 4/5 * (self.K - 273)
    
    def Fahrenheit(self):
        return 9/5 * (self.K - 273) + 32

A = Kelvin(69)
print(f" Suhu Celciusnya : {A.Celcius()}")
print(f" Suhu Reamurnya : {A.Reamur()}")
print(f" Suhu Fahrenheitnya : {A.Fahrenheit()}")