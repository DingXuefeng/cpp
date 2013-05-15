import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string
import draw as dr
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
thetaList = np.array(thetaList)
phiList = np.array(phiList)
#for theta,phi in (np.array(thetaphiList)/np.pi*180).round():
#  print [theta,phi]

xx = R * np.sin(thetaList)* np.sin(phiList)
yy = R * np.sin(thetaList)* np.cos(phiList)
zz = R * np.cos(thetaList)
x1=xx.tolist()
y1=yy.tolist()
z1=zz.tolist()
x1+=(xx).tolist()
y1+=(yy*(-1)).tolist()
z1+=(zz).tolist()
y2 = (np.array(z1)*(-1)).tolist()
x2 = y1
z2 = x1
x3 = (np.array(z1)*(-1)).tolist()
z3 = y1
y3 = x1

#x+=yy.tolist()
#y+=xx.tolist()
#z+=zz.tolist()
#
#x+=xx.tolist()
#y+=zz.tolist()
#z+=yy.tolist()

#
#
#x+=(xx*(-1)).tolist()
#y+=(yy).tolist()
#z+=(zz).tolist()
x=x1+x2+x3
y=y1+y2+y3
z=z1+z2+z3
#x=xx
#y=yy
#z=zz
for i in range(len(x)):
  ball = vs.sphere(pos=(x[i],y[i],z[i]), radius=0.254)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
##ax.plot(xx,yy,zz,".")
#ax.scatter(x,y,z,color="g",s=100)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#plt.show()
for i in range(len(x)):
  print x[i],y[i],z[i]
