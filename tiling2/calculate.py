import numpy as np
hexagonN = 8
squareN = 6
def R(lSide):
  a = lSide*3
  R = 2**-0.5*a
  return R
def lSide(R):
  a = 2**0.5*R
  lSide = a/3
  return lSide
print "Module coverage"
print "containing 19 PMT:"
rPMT = 1
nPMT = 19
rPMTOptSurf = 0.25/0.254
rModule = rPMT*(2*3**0.5+1)
RModule = rModule*2*3**-0.5
print RModule
areaModule = 6*3**0.5/4*RModule**2
areaPMTOptSurf = np.pi*rPMTOptSurf**2
coverage = nPMT*areaPMTOptSurf/areaModule
print coverage
print "Module coverage"
print "containing 1 PMT:"
nPMT = 1
rModule = rPMT
RModule = rModule*2*3**-0.5
areaModule = 6*3**0.5/4*RModule**2
coverage = nPMT*areaPMTOptSurf/areaModule
print coverage
