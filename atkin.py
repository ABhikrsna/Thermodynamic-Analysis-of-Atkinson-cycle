import matplotlib.pyplot as plt
import numpy as np
import pyromat as pyro

v1=float(input("Volume of Cylinder (in cm^3):-"))
v2=float(input("Clearence Volume(in cm^3):-"))
tmax=float(input("Maximum Temperature limit (in K):-"))
tmin=float(input("Minimum Temperature limit (in K):-"))
pin=float(input("Input Pressure (in KPa):-"))

air=pyro.get('ig.air')
r=v1/v2
#Using air as working fluid
g=1.4  
cv=0.718  
cp=1.005
R=cp-cv

p2=pin*pow(r,g)
t2=tmin*pow(r,g-1)
rp=tmax/t2
t4=tmin*pow(rp,1/g)
pmax=p2*rp
v3=v2
v4=v3*pow(tmax/t4,1/(g-1))
p4=pmax*pow(v3/v4,g)

qin=cv*(tmax-t2)
qout=cp*(t4-tmin)
eff=100*(qin-qout)/qin
effc=(1-(tmin/tmax))*100
print("\nAll Pressures in KPa:- ",pin,p2,pmax,p4)
print("\nAll Temperature in K:- ",tmin,t2,tmax,t4)
print("\nPressure ratio and compression ratio:-",rp,r)
print(f"\nEfficiency of atkinson cycle:-{eff}%")
print(f"\nCarnot efficiency:-{effc}%")
plt.subplot(2,1,1)
plt.grid()
c=pin*pow(v1,g)
x=np.linspace(v1,v2)
y=c/pow(x,g)
plt.plot(x,y)

x1=np.linspace(v2,v3)
y1=np.linspace(p2,pmax)
plt.plot(x1,y1)

c1=pmax*pow(v3,g)
x2=np.linspace(v4,v3)
y2=c1/pow(x,g)
plt.plot(x2,y2)

x3=[v4,v1]
y3=[c1/pow(v4,g)+75,pin]
plt.plot(x3,y3)

plt.xlabel("Volume (in cm^3)")
plt.ylabel("Pressure (in KPa)")
plt.legend(["Reversible Adiabatic Compression",
            "Constant Volume Heat Addition",
            "Reversible Adiabatic Expansion",
            "Constant Pressure Heat Rejection"],
           loc="upper right")

plt.subplot(2,1,2)
plt.grid()
s1=air.s(tmin,pin)
s2=s1
s3=air.s(tmax,pmax)
s4=s3
t2_2=air.T_s(s=s1,p=p2)
t4_2=air.T_s(s=s4,p=p4)

plt.plot([s1,s2],[tmin,t2_2])

T=np.linspace(t2_2,tmax)
p=np.linspace(p2,pmax)
s=air.s(T,p)
plt.plot(s,T)

plt.plot([s3,s4],[tmax,t4_2])

T=np.linspace(tmin,t4_2)
s=air.s(T=T,p=pin)
plt.plot(s,T)

plt.xlabel("Entropy (in KJ/kg/K")
plt.ylabel("Temperature (in K)")
plt.legend(["Reversible Adiabatic Compression",
            "Constant Volume Heat Addition",
            "Reversible Adiabatic Expansion",
            "Constant Pressure Heat Rejection"],
           loc="upper right")

plt.show()