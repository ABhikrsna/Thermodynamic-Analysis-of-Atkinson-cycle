import matplotlib.pyplot as plt
import numpy as np
g=1.4
cv=0.718
cp=1.005
tmax=1926
tmin=293
plt.subplot(2,1,1)
plt.grid()
r=np.linspace(1,15)
for rp in range(4,8):
    wd=cv*(tmax-(tmin*pow(r,g-1)))-cp*((tmax/(pow(rp,(g-1)/g)*pow(r,g-1)))-tmin)
    plt.plot(r,wd)
plt.xlabel("Compression Ratio")
plt.ylabel("Work Done (in KJ/kg)")

plt.subplot(2,1,2)
plt.grid()
rp1=np.linspace(2,13)
for r1 in range(8,10):
    wd1=cv*(tmax-(tmin*pow(r1,g-1)))-cp*((tmin*pow(rp1,1/g))-tmin)
    plt.plot(rp1,wd1)
plt.xlabel("Pressure Ratio")
plt.ylabel("Work Done (in KJ/kg)")
plt.show()
