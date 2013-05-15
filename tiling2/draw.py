import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string

file = open('data.txt','r')
l = string.atof(string.split(file.readline())[1])
n = string.atoi(string.split(file.readline())[1])
initTheta = string.atof(string.split(file.readline())[1])
print l
print n
print initTheta
x = []
y = []
while 1:
  line = file.readline()
  if not line:
    break
  data = string.split(line)
  x.append(string.atof(data[0]))
  y.append(string.atof(data[1]))
file.close();
unitLength = 0.254*3**-0.5*2
verts = np.array([[np.cos(theta),np.sin(theta)] for theta in np.arange(7)*360./6/180*np.pi])*unitLength
codes = [1,2,2,2,2,2,79]
hexagon = mpath.Path(verts, codes)
pathpatch = mpatch.PathPatch(hexagon,facecolor='red',edgecolor='green')
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
for i in range(len(x)):
  tverts = verts+[x[i],y[i]]
  thexagon = mpath.Path(tverts, codes)
  tpathpatch = mpatch.PathPatch(thexagon,facecolor='None',edgecolor='green')
  ax.add_patch(tpathpatch)
overts = np.array([[np.cos(theta),np.sin(theta)] for theta in (np.arange(n+1)*360./n+initTheta)/180*np.pi])*l/2/np.cos((90-360./n/2)/180*np.pi)
ocodes = [1]+[2]*(n-1)+[79]
pentagon = mpath.Path(overts, ocodes)
opathpatch = mpatch.PathPatch(pentagon,facecolor='None',edgecolor='blue')
ax.add_patch(opathpatch)
ax.set_title('PMT module placement on hexagon')
ax.set_xlabel(r'x(m)')
ax.set_ylabel(r'y(m)')
limit  = 9 
ax.viewLim.update_from_data(np.array([-limit,limit]),np.array([-limit,limit]))
ax.set
plt.show()

