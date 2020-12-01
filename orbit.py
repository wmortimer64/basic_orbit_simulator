import matplotlib.pyplot as plt
import math

#x and y positions in the orbit (cartesian, meters)
x = 6300000+2000000#float(input("how high "))
y = 0

#x and y speeds (m/s) in the orbit
yspd = 7500#float(input("spd "))
xspd = 0

#starting time (s)
t = 0

''' arrays to store values to graph at end
parr is pressure
yarr is y position
xarr is x position
accarr is magnitude of acceleration
spdarr is magnitude of speed
harr is magnitude of position
qarr is something about the heat'''
parr = []
yarr = []
xarr = []
accarr = []
spdarr = []
harr = []
qarr = []
tarr = []

''' values to descibe paper plane
m is mass in kg
CD_A is the coefficent of drag times the area'''

m=0.0045#float(input("mass "))
CD_A = 0.017#float(input("CD A "))
h = x
spd = 0

'''dt is the timestep, the smaller the more accurate the simulation, but it takes longer'''
dt = 0.1#float(input("time step "))

'''pressure returns the pressure given a altitude, in km above the CENTER of the earth'''
def pressure(h):
    return 1.217*math.exp(-(h-6371000)/8500)

'''while the plane is above the ground, not crazy far away, and less than two hours have passed do the simulation'''
while 10000000>h>6371000 and t<72000:
    
    '''position change with speed'''
    xnew=x+xspd*dt
    ynew=y+yspd*dt

    '''time increases'''
    t+=dt
    
    '''height is the magnitude of x and y'''
    h = math.hypot(x,y)
    
    '''speed is the magnitude of x speed and y speed'''
    spd = math.hypot(xspd,yspd)
    
    '''speed change with gravity and air resitance'''
    xspdnew=xspd+(-9.8*x/h-(xspd * spd * CD_A * pressure(h))/(2 * m)) * dt
    yspdnew=yspd+(-9.8*y/h-(yspd * spd * CD_A * pressure(h))/(2 * m)) * dt
    
    '''q is something about the heating rate, have to fix this'''
    q = spd**3 * pressure(h)
    
    '''add values to arrays to look at later'''
    parr+=[pressure(h)]
    yarr+=[y]
    xarr+=[x]
    spdarr+=[math.hypot(xspd,yspd)]
    tarr+=[t]
    harr+=[h-6300000]
    qarr += [q**1]
    
    '''values become the new values'''
    x = xnew
    y = ynew
    xspd = xspdnew
    yspd = yspdnew

''' make plot square'''
fig, ax = plt.subplots(figsize=(12, 12))

'''set scale of plot'''
plt.xlim([-10000000,10000000])
plt.ylim([-10000000,10000000])


'''include earth'''
planet = plt.Circle((0,0),6371000)
ax.add_artist(planet)

'''show path of paper plane'''
ax.plot(xarr[:-1],yarr[:-1])
plt.show()

'''other graphs might be helpful'''
plt.plot(tarr[:-1],harr[:-1])
plt.show()
plt.plot(tarr[:-4],spdarr[:-4])
plt.show()
plt.plot(tarr[:-4],qarr[:-4])
plt.show()

'''do the fist one again but show temperature with color
takes forever to draw'''
fig, ax = plt.subplots(figsize=(12, 12))
planet = plt.Circle((0,0),6371000)
plt.xlim([-10000000,10000000])
plt.ylim([-10000000,10000000])
ax.add_artist(planet)
plt.scatter(xarr,yarr,c=qarr, cmap='magma',s=1)
plt.show()
