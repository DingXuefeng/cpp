import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string

p = np.linspace(15,25,1001)
#p = np.linspace(17.29,17.3,1001)
#p=np.array([18.6696696697])
p=np.array([17.954])
PMT = []
def weiduR(R,sumh):
  #ok
  #ok,2
  return (R**2-sumh**2)**0.5
def angle(R,sumh):
  #ok
  return 2*np.arccos(R/3**0.5/weiduR(R,sumh))
def deltaArc(R,sumh,deltaAngle):
  #ok
  return weiduR(R,sumh)*deltaAngle
def deltahf(rPMT,l0):
  if l0>2*rPMT:
    print "Failed"
    return 0.0
  r2 = R*np.sin(anglePMT(rPMT,R)/2)*2
  return (r2**2-l0**2)**0.5
def weidutheta(R,sumh):
  #ok,2
  return np.arccos(sumh/R)
def rPMTtoRmodule(rPMT):
  #ok,2
  return rPMT/3**0.5*2
def weiduPMTdeltaR(rPMT,R,sumh):
  #ok,2
  return rPMTtoRmodule(rPMT)/2*np.cos(weidutheta(R,sumh))
def weiduPMTdeltah(rPMT,R,sumh):
  #ok,2
  return rPMTtoRmodule(rPMT)/2*np.sin(weidutheta(R,sumh))
def weiduRup(rPMT,R,sumh):
  #ok,2
  return weiduR(R,sumh)-weiduPMTdeltaR(rPMT,R,sumh)
def weiduphiup(rPMT,R,sumh):
  #ok,2
  return np.arctan(rPMT/weiduRup(rPMT,R,sumh))
def weiduRdown(rPMT,R,sumh):
  #ok,2
  return weiduR(R,sumh)+weiduPMTdeltaR(rPMT,R,sumh)
def weiduphidown(rPMT,R,sumh):
  #ok,2
  return np.arctan(rPMT/weiduRdown(rPMT,R,sumh))
def fdeltatheta(rPMT,R):
  return np.arctan(rPMTtoRmodule(rPMT)/2/R)+np.arctan(rPMTtoRmodule(rPMT)/R)
def deltaho(rPMT,R,oldsumh,deltatheta):
  #ok,2
  newweidutheta=weidutheta(R,oldsumh)-deltatheta
  newh=R*np.cos(newweidutheta)
  return newh-oldsumh
def deltah(rPMT,R,oldsumh):
  return deltaho(rPMT,R,oldsumh,fdeltatheta(rPMT,R))
def PMTno(rPMT,R,sumh,deltaAngle):
  #ok,2
  return int(containangle(rPMT,R,sumh)/deltaAngle+1)
def PMTn(rPMT,R,sumh,deltaAngle,odd):
  #ok,2
  if(odd):
    return int(PMTno(rPMT,R,sumh,deltaAngle)/2)*2
  else:
    return int((PMTno(rPMT,R,sumh,deltaAngle)-1)/2)*2+1
def angleToWeidaoAngle(R,sumh,angle):
  return np.arcsin(R*np.sin(angle/2)/weiduR(R,sumh))*2
def bigR(rPMT,R):
  return (R**2+(rPMTtoRmodule(rPMT)/2)**2)**0.5
def angleup(rPMT,R,sumh):
  #ok,2
  return angle(R,sumh+weiduPMTdeltah(rPMT,R,sumh))
def containangle(rPMT,R,sumh):
  #ok,2
  return angleup(rPMT,R,sumh)-weiduphiup(rPMT,R,sumh)*2
def maxPMT(rPMT,R,sumh):
  #ok
  #ok,2
  return PMTno(rPMT,R,sumh,weiduphiup(rPMT,R,sumh)*2)
def maxPMTo(rPMT,R,sumh,odd):
  #ok
  #ok,2
  if(odd):
    return maxPMT(rPMT,R,sumh)/2*2
  else:
    return (maxPMT(rPMT,R,sumh)-1)/2*2+1
def fdeltaAngle(rPMT,R,sumh,odd,res):
  #ok
  #ok,2
  return containangle(rPMT,R,sumh)/(maxPMTo(rPMT,R,sumh,odd)-res-1)
def shouldwegetnewline(rPMT,R,sumh,deltaAngle):
  #ok,2
  newsumh = sumh+deltah(rPMT,R,sumh)
  if deltaAngle<weiduphidown(rPMT,R,newsumh)*2:
    return True
  else:
    return False
def anglePMT(rPMT,R):
  return np.arctan(rPMT/R)*2
def fdeltathetanewline(rPMT,R):
  return np.arctan(rPMTtoRmodule(rPMT)/R)*2
def newlinedeltah(rPMT,R,sumh):
  return deltaho(rPMT,R,sumh,fdeltathetanewline(rPMT,R))
def noTouchTop(rPMT,R,sumh,h):
  #ok,2
  return weidutheta(R,h)<weiduthetatop(rPMT,R,sumh)
def weiduthetatop(rPMT,R,sumh):
  #ok,2
  return weidutheta(R,sumh)-np.arctan(rPMTtoRmodule(rPMT)/R)

result=[[]]
maxR=0;
initOdd = True
rPMT = (0.254+0.005)*(2*3**0.5+1)+0.005
rPMT = 0.264*(2*3**0.5+1)
rPMTOptSurf = 0.254*19**0.5
def coveragef(rPMTOptSurf,R,nPMT):
  return nPMT*rPMTOptSurf**2/(4*R**2)*100

ress=[0,0,0,0]

for R in p:
  put=[]
  tmpresult=[]
  h = R/3**0.5
  sumh = 0
  odd = initOdd
  resi=0
  deltaAngle = fdeltaAngle(rPMT,R,0,odd,ress[resi]) #ok,2
  #print noTouchTop(rPMT,R,sumh,h)
  while(noTouchTop(rPMT,R,sumh,h)): #ok,2
    info=[sumh,deltaAngle,odd]
    putPMT = PMTn(rPMT,R,sumh,deltaAngle,odd) #ok,2
    print putPMT,
    if(shouldwegetnewline(rPMT,R,sumh,deltaAngle)): #ok,2
      sumh += newlinedeltah(rPMT,R,sumh)
      odd = not odd
      resi+=1
      deltaAngle = fdeltaAngle(rPMT,R,sumh,odd,ress[resi])
    else:
      sumh += deltah(rPMT,R,sumh) #ok,2
      odd = not odd
    tmpresult.append(info+[putPMT])
    put.append(putPMT)
  print
  print put
  PMT.append((np.array(put).sum()*2-put[0])*6)
  if coveragef(rPMTOptSurf,R,PMT[-1])>maxR:
    maxR = coveragef(rPMTOptSurf,R,PMT[-1])
    result = [tmpresult,R,PMT[-1]]


def run():

  print maxR
  print result[1],result[2]

#  for side in result[0]:
#    print side

    #print put
  npPMT = np.array(PMT)
  coverage = coveragef(rPMTOptSurf,p,npPMT)
  fig = plt.figure(figsize=(10,10))
  ax = fig.add_subplot(211)
  ax.plot(p,np.array(PMT)/10000.,".",ms=2)
  ax.set_xlabel("Detactor Radius(m)")
  ax.set_ylabel("PMT number(x10^4)")
  ax.grid(True)
  bx = fig.add_subplot(212)
  bx.plot(p,coverage,".",ms=2,color="red")
  bx.set_xlabel("Detactor Radius(m)")
  bx.set_ylabel("coverage(%)")
  bx.grid(True)
  plt.show()

if __name__ == "__main__":  
  run()
