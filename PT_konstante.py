import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
# http://www.arso.gov.si/vreme/poro%C4%8Dila%20in%20publikacije/Zgibanka-trajanje_soncnega_obsevanja.pdf
# http://www.ugodnagradnja.com/index.php/izracuni/gradnja/akumulacija-materialov/
# https://www.nrel.gov/docs/legosti/old/2525.pdf

#Konstante
tp_stiropor = 0.04 #w/mK
#tp_opeka = 0.6 #w/mK
tp_beton = 2
gostota_beton = 2000

alfa_zrak = 30 #w/m**K
reflektivnost_b = 0.2
reflektivnost_n = 0.65
reflektivnost_m = 0.85 # https://www.epa.gov/sites/production/files/2014-08/documents/energy_and_buildings_volume_39_0.pdf str 3

#Definiram fucnkcijo za sevanje
cas_sevanje_S = np.arange(5,20,1)
sevanje_S = np.array([0,50,80,180,310,420,500,520,480,420,300,180,80,50,0])
funkcija_sevanja_S = interpolate.InterpolatedUnivariateSpline(cas_sevanje_S,sevanje_S)
def fun_sevanje_S(cas):
    if cas > 5 and cas < 19:
        return funkcija_sevanja_S(cas)
    else:
        return 0


test = np.linspace(0, 24, 500)
#plt.plot(test,fun_sevanje_S(test))
#plt.show()

cas_sevanje_W = np.arange(12,20,1)
sevanje_W = np.array([0,300,520,700,820,800,500,0])
funkcija_sevanja_W = interpolate.InterpolatedUnivariateSpline(cas_sevanje_W,sevanje_W)
def fun_sevanje_W(cas):
    if cas > 12 and cas < 19:
        return funkcija_sevanja_W(cas)
    else:
        return 0

#test = np.linspace(0,24,500)
#plt.plot(test,funkcija_sevanja_W(test))
#plt.show()



#temperature = pd.read_csv("dnevne-temp-julij.csv", delim_whitespace=True, parse_dates=True)
#print(temperature)

cas_sevanje_E = np.arange(5,14,1)
sevanje_E = np.array([0,350,700,820,700,550,350, 100,0])
funkcija_sevanja_E = interpolate.InterpolatedUnivariateSpline(cas_sevanje_E,sevanje_E)
def fun_sevanje_E(cas):
    if cas > 5 and cas < 13:
        return funkcija_sevanja_E(cas)

    else:
        return 0

for x in range(0,24,1):
    print(fun_sevanje_E(x))
#test = np.linspace(0, 24, 500)
#plt.plot(test,funkcija_sevanja_E(test))
#plt.plot(cas_sevanje_E,sevanje_E)
#plt.show()


"""
Celice se zacnejo steti pri notranji steni
temperatura notraj je T_nes2
Temperatura zunaj T_nes1
"""

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
ϵ_2 = 0.9
ϵ_1 = 0.9

σ = 5.67 * 10**-8


def tem_stena_not(n, tem, λ, α, ρ, c):
    """
    sevanje + konvekcija + prevod
    :return:
    """
    T_nova = (δ_t*3600/(ρ*δ_x**3 * c))*(λ*(tem[n+1]-tem[n])*δ_x +α*δ_x**2 *(T_nes2-tem[n])+ ϵ_2*σ*δ_x**2 *((T_nes2+273)**4 - (tem[n]+273)**4)) +tem[n]
    tok_v_hiso = α*δ_x**2 *(T_nes2-tem[n])+ ϵ_2*σ*δ_x**2 *((T_nes2+273)**4 - (tem[n]+273)**4)
    return T_nova, tok_v_hiso

def temp_notranja(n, tem, λ, ρ, c):
    """
    :return: 
    """
    #print(tem[n - 1] - 2 * tem[n] + tem[n + 1])
    T_nova = (δ_t*3600 / (ρ * (δ_x**3) * c)) *(λ*δ_x*(tem[n-1] - 2*tem[n] + tem[n+1])) + tem[n]
    return T_nova

def temp_sredina(n, tem, λ_1, λ_2 , ρ, c_1, c_2):
    T_nova = (δ_t*3600 / (ρ * δ_x**3 * (c_1+c_2)/2)) *(δ_x*(λ_2*(tem[n-1]-tem[n]) +λ_1*(tem[n+1]-tem[n]))) + tem[n]
    return T_nova

def temp_stena_zun(n, tem, λ, α, ρ, c, sevanje, T_nes1):
    """
    sevanje + konvekcija + prevod
    :return:
    """
    #print((λ*(tem[n-1]-tem[n])*δ_x +α*δ_x**2 *(T_nes1-tem[n])+ϵ_1*σ*δ_x**2 *((T_nes1+273)**4 - (tem[n]+273)**4) + sevanje*(1-reflektivnost_m)*δ_x**2))
    T_nova = (δ_t*3600/(ρ*δ_x**3 * c))*(λ*(tem[n-1]-tem[n])*δ_x +α*δ_x**2 *(T_nes1-tem[n])+
                                   ϵ_1*σ*δ_x**2 *((T_nes1+273)**4 - (tem[n]+273)**4) + sevanje*(1-reflektivnost_b)*δ_x**2) +tem[n]
    #tok_v_hiso = α*δ_x**2 *(T_nes2*tem[n])+ ϵ_2*σ*δ_x**2 *(T_nes2**4 - tem[n]**4
    return T_nova

#def fn_temperatura(trenutni_cas):
 #   return 38




