#nama : ALI MABRUR MUBAROK
#nim : 210511112
#kelas : TI21C / R3

from tkinter import *
from turtle import color
from playsound import playsound

root3 = Tk()
root3.title('Aplikasi Macam - macam suara hewan')
root3.config(background="blue")

Label(root3, text="PEMUTAR SUARA JENIS - JENIS HEWAN", bg="yellow", font="Lobster 30").grid(
    row=0, column=0, columnspan=3, pady=5)

class Animal: 
    def make_sound(self): 
        print("The animal makes a sound") 
        
class Dog(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - anjing.mp3') 
        
    b1 = Button(root3, text="Anjing", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b1.grid(row=3, column=0, padx=15, pady=15)

class Cat(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - kucing.mp3')
        
    b2 = Button(root3, text="Kucing", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b2.grid(row=3, column=1, padx=15, pady=15)

class Chicken(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - ayam.mp3')

    b3 = Button(root3, text="Ayam", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b3.grid(row=3, column=2, padx=15, pady=15)

class Pig(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - babi.mp3')

    b4 = Button(root3, text="Babi", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b4.grid(row=4, column=0, padx=15, pady=15)

class Bird(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - burung.mp3')

    b5 = Button(root3, text="Burung", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b5.grid(row=4, column=1, padx=15, pady=15)

class Elephant(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - gajah.mp3')

    b6 = Button(root3, text="Gajah", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b6.grid(row=4, column=2, padx=15, pady=15)

class Sheep(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - kambing.mp3')

    b7 = Button(root3, text="Kambing", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b7.grid(row=5, column=0, padx=15, pady=15)

class Monkey(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - monyet.mp3')

    b8 = Button(root3, text="Monyet", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b8.grid(row=5, column=1, padx=15, pady=15)

class Cow(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - sapi.mp3')

    b9 = Button(root3, text="Sapi", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b9.grid(row=5, column=2, padx=15, pady=15)
    
class Lion(Animal): 
    def make_sound(): 
        playsound('D:\TUGAS FILE MANAGER (SISTEM INFORMASI)\ALI MABRUR MUBAROK\SEMESTER 4\PEMROGRAMAN BERORIENTASI OBJEK LANJUT\Pertemuan 3\Hewan\suara - singa.mp3')

    b10 = Button(root3, text="Singa", font="Normal 20", command=make_sound, relief=RAISED, bd=5, bg="lightgray", activebackground="purple")
    b10.grid(row=6, column=1, padx=15, pady=15)

def animal_sound(animal): 
    animal.make_sound() 

root3.mainloop()