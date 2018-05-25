import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate
from tkinter import *
import sys
import PT_konstante as pt
import pygame





def izris(temperature_N,temperature_S,temperature_E,temperature_W, temperature_UP):

    for x in range(0, st_celic):
        for n in range(0, 9):
            # print(self.temperature_N,"temperature")
            # print(n)

            _ = temperature_UP[n]
            c_UP = (_-t_min)/(t_max-t_min)
            mycolor_UP = round(255 * c_UP, -1)
            mycolor_UP = (mycolor_UP, 255 - mycolor_UP, 0)

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

            x9 = plus_x
            y9 = 100+vel_ch*(celice-n)

            x0 = plus_x + x * vel_cs
            y0 = stran_odmik + (celice - n - 1) * vel_ch
            #x1 = plus_x + (x + 1) * vel_cs
            #y1 = stran_odmik + (celice - n) * vel_ch

            x2 = plus_x + x * vel_cs
            y2 = plus_y + (st_celic * vel_cs+ n*vel_ch)
            #x3 = plus_x + (x + 1) * vel_cs
            #y3 = plus_y + (st_celic + n + 1) * vel_cs

            x5 = stran_odmik + (celice - n - 1) * vel_ch
            y5 = plus_y + x * vel_ch
            #x6 = stran_odmik + (celice - n) * vel_ch
            #y6 = plus_y + (x + 1) * vel_cs

            x8 = plus_x + (st_celic*vel_cs + n * vel_ch)
            y8 = plus_y + x * vel_ch
            #x9 = plus_x + (st_celic + n + 1) * vel_cs
            #y9 = plus_y + (x + 1) * vel_cs

            pygame.draw.rect(gameDisplay, mycolor_UP, [x9, y9, vel_cs, vel_ch])
            pygame.draw.rect(gameDisplay, black, [x9, 110, vel_cs, vel_ch*celice], 2)

            pygame.draw.rect(gameDisplay, mycolor_N, [x0, y0, vel_cs, vel_ch])
            pygame.draw.rect(gameDisplay, mycolor_S, [x2, y2, vel_cs, vel_ch])
            pygame.draw.rect(gameDisplay, mycolor_E, [x8, y8, vel_ch, vel_cs])
            pygame.draw.rect(gameDisplay, mycolor_W, [x5, y5, vel_ch, vel_cs])

        pygame.draw.lines(gameDisplay, black, True, tocke_linije, 4)
        T_surN = myfont.render(f"T_sN={round(temperature_N[8],2)}", False, (0, 0, 0))
        T_surS = myfont.render(f"T_sS={round(temperature_S[8],2)}", False, (0, 0, 0))
        T_surE = myfont.render(f"T_sW={round(temperature_W[8],2)}", False, (0, 0, 0))
        T_surW = myfont.render(f"T_sE={round(temperature_E[8],2)}", False, (0, 0, 0))
        T_surUP = myfont.render(f"T_sUP={round(temperature_UP[8],2)}", False, (0, 0, 0))
        streha = myfont.render(f"Streha:", False, (0, 0, 0))

        gameDisplay.blit(T_surN, ( plus_x+100, stran_odmik-26))
        gameDisplay.blit(T_surS, ( plus_x+100, plus_y + (st_celic*vel_cs + celice * vel_ch)))
        gameDisplay.blit(T_surE, (stran_odmik/2, plus_y+100))
        gameDisplay.blit(T_surW, (plus_x + (st_celic * vel_cs + celice * vel_ch), plus_y+100))
        gameDisplay.blit(T_surUP, (x9, 80))
        gameDisplay.blit(streha, (x9-80, 130))

