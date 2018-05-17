import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import tkinter as tk
import sys


temperature = np.array([19,22,23,23,24,24,24,25,25])
temperature_nove = np.zeros(9)
trenutni_cas = 5

class Gui():
    """
    class--> kreira grafični vmesnik
    """
    def __init__(self, master):
        frame_top = Frame(master)  #glavni frame za gumbe
        self.canvas = Canvas(master, width=600, height=300)  #glavni frame za grafiko
        #self.frame_NTM = Frame(master,width=300, height=800)
        #self.frame_NTM.pack(side = RIGHT)


root = Tk()
okno = Gui(root)
root.mainloop()