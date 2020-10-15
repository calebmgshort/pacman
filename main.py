from tkinter import *
import center_tk_window
from PIL import ImageTk, Image

class Pacman:
    def __init__(self):
        pass
    
    

gui = Tk()
gui.title("Pacman")
gui.configure(background="black")
gui.geometry("800x800")


#pacman = Pacman()
image_path = "resources/pacman.png"
inner_img = Image.open(image_path)
inner_img = inner_img.resize((40,40))
outer_img = ImageTk.PhotoImage(inner_img)
panel = Label(gui, image = outer_img)
panel.pack()

#button = Button(top, text='Stop', width=25, command=top.destroy) 
#button.pack()

center_tk_window.center_on_screen(gui)
gui.mainloop()