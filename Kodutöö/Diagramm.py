import matplotlib.pyplot as plt
import numpy as np

file=open("Kodutöö/1.txt","r")
mas1=[]
mas2=[]
for line in file:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
file.close()

title = "Данные о ИТ безопасности"
plt.grid(True)

color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)

plt.show()