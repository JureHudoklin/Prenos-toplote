import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
from tkinter import *
import sys
import PT_konstante as pt
import pygame


class Gui():

    def __init__(self, master):
        #frame_top = Frame(master)  #glavni frame za gumbe
        self.canvas = Canvas(master, width=1700, height=1716)  #glavni frame za grafiko
        self.canvas.pack()
        self.dan = 0
        self.trenutni_cas = 5

        self.ρ_not = 1200
        self.ρ_zun = 12
        self.δ_x = 0.03
        self.δ_t = 0.001
        self.c_notranji = 880
        self.c_zunanji = 1300
        self.prevodnost_1 = 0.04
        self.prevodnost_2 = 2
        self.alfa_notranji = 10
        self.alfa_zunanji = 50
        self.T_nes2 = 19
        self.T_nes1 = 35
        self.ϵ_2 = 0.9
        self.ϵ_1 = 0.9
        self.sevanje = 800
        self.σ = 5.67 * 10 ** -8
        self.vel_cs = 10
        self.vel_ch = 10
        self.celice = 9
        self.st_celic = 50
        self.temperature_N = np.array([19, 20, 23, 23, 24, 24, 28, 32, 38])
        self.temperature_S = np.array([19, 22, 23, 23, 24, 24, 24, 25, 25])
        self.temperature_E = np.array([19, 22, 23, 23, 24, 24, 24, 25, 20])
        self.temperature_W = np.array([19, 22, 23, 23, 24, 24, 24, 25, 25])
        """
        if self.trenutni_cas < 6:
            self.test()
            print("neki")
            self.izris()
            self.trenutni_cas += 0.001
            # print(trenutni_cas)
        else:
            self.dan += 1
            self.trenutni_cas = 0
        """
        trenutni_cas = 5

        self.st_dni = 1
        self.dan = 0
        #self.canvas.create_line(0, 0, 200, 100)
        #self.canvas.create_rectangle(0,0,100,100, fill="red")
        #self.test()
        self.zagon()

    def zagon(self):
        while self.dan < self.st_dni:
            if self.trenutni_cas < 6:
                self.test()
                print("neki")
                self.izris()
                self.trenutni_cas += 0.001
                # print(trenutni_cas)
            else:
                self.dan += 1
                self.trenutni_cas = 0


    def test2(self):
        print("neki")

    def test(self):
            _, self.temperature_N = pt.nove_N(self.temperature_N, self.trenutni_cas)
            _,self.temperature_S = pt.nove_N(self.temperature_S, self.trenutni_cas)
            _,self.temperature_E = pt.nove_N(self.temperature_E, self.trenutni_cas)
            _,self.temperature_W = pt.nove_N(self.temperature_W, self.trenutni_cas)
            self.trenutni_cas += 0.001
            self.izris()

    def izris(self):
        self.canvas.clipboard_clear()
        vel_cs = 10
        vel_ch = 10
        celice = 9
        st_celic = 50
        for x in range(0, st_celic):
            for n in range(0,9):
                #print(self.temperature_N,"temperature")
                #print(n)
                _ = int(self.temperature_N[n])
                c_N = (255 - (_ - 19) * 5, 0 + (_ - 19) * 5, 0)
                _ = int(self.temperature_S[n])
                c_S = (255 - (_ - 19) * 5, 0 + (_ - 19) * 5, 0)
                _ = int(self.temperature_E[n])
                c_E = (255 - (_ - 19) * 5, 0 + (_ - 19) * 5, 0)
                _ = int(self.temperature_W[n])
                c_W = (255 - (_ - 19) * 5, 0 + (_ - 19) * 5, 0)
                mycolor_N = '#%02x%02x%02x' % c_N
                mycolor_S = '#%02x%02x%02x' % c_S
                mycolor_E = '#%02x%02x%02x' % c_E
                mycolor_W = '#%02x%02x%02x' % c_W

                stran_odmik =300
                plus_x = vel_ch*celice +stran_odmik
                plus_y = vel_ch*celice +stran_odmik
                x0 = plus_x + x*vel_cs
                y0 = stran_odmik + (celice-n-1)*vel_ch
                x1 = plus_x + (x+1)*vel_cs
                y1 = stran_odmik + (celice-n)*vel_ch

                x2 = plus_x + x*vel_cs
                y2 = plus_y + (st_celic+n)* vel_cs
                x3 = plus_x + (x+1)*vel_cs
                y3 = plus_y + (st_celic+n+1)* vel_cs

                x5 = stran_odmik +(celice-n-1)*vel_ch
                y5 = plus_y + x*vel_cs
                x6 = stran_odmik +(celice-n)*vel_ch
                y6 = plus_y + (x+1)*vel_cs

                x8 = plus_x +(st_celic+n)* vel_cs
                y8 = plus_y + x*vel_cs
                x9 = plus_x + (st_celic+n+1)* vel_cs
                y9 = plus_y + (x+1)*vel_cs

                self.canvas.create_rectangle(x0,y0,x1,y1, fill=mycolor_N)
                self.canvas.create_rectangle(x2,y2,x3,y3, fill=mycolor_S)
                self.canvas.create_rectangle(x5, y5, x6, y6, fill=mycolor_W)
                self.canvas.create_rectangle(x8, y8, x9, y9, fill=mycolor_E)
        self.canvas.update()

root = Tk()
okno = Gui(root)
root.mainloop()

dan = 0
st_dni = 1
trenutni_cas = 5
"""
while dan < st_dni:
    if trenutni_cas < 6:
        okno.test()
        print("neki")
        #okno.izris()
        trenutni_cas += 0.001
        #print(trenutni_cas)
    else:
        dan += 1
        trenutni_cas = 0
"""
