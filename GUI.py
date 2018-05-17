import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
from tkinter import *
import sys
import PT_konstante as pt

ρ_not = 1200
ρ_zun = 12
δ_x = 0.03
δ_t = 0.001
c_notranji = 880
c_zunanji = 1300
prevodnost_1 = 0.04
prevodnost_2 = 2
alfa_notranji = 10
alfa_zunanji = 50
T_nes2 = 19
T_nes1 = 35
ϵ_2 = 0.9
ϵ_1 = 0.9
sevanje = 800
σ = 5.67 * 10**-8

temperature_N = np.array([19,20,23,23,24,24,28,32,38])
temperature_S = np.array([19,22,23,23,24,24,24,25,25])
temperature_E = np.array([19,22,23,23,24,24,24,25,20])
temperature_W = np.array([19,22,23,23,24,24,24,25,25])
temperature_nove = np.zeros(9)
trenutni_cas = 5
vel_cs = 4
vel_ch = 10

class Gui():

    def __init__(self, master):
        #frame_top = Frame(master)  #glavni frame za gumbe
        self.canvas = Canvas(master, width=1016, height=1716)  #glavni frame za grafiko
        self.canvas.pack()

        #self.canvas.create_line(0, 0, 200, 100)
        #self.canvas.create_rectangle(0,0,100,100, fill="red")
        sprem_1 = 108
        for x in range(8,sprem_1):
            x += 1
            for n in range(0,9):
                _ = temperature_N[n]
                c_N = (255 - (_-19)*13 , 0+(_-19)*13, 0)
                _ = temperature_S[n]
                c_S = (255 - (_ - 19) * 13, 0 + (_ - 19) * 13, (_ - 19) * 13)
                _ = temperature_E[n]
                c_E = (255 - (_ - 19) * 13, 0 + (_ - 19) * 13, (_ - 19) * 13)
                _ = temperature_W[n]
                c_W = (255 - (_ - 19) * 13, 0 + (_ - 19) * 13, (_ - 19) * 13)
                mycolor_N = '#%02x%02x%02x' % c_N
                print(mycolor_N)
                mycolor_S = '#%02x%02x%02x' % c_S
                mycolor_E = '#%02x%02x%02x' % c_E
                mycolor_W = '#%02x%02x%02x' % c_W

                self.canvas.create_rectangle((vel_ch-vel_cs)*9+x*vel_cs, n*vel_ch, (vel_ch-vel_cs)*9+x*vel_cs+vel_cs,n*vel_ch+vel_ch, fill=mycolor_N)

                self.canvas.create_rectangle((vel_ch - vel_cs) * 9 + x * vel_cs, sprem_1*vel_cs+n * vel_ch,
                                             (vel_ch - vel_cs) * 9 + x * vel_cs + vel_cs,
                                             sprem_1 * vel_cs+ n * vel_ch + vel_ch,
                                             fill=mycolor_N)

                self.canvas.create_rectangle(n*vel_ch,(vel_ch-vel_cs)*9+x*vel_cs, n*vel_ch+vel_ch, (vel_ch-vel_cs)*9+x*vel_cs+vel_cs, fill=mycolor_W)
                self.canvas.create_rectangle(sprem_1*vel_cs+n * vel_ch, (vel_ch - vel_cs) * 9 +
                                             + x * vel_cs, sprem_1*vel_cs+n * vel_ch + vel_ch,
                                             (vel_ch - vel_cs) * 9 + x * vel_cs + vel_cs, fill=mycolor_W)

root = Tk()
okno = Gui(root)
root.mainloop()



