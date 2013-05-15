#!/bin/python
# -*- coding: utf-8 -*-  
import matplotlib.pyplot as plt
import numpy as np
import string

file = open('out','r')
pentagonNl = []
lll = []
while 1:
  line = file.readline()
  if not line:
    break
  data = string.split(line)
  lll.append(string.atof(data[0]))
  pentagonNl.append(string.atof(data[1]))
file.close();
hexagonCover = []
ballCover = []
C60Cover = []
r = []
PMT = []
#for ix in range(len(lll)):
for ix in range(7):
  pentagonN = pentagonNl[ix]
  ll = lll[ix]
  length = ll*0.254*2/3**0.5
  print "length(m) "
  print length
  print "out ball r(m)"
  print length*2.478
  r.append(length*2.478)
  l = int(ll-1)/3*3+1
  hexagonN = l**2-(l-1)/3/2.*6
  print "How many hexagon"
  print (hexagonN)
  print "How many PMT"
  print (pentagonN*12+hexagonN*20)
  PMT.append((pentagonN*12+hexagonN*20))
  print "coverage"
  print 3.1415*(pentagonN*12+hexagonN*20)*0.25**2/(4*(length*2.478)**2)
  print 3.1415*(pentagonN*12+hexagonN*20)*0.25**2/(72.6*(length)**2)
  hexagonCover.append((pentagonN*12+hexagonN*20)\
      *6*0.25*3**0.5*(0.254*2/3**0.5)**2\
      /(72.6*(length)**2))
  C60Cover.append((pentagonN*12+hexagonN*20)\
      *3.14159*0.25**2\
      /(72.6*(length)**2))
  ballCover.append((pentagonN*12+hexagonN*20)\
      *0.25**2\
      /(4*(length*2.478)**2))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(r,np.array(hexagonCover)*100,".",label="module coverage on truncated icosahedron")
ax.plot(r,np.array(C60Cover)*100,".",label="Optical surface coverage on trun. icosa.")
ax.plot(r,np.array(ballCover)*100,".",label="Opt. surf. cov. on ball(simple projection)")
ax.legend(loc='upper left', bbox_to_anchor = (1./7, 3.5/5))
ax.set_xlabel(r'radius of detector(m)')
ax.set_ylabel(r'coverage(%)')
#ax.legend()
#ax.plot(r,PMT,".")
'''
limit  = 25
ax.viewLim.update_from_data(np.array([0,20]),np.array([0,1.5]))
'''
print PMT
plt.grid(True)
plt.show()



