import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string

class Tiling:
  def __init__(self,R):
    self.result=[[]]
    self.maxR=0;
    self.initOdd = True
    self.rPMT = 0.25411
    self.rPMTOptSurf = 0.254

  def noTouchTop(self):
    return PMTtop()<=h
  def arc(self):
    #ok
    return weiduR()*angle()
  def weiduR(self):
    #ok
    return (self.R**2-self.sumh**2)**0.5
  def angle(self):
    #ok
    return 2*np.arccos(self.R/3**0.5/weiduR(self.R,self.sumh))
  def deltaArc(self):
    #ok
    return weiduR()*deltaAngle
  def deltahf():
    if l0>2*rPMT:
      print "Failed"
    return 0.0
  r2 = R*np.sin(anglePMT(rPMT,R)/2)*2
  return (r2**2-l0**2)**0.5
def deltah(rPMT,R,oldsumh,deltaAngle):
  #
  l0=weiduR(R,oldsumh)*np.sin(deltaAngle/2)
  l1=deltahf(rPMT,l0)
  l2=(oldsumh**2+(weiduR(R,oldsumh)*np.cos(deltaAngle/2))**2)**0.5
  l3=R
  theta1=np.arccos((l2**2+l3**2-l1**2)/(2*l2*l3))
  theta2=np.arccos(oldsumh/l2)
  newtheta=theta2-theta1
  newh=R*np.cos(newtheta)
  return newh-oldsumh
def PMTn(R,sumh,deltaAngle,odd):
  if(odd):
    return int(angle(R,sumh)/deltaAngle/2)*2
  else:
    return int((angle(R,sumh)-deltaAngle)/deltaAngle/2)*2+1
def angleToWeidaoAngle(R,sumh,angle):
  return np.arcsin(R*np.sin(angle/2)/weiduR(R,sumh))*2
def maxPMT(rPMT,R,sumh):
  #ok
  return int(angle(R,sumh)/angleToWeidaoAngle(R,sumh,anglePMT(rPMT,R)));
def maxPMTo(rPMT,R,sumh,odd):
  #ok
  if(odd):
    return maxPMT(rPMT,R,sumh)/2*2
  else:
    return (maxPMT(rPMT,R,sumh)-1)/2*2+1
def fdeltaAngle(rPMT,R,sumh,odd):
  #ok
  return angle(R,sumh)/maxPMTo(rPMT,R,sumh,odd)
def shouldwegetnewline(rPMT,R,sumh,deltaAngle):
  newsumh = sumh+deltah(rPMT,R,sumh,deltaAngle)
  if deltaArc(R,newsumh,deltaAngle)<=2*rPMT:
    return True
  else:
    return False
def anglePMT(rPMT,R):
  return np.arctan(rPMT/R)*2
def newlinedeltah(rPMT,R,sumh):
  return R*np.cos(np.arccos(sumh/R)-anglePMT(rPMT,R))-sumh
def PMTtop(rPMT,R,sumh):
  return R*np.cos(np.arccos(sumh/R)-anglePMT(rPMT,R)/2.)

def coveragef(rPMTOptSurf,R,nPMT):
  return nPMT*rPMTOptSurf**2/(4*R**2)*100
p = np.linspace(17,19,1001)
p = np.linspace(18.3,18.4,1001)
p=np.array([18.6696696697])
#p=np.array([18.3443])
PMT = []

for R in p:
  put=[]
  tmpresult=[]
  h = R/3**0.5
  sumh = 0
  odd = initOdd
  deltaAngle = fdeltaAngle(rPMT,R,0,odd)
  while(noTouchTop(rPMT,R,sumh,h)):
    info=[sumh,deltaAngle,odd]
    putPMT = PMTn(R,sumh,deltaAngle,odd)
    if(shouldwegetnewline(rPMT,R,sumh,deltaAngle)):
      sumh += newlinedeltah(rPMT,R,sumh)
      odd = not odd
      odd = initOdd
      deltaAngle = fdeltaAngle(rPMT,R,sumh,odd)
    else:
      sumh += deltah(rPMT,R,sumh,deltaAngle)
      odd = not odd
    tmpresult.append(info+[putPMT])
    put.append(putPMT)
  put.pop()
  PMT.append((np.array(put).sum()*2-put[0])*6)
  if coveragef(rPMTOptSurf,R,PMT[-1])>maxR:
    maxR = coveragef(rPMTOptSurf,R,PMT[-1])
    result = [tmpresult,R]


def run():

  print maxR
  print result[1]

  for side in result[0]:
    print side

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
