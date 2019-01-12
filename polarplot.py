import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a):
    return a*np.cos(x)

werte = csv_read("csv/variable-frequenz.csv")
phi = np.zeros(26)
rdata = np.zeros(26)
fphi = np.zeros(2)
fr = np.zeros(2)
ignore = 3
i=0
j=0
for values in werte:
    if(ignore >= 1):
        if(ignore <=2):
            fphi[j] = float(values[2])*float(values[0]) * (2*np.pi) * 10**(-6)
            fr[j] = (float(values[1])/15)
            j+=1
        
        ignore = ignore - 1
    else:
        phi[i] = float(values[2])*float(values[0]) * (2*np.pi) * 10**(-6)
        rdata[i] = (float(values[1])/15)
        i+=1

phi_line = np.linspace(0,np.pi/2)

plt.polar(phi, rdata, "r.", label="Messwerte")
plt.polar(fphi, fr, "ro", label="Nicht betrachete Messwerte")
plt.polar(phi_line, np.cos(phi_line), "b-", label="Theoriekurve")

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-polar.pdf")