import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#Задание №1
title = "IKT turvameetodite kasutamise osatähtsus ettevõttes, 2018"

fig, ax = plt.subplots(ncols=1)
fig.canvas.set_window_title(title)
fig.suptitle(title +
             "https://vana.stat.ee/pressiteade-2019-111")

ax.set_xlabel("%")
ax.set_ylabel("Nimi")

#https://vana.stat.ee/pressiteade-2019-111
data = [
    [6.6, 'Kasutaja tuvastamine biomeetriliste meetoditega'],
    [24.9, 'IKT riskianalüüside teostamine'],
    [28.8, 'IKT turvatestid'],
    [30.2, 'Andmete, dokumentide, e-kirjade krüpteerimine'],
    [35.8, 'Turvaintsidendi logifailide kopeerimine ja säilitamine analüüsiks'],
    [39.9, 'VPN-i kasutamine'],
    [60, 'Võrgujuurdepääsu kontroll'],
    [61.1, 'Tugev paroolide autentimine'],
    [64.6, 'Andmete varundamine eraldi keskkonda'],
    [70.7, 'Tarkvara värskemate versioonide kasutamine'],
    [86.1, 'Erinevate IKT turvameetodite kasutamine']
]

values = [x[1] for x in data]
tick_label = [x[0] for x in data]

ax.barh(values, tick_label, 0.7, color="#b32b0e")

plt.show()

#Задание №2
#ОЧКо(Очки)
x1 = np.arange(-9, -1, 0.01)
x2 = np.arange(1, 9, 0.01)
x3 = np.arange(-9, -1, 0.01)
x4 = np.arange(1, 9, 0.01)
x5 = np.arange(-9, -6, 0.01)
x6 = np.arange(6, 9, 0.01)
x7 = np.arange(-1, 1, 0.01)

y1 = (-0.0625*((x1+5)**2)+2)
y2 = (-0.0625*((x2-5)**2)+2)
y3 = (0.25*((x3+5)**2)-3)
y4 = (0.25*((x4-5)**2)-3)
y5 = (-((x5+7)**2)+5)
y6 = (-((x6-7)**2)+5)
y7 = (-0.5*(x7**2)+1.5)

plt.subplots()
plt.grid(True)
plt.plot(x1, y1, 'b', linewidth=1)
plt.plot(x2, y2, 'b', linewidth=1)
plt.plot(x3, y3, 'b', linewidth=1)
plt.plot(x4, y4, 'b', linewidth=1)
plt.plot(x5, y5, 'b', linewidth=1)
plt.plot(x6, y6, 'b', linewidth=1)
plt.plot(x7, y7, 'b', linewidth=1)

plt.show()