def grafi(plot_tok, plot_Ts_inS, plot_Ts_outS,plot_Ts_inN,plot_Ts_outN,plot_Ts_inW,plot_Ts_outW,plot_Ts_inE,plot_Ts_outE,plot_Ts_inUP,plot_Ts_outUP):
    plot_cas = np.arange(0.1, 24.1, 0.1)
    skupna_moc = integrate.trapz(plot_tok, dx = 0.001*3600)
    print(skupna_moc)

    fig = plt.figure()
    fig.clf()

    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)


    ax1.plot(plot_cas, plot_Ts_inS, label="Ts_S")
    ax1.plot(plot_cas, plot_Ts_inE, label="Ts_E")
    ax1.plot(plot_cas, plot_Ts_inW, label="Ts_W")
    ax1.plot(plot_cas, plot_Ts_inN, label="Ts_N")
    ax1.plot(plot_cas, plot_Ts_inUP, label="Ts_UP")

    ax2.plot(plot_cas, plot_Ts_outS, label="Ts_S")
    ax2.plot(plot_cas, plot_Ts_outE, label="Ts_E")
    ax2.plot(plot_cas, plot_Ts_outW, label="Ts_W")
    ax2.plot(plot_cas, plot_Ts_outN, label="Ts_N")
    ax2.plot(plot_cas, plot_Ts_outUP, label="Ts_UP")

    ax3.plot(plot_cas,plot_tok, label="tok")
    ax1.set_title("Temperatura notranje stene")
    ax2.set_title("Temperatura zunanje stene")
    ax3.set_title("Toplotni tok klimatske naprave")
    fig.suptitle('CC   refleksivnost = 0.2')
    ax1.set_xlabel("t[h]")
    ax1.set_ylabel("T[C]")
    ax2.set_xlabel("t[h]")
    ax2.set_ylabel("T[C]")
    ax3.set_xlabel("t[h]")
    ax3.set_ylabel("tok[W]")

    ax1.set_xlim(0, 24)
    ax2.set_xlim(0, 24)
    ax3.set_xlim(0, 24)
    ax3.legend()
    ax1.legend()
    ax2.legend()

    plt.tight_layout()
    plt.savefig("grafi2.jpg", dpi=500)
    plt.show()


