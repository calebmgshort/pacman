from tkinter import *
from settings import objects, stop_execution
import time

update_interval = 0.025

def update():
    for one_object in objects:
        #one_object.update()
        velocity = one_object["velocity"]
        coordinates = one_object["coordinates"]
        new_coordinates = [0,0]
        new_coordinates[0] = coordinates[0] + velocity[0] * update_interval
        new_coordinates[1] = coordinates[1] + velocity[1] * update_interval
        one_object["coordinates"] = new_coordinates
        # TODO: Only update if the coordinates are still on screen


def render():
    for one_object in objects:
        coordinates = one_object["coordinates"]
        one_object["label"].place(anchor = NW, x=coordinates[0], y=coordinates[1])
    #render_background()
    #render_objects()

def update_and_render():
    while(True):
        if stop_execution:
            return
        update()
        render()
        time.sleep(update_interval)
