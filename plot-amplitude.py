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
    return (1/a) * np.sin(np.arctan(a*x)) +b

werte = csv_read("csv/variable-frequenz.csv")
xdata = np.zeros(28)
ydata = np.zeros(28)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[1]) / 15.2
        i+=1

guess = (0.8, 0.5)

x_line = np.linspace(10, 10000)

xdata = np.log(xdata)
x_line = np.log(x_line)

plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata, guess)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(pcov)

plt.xlabel(r"$\symup{ln}(\Delta t)$ / ln(ms)")
plt.ylabel(r"$U$ / V")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-amplitude.pdf")