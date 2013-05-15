import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string
p = np.linspace(16/0.254,20/0.254,10000)
startTheta = np.arcsin((3/2.)**0.5)
startThetaPhi = -np.pi/4
startThetaPhie = np.pi/4
endTheta = np.pi/2
theta = [startTheta-PMTtheta]
tmptheta = theta[-1]-PMTtheta*3**0.5
weiduyuanR = R*np.sin(tmptheta)
thisArcAngle = np.arccos(R/3**0.5/weiduyuanR)
thisArc = thisArcAngle*weiduyuanR
tmpnPMT = R*np.sin(tmptheta)*angle(tmptheta)
m = 6*3**0.5/4/(np.pi*(3**0.5/2)**2)
coverage = (1+(np.pi/8*p).round())*((2./3*p).round()+1)*2/p**2*m
print ((2./3*p).round()+1)
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.plot(p*0.254,coverage)
plt.show()

