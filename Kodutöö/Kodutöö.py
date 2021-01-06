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
