import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
r,rp,tmax,tmin=sp.symbols('r rp tmax tmin',real=True)
g=1.4
cv=0.718
cp=1.005
tmax1=1926
tmin1=293
wd=cv*(tmax-(tmin*pow(r,g-1)))-cp*((tmax/(pow(rp,(g-1)/g)*pow(r,g-1)))-tmin)
k=sp.diff(wd,r)
ans=sp.solve(k,(r,rp,tmax,tmin))
print("the maximum work done is at:",ans)
rp1=np.linspace(2,10)
r1=1.4*pow((tmax1/tmin1),5/4)*pow(1/rp1,5/14)
wd1=cv*(tmax1-(tmin1*pow(r1,g-1)))-cp*((tmax1/(pow(rp1,(g-1)/g)*pow(r1,g-1)))-tmin1)
eff1=1-(g*(pow(rp1,1/g)-1)/(pow(r1,g-1)*(rp1-1)))

plt.subplot(1,3,1)
plt.grid()
plt.plot(rp1,r1)
plt.xlabel("Pressure ratio")
plt.ylabel("Compression ratio")

plt.subplot(1,3,2)
plt.grid()
plt.plot(r1,wd1)
plt.xlabel("Compression ratio")
plt.ylabel("Work Done")

plt.subplot(1,3,3)
plt.grid()
plt.plot(r1,eff1)
plt.xlabel("Compression ratio")
plt.ylabel("Efficiency")

plt.show()