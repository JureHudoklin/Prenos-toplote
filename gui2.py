import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
from tkinter import *
import sys
import PT_konstante as pt
import pygame


def test(temperature_N,temperature_S,temperature_E,temperature_W,trenutni_cas):
    return


def izris(temperature_N,temperature_S,temperature_E,temperature_W):
    vel_cs = 10
    vel_ch = 10
    celice = 9
    st_celic = 50
    for x in range(0, st_celic):
        for n in range(0, 9):
            # print(self.temperature_N,"temperature")
            # print(n)
            t_max = 50
            t_min = 18

            _ = temperature_N[n]
            c_N = (_-t_min)/(t_max-t_min)
            mycolor_N = round(255 * c_N, -1)
            mycolor_N = (mycolor_N,255-mycolor_N,0)
            _ = temperature_S[n]
            c_S = (_-t_min)/(t_max-t_min)
            mycolor_S = round(255 * c_S, -1)
            mycolor_S = (mycolor_S, 255 - mycolor_S, 0)
            _ = temperature_E[n]
            c_E = (_-t_min)/(t_max-t_min)
            mycolor_E = round(255 * c_E, -1)
            mycolor_E = (mycolor_E, 255 - mycolor_E, 0)
            _ = temperature_W[n]
            c_W = (_-t_min)/(t_max-t_min)
            mycolor_W = round(255 * c_W, -1)
            mycolor_W = (mycolor_W, 255 - mycolor_W, 0)

            stran_odmik = 150
            plus_x = vel_ch * celice + stran_odmik
            plus_y = vel_ch * celice + stran_odmik
            x0 = plus_x + x * vel_cs
            y0 = stran_odmik + (celice - n - 1) * vel_ch
            x1 = plus_x + (x + 1) * vel_cs
            y1 = stran_odmik + (celice - n) * vel_ch

            x2 = plus_x + x * vel_cs
            y2 = plus_y + (st_celic + n) * vel_cs
            x3 = plus_x + (x + 1) * vel_cs
            y3 = plus_y + (st_celic + n + 1) * vel_cs

            x5 = stran_odmik + (celice - n - 1) * vel_ch
            y5 = plus_y + x * vel_cs
            x6 = stran_odmik + (celice - n) * vel_ch
            y6 = plus_y + (x + 1) * vel_cs

            x8 = plus_x + (st_celic + n) * vel_cs
            y8 = plus_y + x * vel_cs
            x9 = plus_x + (st_celic + n + 1) * vel_cs
            y9 = plus_y + (x + 1) * vel_cs

            pygame.draw.rect(gameDisplay, mycolor_N, [x0, y0, vel_cs, vel_ch])
            pygame.draw.rect(gameDisplay, mycolor_S, [x2, y2, vel_cs, vel_ch])
            pygame.draw.rect(gameDisplay, mycolor_E, [x8, y8, vel_cs, vel_ch])
            pygame.draw.rect(gameDisplay, mycolor_W, [x5, y5, vel_cs, vel_ch])


def game_loop():
    temperature_N = np.array([19, 20, 23, 23, 40, 24, 28, 32, 40])
    temperature_S = np.array([19, 22, 23, 23, 24, 24, 24, 25, 10])
    temperature_E = np.array([19, 22, 23, 40, 24, 24, 24, 25, 20])
    temperature_W = np.array([19, 22, 23, 23, 24, 24, 24, 25, 25])
    dan = 0
    trenutni_cas = 12
    on = True
    delaj = False
    while on:
        if delaj:
            _, temperature_N = pt.nove_N(temperature_N, trenutni_cas)
            _, temperature_S = pt.nove_S(temperature_S, trenutni_cas)
            _, temperature_W = pt.nove_W(temperature_W, trenutni_cas)
            _, temperature_E = pt.nove_E(temperature_E, trenutni_cas)
            trenutni_cas += 0.001
            gameDisplay.fill(white)
            izris(temperature_N, temperature_S, temperature_E, temperature_W)
            # test(temperature_N,temperature_S,temperature_E,temperature_W,trenutni_cas)
            print(trenutni_cas)
            print(temperature_N[-1],temperature_S[-1],temperature_E[-1],temperature_W[-1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.KEYDOWN:
                #print(pygame.key.get_pressed())
                if event.key == pygame.K_RIGHT:
                    delaj = True
            if event.type == pygame.KEYUP:
                #print(pygame.key.get_pressed())
                if event.key == pygame.K_RIGHT:
                    delaj = False



        pygame.display.update()
        clock.tick(100)

pygame.init()
white = (255,255,255)
black = (0,0,0)



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
σ = 5.67 * 10 ** -8
vel_cs = 10
vel_ch = 10
celice = 9
st_celic = 50


display_width = 1700
display_height = 1700

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SIMULACIJA")
clock = pygame.time.Clock()
game_loop()
pygame.quit()
quit()