def nove_N(temperature, trenutni_cas):
    temperature_nove = np.zeros(9)
    for m,_ in enumerate(temperature):
        if m == 0:
            temperature_nove[m], tok = tem_stena_not(m, temperature, prevodnost_2, alfa_notranji, ρ_not, c_notranji)
        elif m == 3:
            _ = (ρ_not+ ρ_zun)/2
            temperature_nove[m] = temp_sredina(m, temperature, prevodnost_1, prevodnost_2 , _, c_zunanji, c_notranji)
        elif m < 3:
            temperature_nove[m] = temp_notranja(m, temperature, prevodnost_2, ρ_not, c_notranji)
        elif m == 8:
            temperature_nove[m] = temp_stena_zun(m, temperature, prevodnost_1, alfa_zunanji, ρ_zun, c_zunanji, 0, fn_temperatura(trenutni_cas))
        elif m > 3:
            temperature_nove[m] = temp_notranja(m, temperature, prevodnost_1, ρ_zun, c_zunanji)
    return tok, temperature_nove
    #print(temperature)

def nove_S(temperature, trenutni_cas):
    #print("neki")
    temperature_nove = np.zeros(9)
    for n,_ in enumerate(temperature):
        if n == 0:
            temperature_nove[n], tok = tem_stena_not(n, temperature, prevodnost_2, alfa_notranji, ρ_not, c_notranji)
        elif n == 3:
            _ = (ρ_not+ ρ_zun)/2
            temperature_nove[n] = temp_sredina(n, temperature, prevodnost_1, prevodnost_2 , _, c_zunanji, c_notranji)
        elif n < 3:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_2, ρ_not, c_notranji)
        elif n == 8:
            temperature_nove[n] = temp_stena_zun(n, temperature, prevodnost_1, alfa_zunanji, ρ_zun, c_zunanji, fun_sevanje_S(trenutni_cas), fn_temperatura(trenutni_cas))
        elif n > 3:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_1, ρ_zun, c_zunanji)
        #print(trenutni_cas)
        #print(sevanje_S(trenutni_cas),"sevanje")
    return tok, temperature_nove



def nove_E(temperature, trenutni_cas):
    temperature_nove = np.zeros(9)
    for n, _ in enumerate(temperature):
        if n == 0:
            temperature_nove[n], tok = tem_stena_not(n, temperature,  prevodnost_2, alfa_notranji, ρ_not,
                                                     c_notranji)
        elif n == 3:
            _ = (ρ_not + ρ_zun) / 2
            temperature_nove[n] = temp_sredina(n, temperature, prevodnost_1, prevodnost_2, _, c_zunanji, c_notranji)
        elif n < 3:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_2, ρ_not, c_notranji)
        elif n == 8:
            temperature_nove[n] = temp_stena_zun(n, temperature, prevodnost_1, alfa_zunanji, ρ_zun, c_zunanji,
                                                 fun_sevanje_E(trenutni_cas), fn_temperatura(trenutni_cas))
        elif n > 3:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_1, ρ_zun, c_zunanji)
        #print(fun_sevanje_E(trenutni_cas))
    return tok, temperature_nove
    # print(tok)
    # print(temperature)


def nove_W(temperature, trenutni_cas):
    temperature_nove = np.zeros(9)
    for n, _ in enumerate(temperature):
        if n == 0:
            temperature_nove[n], tok = tem_stena_not(n, temperature, prevodnost_2, alfa_notranji, ρ_not,
                                                     c_notranji)
        elif n == 3:
            _ = (ρ_not + ρ_zun) / 2
            temperature_nove[n] = temp_sredina(n, temperature, prevodnost_1, prevodnost_2, _, c_zunanji, c_notranji)
        elif n < 3:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_2, ρ_not, c_notranji)
        elif n == 8:
            temperature_nove[n] = temp_stena_zun(n, temperature, prevodnost_1, alfa_zunanji, ρ_zun, c_zunanji,
                                                 fun_sevanje_W(trenutni_cas), fn_temperatura(trenutni_cas))
        elif n > 3:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_1, ρ_zun, c_zunanji)
    print(fun_sevanje_W(trenutni_cas))
    return tok, temperature_nove
    # print(tok)
    # print(temperature)

temperature_tabela = pd.read_excel('temperature.xlsx')
temperature_tabela = temperature_tabela.sort_values(by=['cas'])
temperature_cas = np.array(temperature_tabela['cas'])
dolzina = len(temperature_cas) // 80
temperature_cas = temperature_cas[0:dolzina * 80]
temperature_cas = temperature_cas.reshape(dolzina, 80)
temperature_cas = [np.average(x) for x in temperature_cas]

temperature_T = np.array(temperature_tabela['T'])
temperature_T = temperature_T[0:dolzina * 80]
temperature_T = temperature_T.reshape(dolzina, 80)
temperature_T = [np.average(x) for x in temperature_T]

temperature_spline = interpolate.UnivariateSpline(temperature_cas, temperature_T)

def fn_temperatura(t):
    if 0 <= t < 12:
        return temperature_spline(t) + (t/10) ** 2 * 0.25
    else:
        return temperature_spline(t) + (t/10) ** 2 * 0.25 - ((t-12)/10) ** 2 * 0.7


"""
cas_test = np.linspace(0, 24, 100)
plt.plot(temperature_cas, temperature_T, 'r.')
plt.plot(cas_test, temperature_spline(cas_test),'b')
for t in cas_test:
    print(t, dnevna_temperatura(t))
    plt.plot(t, dnevna_temperatura(t), 'go')
plt.show()
"""