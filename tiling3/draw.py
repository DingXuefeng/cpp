import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import numpy as np
import string

p = np.linspace(17,19,1001)
#p = np.linspace(17.95,18.0,1001)
#p=np.array([18.6696696697])
#p=np.array([18.96395])
p=np.array([17.5+0.1881])
PMT = []
def arc(R,sumh):
  #ok
  return weiduR(R,sumh)*angle(R,sumh)
def weiduR(R,sumh):
  #ok
  return (R**2-sumh**2)**0.5
def angle(R,sumh):
  #ok
  return 2*np.arccos(R/3**0.5/weiduR(R,sumh))
def deltaArc(R,sumh,deltaAngle):
  #ok
  return weiduR(R,sumh)*deltaAngle
def deltahf(rPMT,R,l0):
  r2 = R*np.sin(anglePMT(rPMT,R)/2)*2
  if r2>l0:
    return (r2**2-l0**2)**0.5
  else:
    print "Warning! sumh:%i"%sumhh[-1]
    return rPMT
def leasth(rPMT,R,sumh):
  return R*np.cos(np.arccos(sumh/R)-anglePMT(rPMT,R))
def deltah(rPMT,R,oldsumh,deltaAngle):
  #
  l0=weiduR(R,oldsumh)*np.sin(deltaAngle/2)
  l1=deltahf(rPMT,R,l0)
  l2=(oldsumh**2+(weiduR(R,oldsumh)*np.cos(deltaAngle/2))**2)**0.5
  l3=R
  #print l1,l2,l3
  #print ((l2**2+l3**2-l1**2)/(2*l2*l3))
  theta1=np.arccos((l2**2+l3**2-l1**2)/(2*l2*l3))
  theta2=np.arccos(oldsumh/l2)
  newtheta=theta2-theta1
  newh=R*np.cos(newtheta)
  if len(sumhh)==1:
    return newh-oldsumh
  else:
    if newh>leasth(rPMT,R,sumhh[-2]):
      return newh-oldsumh
    else:
      print "Warning"
      return leasth(rPMT,R,sumhh[-2])
def PMTn(R,sumh,deltaAngle,odd):
  if(odd):
    return int(angle(R,sumh)/deltaAngle/2)*2
  else:
    return int((angle(R,sumh)-deltaAngle)/deltaAngle/2)*2+1
def angleToWeidaoAngle(R,sumh,angle):
  return np.arcsin(R*np.sin(angle/2)/weiduR(R,sumh))*2
def weidaoAngleToAngle(R,sumh,weidaoangle):
  return np.arcsin(weiduR(R,sumh)*np.sin(angle/2)/R)*2
def maxPMT(rPMT,R,sumh):
  #ok
  return int(angle(R,sumh)/angleToWeidaoAngle(R,sumh,anglePMT(rPMT,R)));
def maxPMTo(rPMT,R,sumh,odd):
  #ok
  if(odd):
    return maxPMT(rPMT,R,sumh)/2*2
  else:
    return (maxPMT(rPMT,R,sumh)-1)/2*2+1
def fdeltaAngle(rPMT,R,sumh,odd,reserveNum):
  #ok
  #print maxPMTo(rPMT,R,sumh,odd),reserveNum
  return angle(R,sumh)/(maxPMTo(rPMT,R,sumh,odd)-reserveNum)
  #return angle(R,sumh)/(maxPMTo(rPMT,R,sumh,odd)-1)
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
def noTouchTop(rPMT,R,sumh,h):
  return PMTtop(rPMT,R,sumh)<=h
def PMTtop(rPMT,R,sumh):
  return R*np.cos(np.arccos(sumh/R)-anglePMT(rPMT,R)/2.)

def coveragef(rPMTOptSurf,R,nPMT):
  return nPMT*rPMTOptSurf**2/(4*R**2)*100

reserveNum=[5,0,1,2,0,0,0,0,0,0,0,0,0]
result=[[]]
maxR=0;
rPMTOptSurf = 0.254
initOdd = True
sumhh=[]
for R in p:
  #rPMT = 0.264*R/(R**2-0.264**2)**0.5
  rPMT = 0.264
  put=[]
  tmpresult=[]
  h = R/3**0.5
  sumh = 0
  odd = initOdd
  reserveNumi=0
  deltaAngle = fdeltaAngle(rPMT,R,0,odd,reserveNum[reserveNumi])
  #print "new Line! %i"%reserveNum[reserveNumi]
  while(noTouchTop(rPMT,R,sumh,h)):
    sumhh.append(sumh)
    info=[sumh,deltaAngle,odd]
    putPMT = PMTn(R,sumh,deltaAngle,odd)
    tmpresult.append(info+[putPMT])
    put.append(putPMT)
    if(shouldwegetnewline(rPMT,R,sumh,deltaAngle)):
      reserveNumi+=1
      sumh += newlinedeltah(rPMT,R,sumh)
      odd = not odd
      odd = initOdd
      deltaAngle = fdeltaAngle(rPMT,R,sumh,odd,reserveNum[reserveNumi])
      #if(noTouchTop(rPMT,R,sumh,h)):
	  #print "new Line! %i"%reserveNum[reserveNumi]
	  #print PMTn(R,sumh,deltaAngle,odd)
	  #print PMTn(R,sumh,fdeltaAngle(rPMT,R,sumh,odd,0),odd)
    else:
      sumh += deltah(rPMT,R,sumh,deltaAngle)
      odd = not odd
  print put
  PMT.append((np.array(put).sum()*2-put[0])*6)
  if coveragef(rPMTOptSurf,R,PMT[-1])>maxR:
    maxR = coveragef(rPMTOptSurf,R,PMT[-1])
    result = [tmpresult,R,PMT[-1]]


def run():
#  for i1 in range(40):
#    for i2 in range(20):
#      for i3 in range(10):
#	for i4 in range(5):
#	  for i5 in range(2):
#	    reserveNum=[i1,i2,i3,i4,i5,0,0,0,0,0,0,0,0,0,0]
#	    for R in p:
#	      optimiase(initOdd,R,reserveNum,maxR,result)
  print maxR
  print result[1],result[2]

  #for side in result[0]:
  #  print side

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
  #plt.show()

if __name__ == "__main__":  
  run()
