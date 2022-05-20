from tkinter import *     
import os

class kowal():
    def __init__(self) -> None:
        pass
# -----------------------------------------------------------------------------------
    def services(self):
        print("---"*30)
        print("Witaj wedrowcze!!! Jak moge ci pomoc?")
        print("a - Chcę ulepszyć Broń")
        print("c - company")
        print("---"*30)
# -----------------------------------------------------------------------------------
    def Broń(self,player):
        if player.goold >= 200:
            player.attack += 5
            player.goold -=200
            print("Oto oręż najlepszej jakości specjalnie dla ciebie")
            print(f"Zapłacono 50 zlota | obecnie masz {player.goold}")
        else:
            print("Nie masz wystarczajacej ilosci zlota ")

# -----------------------------------------------------------------------------------
    def towarzystwo(self):
        root = Tk()      
        canvas = Canvas(root, width = 500, height = 500.)      
        canvas.pack()    
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'bbbb.gif')  
        img = PhotoImage(file=image_path)      
        canvas.create_image(350,350, anchor=NW, image=img)   
        mainloop()

    
