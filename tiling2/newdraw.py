import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string

file = open('data.txt','r')
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
verts = [[np.cos(theta),np.sin(theta)] for theta in np.arange(7)*360./6/180*np.pi]
codes = [1,2,2,2,2,2,79]
hexagon = mpath.Path(verts, codes)
pathpatch = mpatch.PathPatch(hexagon,facecolor='red',edgecolor='green')
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
tverts = [];
tcodes = [];
for i in range(len(x)):
  tverts += [[np.cos(theta)+x[i],np.sin(theta)+y[i]] for theta in np.arange(7)*360./6/180*np.pi]
  tcodes += codes
thexagon = mpath.Path(tverts, tcodes)
tpathpatch = mpatch.PathPatch(thexagon,facecolor='red',edgecolor='green')
ax.add_patch(tpathpatch)
ax.set_title('A compound path')
ax.viewLim.update_from_data(np.array([-20,20]),np.array([-20,20]))
plt.show()

