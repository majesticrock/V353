import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#ohne Rauschen

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b

werte = csv_read("csv/aufladen.csv")
xdata = np.zeros(13)
ydata = np.zeros(13)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = 1 - float(values[1]) / 15.2
        i+=1

x_line = np.linspace(0.28, 2.20)
ydata = np.log(ydata)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(pcov)

plt.xlabel(r"$\Delta t$ / ms")
plt.ylabel(r"$U$ / V")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-aufladen.pdf")