def game_loop():
    temperature_UP = np.array([19, 22, 23, 23, 24, 24, 24, 25, 20])
    temperature_N = np.array([19, 20, 23, 23, 30, 24, 28, 32, 30])
    temperature_S = np.array([19, 22, 23, 23, 24, 24, 24, 25, 20])
    temperature_E = np.array([19, 22, 23, 30, 24, 24, 24, 25, 20])
    temperature_W = np.array([19, 22, 23, 23, 24, 24, 24, 25, 25])
    dan = 0
    trenutni_cas = 8
    on = True
    delaj = False
    gameDisplay.fill(white)
    pogoj = 0
    kontrastna = (255,255,255)
    plot_tok = np.array([])
    plot_Ts_inS = np.array([])
    plot_Ts_outS = np.array([])
    plot_Ts_inE = np.array([])
    plot_Ts_outE = np.array([])
    plot_Ts_inW = np.array([])
    plot_Ts_outW = np.array([])
    plot_Ts_inN = np.array([])
    plot_Ts_outN = np.array([])
    plot_Ts_inUP = np.array([])
    plot_Ts_outUP = np.array([])


    while on:
        if delaj:
            if trenutni_cas >= 24:
                trenutni_cas = 0
                dan += 1
            tok = 0
            _, temperature_N = pt.nove_N(temperature_N, trenutni_cas)
            tok += _
            _, temperature_S = pt.nove_S(temperature_S, trenutni_cas)
            tok += _
            _, temperature_W = pt.nove_W(temperature_W, trenutni_cas)
            tok += _
            _, temperature_E = pt.nove_E(temperature_E, trenutni_cas)
            tok += _
            _, temperature_UP = pt.nove_UP(temperature_UP, trenutni_cas)
            tok += _
            trenutni_cas += 0.001
            _ = pt.fn_temperatura(trenutni_cas)
            _ = (_-t_min)/(t_max-t_min)
            _ = round(255 * _, -1)
            kontrastna = ((255 - _, 255 - _, 255 - _))
            _ = (_, 255-_,0)

            gameDisplay.fill((_))
            pygame.draw.rect(gameDisplay, (50, 50, 255), (plus_x, plus_y, st_celic * vel_cs, st_celic * vel_cs))

            pygame.draw.polygon(gameDisplay,black, tocke_poligon1)
            pygame.draw.polygon(gameDisplay, black, tocke_poligon2)
            pygame.draw.polygon(gameDisplay, black, tocke_poligon3)
            pygame.draw.polygon(gameDisplay, black, tocke_poligon4)

            izris(temperature_N, temperature_S, temperature_E, temperature_W, temperature_UP)
                # test(temperature_N,temperature_S,temperature_E,temperature_W,trenutni_cas)
                #print(trenutni_cas)
                #print(temperature_N[1],temperature_S[-1],temperature_E[-1],temperature_W[-1])
            tok = tok * povrsina*-1
            pygame.draw.rect(gameDisplay, black, (200, 0, tok/10, 20))
            text_tok = myfont2.render(f"Tok={round(tok,-1)}", False, black)
            gameDisplay.blit(text_tok,(200,22))
            #print(dan)
            if dan == 1:
                if round(trenutni_cas,4) == round(trenutni_cas, 1):
                    plot_tok = np.append(plot_tok, tok)
                    plot_Ts_inS = np.append(plot_Ts_inS, temperature_S[0])
                    plot_Ts_outS = np.append(plot_Ts_outS, temperature_S[-1])
                    plot_Ts_inN = np.append(plot_Ts_inN, temperature_N[0])
                    plot_Ts_outN = np.append(plot_Ts_outN, temperature_N[-1])
                    plot_Ts_inE = np.append(plot_Ts_inE, temperature_E[0])
                    plot_Ts_outE = np.append(plot_Ts_outE, temperature_E[-1])
                    plot_Ts_inW = np.append(plot_Ts_inW, temperature_W[0])
                    plot_Ts_outW = np.append(plot_Ts_outW, temperature_W[-1])
                    plot_Ts_inUP = np.append(plot_Ts_inUP, temperature_UP[0])
                    plot_Ts_outUP = np.append(plot_Ts_outUP, temperature_UP[-1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                grafi(plot_tok, plot_Ts_inS, plot_Ts_outS,plot_Ts_inN,plot_Ts_outN,plot_Ts_inW,plot_Ts_outW,plot_Ts_inE,plot_Ts_outE,plot_Ts_inUP,plot_Ts_outUP)
                on = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if pogoj == 0:
                        pogoj = 1
                        delaj = True
                    else:
                        delaj = False
                        pogoj = 0


        text_cas = myfont2.render(f"Cas={round(trenutni_cas,1)}", False, black)
        gameDisplay.blit(text_cas, (0,0))
        text_Tin = myfont2.render(f"T_in={round(T_nes2,1)}", False, black)
        gameDisplay.blit(text_Tin, (plus_x+st_celic*vel_cs/2, plus_y+st_celic*vel_cs/2))
        text_T_nes = myfont2.render(f"T_nes={round(pt.fn_temperatura(trenutni_cas),1)}", False, black)
        gameDisplay.blit(text_T_nes,(0,30))








        pygame.display.update()
        clock.tick(300)

pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.

white = (255,255,255)
black = (0,0,0)


povrsina = 200*100*4
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
T_nes2 = 20
T_nes1 = 35
ϵ_2 = 0.9
ϵ_1 = 0.9
sevanje = 800
σ = 5.67 * 10 ** -8
vel_cs = 500
vel_ch = 10
celice = 9
st_celic = 1
stran_odmik = 250
display_width = 1080
display_height = 1080
t_max = 43
t_min = 15


myfont = pygame.font.SysFont('Arial', 25)
myfont2 = pygame.font.SysFont('Arial', 30)
plus_x = vel_ch * celice + stran_odmik
plus_y = vel_ch * celice + stran_odmik
tocke_linije = [(plus_x, stran_odmik),(plus_x+st_celic*vel_cs, stran_odmik),
                (plus_x+st_celic*vel_cs+celice*vel_ch, plus_y), (plus_x+st_celic*vel_cs+celice*vel_ch, plus_y+st_celic*vel_cs),
                (plus_x+st_celic*vel_cs,plus_y+st_celic*vel_cs+celice*vel_ch),(plus_x,plus_y+st_celic*vel_cs+celice*vel_ch),
                (stran_odmik, plus_y+st_celic*vel_cs),(stran_odmik,plus_y)]
tocke_poligon1 = [(stran_odmik,plus_y),(plus_x,plus_y),(plus_x,stran_odmik)]
tocke_poligon2 = [(plus_x+st_celic*vel_cs,plus_y),(plus_x+st_celic*vel_cs+celice*vel_ch,plus_y),(plus_x+st_celic*vel_cs,stran_odmik)]
tocke_poligon3 = [(plus_x+st_celic*vel_cs,plus_y+st_celic*vel_cs),(plus_x+st_celic*vel_cs+celice*vel_ch,plus_y+st_celic*vel_cs),(plus_x+st_celic*vel_cs,plus_y+st_celic*vel_cs+celice*vel_ch)]
tocke_poligon4 = [(stran_odmik,plus_y+st_celic*vel_cs),(plus_x,plus_y+st_celic*vel_cs),(plus_x,plus_y+st_celic*vel_cs+celice*vel_ch)]

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SIMULACIJA")
clock = pygame.time.Clock()
game_loop()
pygame.quit()
print("neki")

quit()

