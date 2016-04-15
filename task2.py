import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
     
def dY_dt(Y,t):
    a = 1.0
    b = 0.2
    return np.array([ a*(Y[0]-Y[0]*Y[1]),b*(-Y[1]+Y[0]*Y[1])])
 

#initial condition for y0 and y1 at x=0                           
Y=np.array([0.10,1.0])                 
t=np.linspace(0, 5, 100)
y= sp.integrate.odeint(dY_dt,Y,t)

fig1=plt.figure()
ax1=fig1.add_subplot(111)
ax1.plot(t, y)
plt.xlabel("time")
plt.ylabel("Prey-Predator(y) ");
plt.plot(t, y[:,0], label='prey', color="blue", linestyle="-")
plt.plot(t, y[:,1], label='predator', color="red", linestyle="-")
plt.title('Prey-Predator vs Time')
plt.savefig("Graph of y1 and y0 against time.png")

fig2=plt.figure()
ax2=fig2.add_subplot(111)
ax2.plot(y[:,0], y[:,1])
plt.xlabel("Prey (y0)")
plt.ylabel("Predator (y1)");
plt.title('Predator vs Prey')
plt.savefig("Graph of y1 against y0.png")

#to test sensitivity, set another initial condition for y0 and y1 at x=0                           
Y2=np.array([0.11,1.0])                 
t=np.linspace(0, 5, 100)
y2= sp.integrate.odeint(dY_dt,Y2,t)

fig3=plt.figure()
ax3=fig3.add_subplot(111)
ax3.plot(t, y2)
plt.xlabel("time")
plt.ylabel("Prey-Predator(y) ");
plt.plot(t, y2[:,0], label='prey', color="blue", linestyle="-")
plt.plot(t, y2[:,1], label='predator', color="red", linestyle="-")
plt.title('Prey-Predator vs Time(2)')
plt.savefig("Graph of y1 and y0 against time 2.png")

fig4=plt.figure()
ax4=fig4.add_subplot(111)
ax4.plot(y2[:,0], y2[:,1])
plt.xlabel("Prey (y0)")
plt.ylabel("Predator (y1)");
plt.title('Predator vs Prey(2)')
plt.savefig("Graph of y1 against y0 2.png")