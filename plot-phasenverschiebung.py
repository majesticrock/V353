import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a,b):
    return np.arctan(-a*x+b)

werte = csv_read("csv/variable-frequenz.csv")
xdata = np.zeros(26)
ydata = np.zeros(26)

ignore = 3
i=0
for values in werte:
    if(ignore >= 1):
        ignore = ignore - 1
    else:
        xdata[i] = float(values[0]) * 2 * np.pi
        ydata[i] = float(values[2])*(float(values[0]) * 2 * np.pi) * 10**(-6)
        i+=1

x_line = np.append([np.linspace(10, 100), np.linspace(100, 1000)], np.linspace(1000, 10000)) * 2 * np.pi

plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(pcov))

plt.xscale('log')
plt.xlabel(r"$\omega$ / $\frac{1}{s}$")
plt.ylabel(r"$\phi$ / rad")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-phasenverschiebung.pdf")