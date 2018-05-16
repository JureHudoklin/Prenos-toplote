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
    if cas > 5 or cas < 19:
        return funkcija_sevanja_S(cas)
    else:
        return 0

cas_sevanje_W = np.arange(12,20,1)
sevanje_W = np.array([0,300,520,700,820,800,500,0])
funkcija_sevanja_W = interpolate.InterpolatedUnivariateSpline(cas_sevanje_W,sevanje_W)
def fun_sevanje_W(cas):
    if cas > 12 or cas < 19:
        return funkcija_sevanja_W(cas)
    else:
        return 0

test = np.linspace(12,19,500)
#plt.plot(test,funkcija_sevanja_W(test))
#plt.show()



#temperature = pd.read_csv("dnevne-temp-julij.csv", delim_whitespace=True, parse_dates=True)
#print(temperature)

cas_sevanje_E = np.arange(5,14,1)
sevanje_E = np.array([0,350,700,820,700,550,350,100,0])
funkcija_sevanja_E = interpolate.InterpolatedUnivariateSpline(cas_sevanje_E, sevanje_E)
def fun_sevanje_E(cas):
    if cas > 4 or cas < 13:
        return funkcija_sevanja_E(cas)
    else:
        return 0



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
T_nes2 = 19
T_nes1 = 35
ϵ_2 = 0.9
ϵ_1 = 0.9
sevanje = 800
σ = 5.67 * 10**-8


def tem_stena_not(n, tem, trenutni_cas, λ, α, ρ, c):
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

def temp_stena_zun(n, tem, trenutni_cas, λ, α, ρ, c):
    """
    sevanje + konvekcija + prevod
    :return:
    """
    #print((λ*(tem[n-1]-tem[n])*δ_x +α*δ_x**2 *(T_nes1-tem[n])+ϵ_1*σ*δ_x**2 *((T_nes1+273)**4 - (tem[n]+273)**4) + sevanje*(1-reflektivnost_m)*δ_x**2))
    T_nova = (δ_t*3600/(ρ*δ_x**3 * c))*(λ*(tem[n-1]-tem[n])*δ_x +α*δ_x**2 *(T_nes1-tem[n])+
                                   ϵ_1*σ*δ_x**2 *((T_nes1+273)**4 - (tem[n]+273)**4) + sevanje*(1-reflektivnost_b)*δ_x**2) +tem[n]
    #tok_v_hiso = α*δ_x**2 *(T_nes2*tem[n])+ ϵ_2*σ*δ_x**2 *(T_nes2**4 - tem[n]**4
    return T_nova







temperature = np.array([19,22,23,23,24,24,24,25,25])
temperature_nove = np.zeros(9)
trenutni_cas = 5

while trenutni_cas < 19:
    for n,_ in enumerate(temperature):
        if n == 0:
            temperature_nove[n], tok = tem_stena_not(n, temperature, trenutni_cas, prevodnost_2, alfa_notranji, ρ_not, c_notranji)
        elif n == 4:
            _ = (ρ_not+ ρ_zun)/2
            temperature_nove[n] = temp_sredina(n, temperature, prevodnost_1, prevodnost_2 , _, c_zunanji, c_notranji)
        elif n < 4:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_2, ρ_not, c_notranji)
        elif n == 8:
            temperature_nove[n] = temp_stena_zun(n, temperature, trenutni_cas, prevodnost_1, alfa_zunanji, ρ_zun, c_zunanji)
        elif n > 4:
            temperature_nove[n] = temp_notranja(n, temperature, prevodnost_1, ρ_zun, c_zunanji)
    temperature = temperature_nove
    temperature_nove = np.zeros(9)
    trenutni_cas += 0.001
    print(tok)
    print(temperature)