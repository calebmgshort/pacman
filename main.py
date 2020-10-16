from tkinter import *
import center_tk_window
from PIL import ImageTk, Image
import threading
from update_and_render_module import update_and_render
from settings import objects, gui

# class Pacman:
#     def __init__(self):
#         pass

gui.title("Pacman")
gui.configure(background="black")
gui.geometry("700x700")
center_tk_window.center_on_screen(gui)


object_pacman = dict()
object_pacman["coordinates"] = (0,0)
object_pacman["velocity"] = (50,0)

image_path = "resources/pacman.png"
inner_img = Image.open(image_path)
inner_img = inner_img.resize((40,40))
outer_img = ImageTk.PhotoImage(inner_img)
object_pacman["label"] = Label(gui, image = outer_img)
object_pacman["label"].place(anchor = NW, x=0, y=0)
objects.append(object_pacman)

thread_update_and_render = threading.Thread(target=update_and_render)
# TODO: Close the started thread
# TODO: Make the objects object-oriented

# TODO: Add a thread to listen for user input from the keyboard


# Start threads
thread_update_and_render.start()


gui.mainloop()
