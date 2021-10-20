import matplotlib.pyplot as plt
import numpy as np
g=1.4

plt.subplot(2,1,1)
plt.grid()
r=np.linspace(4,15)
for rp in range(2,5):
    eff=1-(g*(pow(rp,1/g)-1)/(pow(r,g-1)*(rp-1)))
    plt.plot(r,eff)
plt.xlabel("Compression Rati")
plt.ylabel("Efficiency")

plt.subplot(2,1,2)
plt.grid()
rp1=np.linspace(2,5)
for r1 in range(8,11):
    eff=1-(g*(pow(rp1,1/g)-1)/(pow(r1,g-1)*(rp1-1)))
    plt.plot(rp1,eff)
plt.xlabel("Pressure Ratio")
plt.ylabel("Efficiency")
plt.show()
