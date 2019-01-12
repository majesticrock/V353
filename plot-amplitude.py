import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return 1 / np.sqrt(b + x**2 * a**2)

werte = csv_read("csv/variable-frequenz.csv")
xdata = np.zeros(28)
ydata = np.zeros(28)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0]) * 2 * np.pi
        ydata[i] = float(values[1]) / 15.2
        i+=1

x_line = np.append([np.linspace(10, 100), np.linspace(100, 1000)], np.linspace(1000, 10000)) * 2 * np.pi

plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(pcov))

plt.xscale('log')
plt.xlabel(r"$\omega$ / $\frac{1}{s}$")
plt.ylabel(r"$\frac{U_C}{U_0}$")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-amplitude.pdf")