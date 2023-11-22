# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:42:59 2023

@author: kathr
"""

import random
import tkinter as tk

impath = '/Users/kathr/OneDrive/Desktop/Multimedia/FinalProject/desktop-turtle/'

window = tk.Tk()

#Get image
img = tk.PhotoImage(file = impath+'idle.gif')

#Resize image
img = img.zoom(3)
img = img.subsample(14)

#Display image
label = tk.Label(image = img)
#label.image = img
label.pack()

window.mainloop()
