import numpy as np
import visual as vs
import subprocess  
p = subprocess.Popen("./main",stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)  
#INPUT####################################
theta=np.arctan(1637.6/100);
inputnum=[678.3,-1637.6,1350.,2300*np.cos(theta),2300*np.sin(theta),-1750,2000]
#INPUT END################################
for num in inputnum:
  print num
  p.stdin.write(str(num)+" ")  
for a in p.stdout.readlines():
  print a,
  exec(a)
Op=(0,0,P[2])
ACUPMT=np.array(PMT)-np.array(ACU)
OpP=np.array(P)-np.array(Op)
vs.sphere(pos=ACU,color=vs.color.red,radius=100) #ACU-C
vs.sphere(pos=PMT,color=vs.color.blue,radius=100) #PMT
vs.sphere(pos=P,color=vs.color.green,radius=100) #Point
vs.cylinder(pos=ACU,length=4000,axis=ACUPMT,color=vs.color.yellow,radius=50)
vs.cylinder(pos=Op,length=4000,axis=OpP,color=vs.color.yellow,radius=50)
for z in np.linspace(-2000,2000,40):
  vs.ring(pos=(0,0,z),axis=(0,0,1),radius=2000,thickness=10)

