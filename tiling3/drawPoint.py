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
  
thetaList = np.array(thetaList)
phiList = np.array(phiList)

xx = R * np.sin(thetaList)* np.cos(phiList)
yy = R * np.sin(thetaList)* np.sin(phiList)
zz = R * np.cos(thetaList)
x1=xx.tolist()
y1=yy.tolist()
z1=zz.tolist()
x1+=(xx*(-1)).tolist()
y1+=(yy).tolist()
z1+=(zz).tolist()
y2 = (np.array(z1)*(-1)).tolist()
x2 = y1
z2 = x1
x3 = (np.array(z1)*(-1)).tolist()
z3 = y1
y3 = x1

x=x1+x2+x3
y=y1+y2+y3
z=z1+z2+z3
#x=xx
#y=yy
#z=zz

for i in range(len(x)):
  if x[i]>0:
    ball=vs.sphere(pos=(x[i],y[i],z[i]),radius=0.2541)
for i in range(len(x)):
  print x[i],y[i],z[i]
