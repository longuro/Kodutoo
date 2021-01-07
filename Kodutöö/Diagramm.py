import numpy as np
import matplotlib.pyplot as plt

fail=open("data.txt","r")
mas1=[]
mas2=[]
for line in file
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
file.close()

title = "IKT turvameetodite kasutamise osatähtsus ettevõttes, 2018"

fig, ax = plt.subplots(ncols=1)
fig.canvas.set_window_title(title)
fig.suptitle(title)

ax.set_xlabel("%")
ax.set_ylabel("Nimi")
values = [x[1] for x in data]
tick_label = [x[0] for x in data]

ax.barh(values, tick_label, 0.7, color="#b32b0e")

plt.show()
