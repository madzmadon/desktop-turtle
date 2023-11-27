# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:42:59 2023

@author: kathr
"""

import random
import tkinter as tk

SCREEN_WIDTH = 1440 
SCREEN_HEIGHT = 900

def clamp(val, min, max):
  return min if val < min else max if val > max else val

"""
def make_draggable(widget):
    widget.bind("<Button-1>", drag_start)
    widget.bind("<B1-Motion>", drag_motion)

def drag_start(event):
    widget = event.widget
    widget.drag_start_x = event.x
    widget.drag_start_y = event.y
    
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.drag_start_x + event.x
    y = widget.winfo_y() - widget.drag_start_y + event.y
    widget.place(x = x,  y = y)
    
    widget.geometry(f"115x65+{x}+{y}")
"""
  
def move(event):
    x, y = window.winfo_pointerxy()
    window.geometry(f"+{x}+{y}")

impath = '/Users/kathr/OneDrive/Desktop/Multimedia/FinalProject/desktop-turtle/'

window = tk.Tk()

#Get image
img = tk.PhotoImage(file = impath+'idle.gif')

#Resize image
img = img.zoom(3)
img = img.subsample(14)

window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparent', 'black')
label.pack()

#Display image
label.configure(image = img)

#Drag image around
window.bind('<B1-Motion>', move)

window.mainloop()
