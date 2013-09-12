import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string
import hexagon as dr
from mpl_toolkits.mplot3d import Axes3D
import visual as vs
print "coverage: %lf%%"% dr.maxR
R = dr.result[1]

thetaphiList = []
thetaList = []
phiList = []
for side in dr.result[0]:
  sumh = side[0]
  deltaAngle = side[1]
  odd = side[2]
  putPMT = side[3]
  theta = np.arccos(sumh/R)
  for i in range(putPMT):
    phi = -(putPMT-1)/2.*deltaAngle+i*deltaAngle
    thetaphiList.append([theta,phi])
    thetaList.append(theta)
    phiList.append(phi)
    if sumh!=0:
      thetaphiList.append([-theta,phi])
      thetaList.append(np.pi-theta)
      phiList.append(phi)
  
#weiduX=[]
#weiduY=[]
#weiduZ=[]
#
#for theta,phi in thetaphiList:
#  weiduX.append(R*np.cos
#  print [theta,phi]
#for theta,phi in (np.array(thetaphiList)/np.pi*180).round():
#  print [theta,phi]
#R=R+0.254+0.2
thetaList=np.array(thetaList+thetaList)
phiList=np.array(phiList+(np.array(phiList)+np.pi).tolist())

xx = R * np.sin(thetaList)* np.cos(phiList)
yy = R * np.sin(thetaList)* np.sin(phiList)
zz = R * np.cos(thetaList)
x1=xx.tolist()
y1=yy.tolist()
z1=zz.tolist()
y2 = (np.array(z1)*(-1)).tolist()
x2 = y1
z2 = x1
x3 = (np.array(z1)*(-1)).tolist()
z3 = y1
y3 = x1
ox=x1+x2+x3
oy=y1+y2+y3
oz=z1+z2+z3
for i in range(len(ox)):
  print ox[i],oy[i],oz[i]
x=xx
y=yy
z=zz
#roundnum=14
#def roundarray(l,roundnum):
#  return (np.array(l)*10**roundnum).round()/10**roundnum
#x=roundarray(x,roundnum)
#y=roundarray(y,roundnum)
#z=roundarray(z,roundnum)
#x=xx
#y=yy
#z=zz

r1data=[(0,(0,0,1)),(np.pi/2,(0,0,1)),(np.pi/2,(0,0,1))]
r2data=[(0,(0,0,1)),(np.pi/2,(1,0,0)),(np.pi/2,(0,1,0))]
lframe = vs.frame()
for obj in vs.scene.lights:
    if isinstance(obj, vs.distant_light):
        obj.frame = lframe # put distant lights in a frame
old = vs.vector(vs.scene.forward) # keep a copy of the old forward

for k in range(len(r1data)):
  for i in range(len(x)):
    hexagon = vs.convex(color=(0.7,0.7,0.7))
    L = []
    r=0.264*(2*3**0.5+1)
    rr=r/3**0.5*2
    h=0.254+0.2
    rru=rr/R*(R-h)
    theta=thetaList[i]
    phi=phiList[i]
    ex=vs.vector(1,0,0)
    ey=vs.vector(0,1,0)
    ez=vs.vector(0,0,1)
    ex=ex.rotate(angle=vs.deg2rad(90)+phi,axis=ez)
    ey=ey.rotate(angle=vs.deg2rad(90)+phi,axis=ez)
    ey=ey.rotate(angle=vs.deg2rad(180)+theta,axis=ex)
    ez=ez.rotate(angle=vs.deg2rad(180)+theta,axis=ex)
    ex=ex.rotate(angle=vs.deg2rad(-90),axis=ez)
    ey=ey.rotate(angle=vs.deg2rad(-90),axis=ez)
    center=vs.vector(x[i],y[i],z[i])
    for j in np.arange(0,2*np.pi,np.pi/3):
      up=ex*np.cos(j)*rr+ey*np.sin(j)*rr+ez*(0)+center
      up=up.rotate(angle=r1data[k][0],axis=r1data[k][1])
      up=up.rotate(angle=r2data[k][0],axis=r2data[k][1])
      L.append((up.x,up.y,up.z))
      down=ex*np.cos(j)*rru+ey*np.sin(j)*rru+ez*(h)+center
      down=down.rotate(angle=r1data[k][0],axis=r1data[k][1])
      down=down.rotate(angle=r2data[k][0],axis=r2data[k][1])
      L.append((down.x,down.y,down.z))
#    if up.x>0:
#      continue
    hexagon.pos = L
#ball=vs.sphere(pos=(0,0,0),radius=17.5)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
##ax.plot(xx,yy,zz,".")
#ax.scatter(x,y,z,color="g",s=100)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#plt.show()
#for i in range(len(x)):
#  print x[i],y[i],z[i]
while 1:
    vs.rate(50)
    if vs.scene.forward != old:
        new = vs.scene.forward
        axis = vs.cross(old,new)
        angle = new.diff_angle(old)
        lframe.rotate(axis=axis, angle=angle)
        old = vs.vector(new)
