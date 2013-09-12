import visual as vs
import numpy as np
r=17.5
#vs.scene.forward=(-1,0,0)
ax=vs.arrow(pos=(0,0,0),axis=(12,0,0),color=vs.color.magenta,shaftwidth=1)
ay=vs.arrow(pos=(0,0,0),axis=(0,12,0),color=vs.color.yellow,shaftwidth=1)
az=vs.arrow(pos=(0,0,0),axis=(0,0,12),color=vs.color.green,shaftwidth=1)
bx=vs.arrow(radius=1,pos=(0,0,0),axis=(1,0,0),color=vs.color.magenta)
by=vs.arrow(radius=1,pos=(0,0,0),axis=(0,1,0),color=vs.color.yellow)
bz=vs.arrow(radius=1,pos=(0,0,0),axis=(0,0,1),color=vs.color.green)
while True:
  for theta in np.linspace(0,np.pi,13):
    for phi in np.arange(0,2*np.pi,1/(np.abs(r*np.cos(theta))+np.pi/3*1e-5)):
      x=r*np.sin(theta)*np.cos(phi)
      y=r*np.sin(theta)*np.sin(phi)
      z=r*np.cos(theta)
      bx.visible=False
      bx=vs.arrow(pos=(x,y,z),axis=(r/3,0,0),color=vs.color.magenta)
      by.visible=False
      by=vs.arrow(pos=(x,y,z),axis=(0,r/3,0),color=vs.color.yellow)
      bz.visible=False
      bz=vs.arrow(pos=(x,y,z),axis=(0,0,r),color=vs.color.green)
      bx.rotate(angle=vs.deg2rad(90)+phi,axis=az.axis)
      by.rotate(angle=vs.deg2rad(90)+phi,axis=az.axis)
      bz.rotate(angle=vs.deg2rad(90)+phi,axis=az.axis)
      bx.rotate(angle=vs.deg2rad(180)+theta,axis=ax.axis)
      by.rotate(angle=vs.deg2rad(180)+theta,axis=ax.axis)
      bz.rotate(angle=vs.deg2rad(180)+theta,axis=ax.axis)
      bx.rotate(angle=vs.deg2rad(-90),axis=az.axis)
      by.rotate(angle=vs.deg2rad(-90),axis=az.axis)
      bz.rotate(angle=vs.deg2rad(-90),axis=az.axis)

      #unit.rotate(angle=vs.deg2rad(90),axis=(1,0,0))
      vs.rate(100)
      
