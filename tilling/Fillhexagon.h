#ifndef Fillhexagon_H
#define Fillhexagon_H
#include "Tiling.h"
#include <cmath>
class Fillhexagon : public Tiling
{
  public:
    double area()
    {
      return (0.5*sqrt(3)/4*1*1)*6;
    }
    int PMTnum()
    {
      if(25==25)
      {
      }
      return 25*25-8/2*6;
    }
    double coverage()
    {
      return PMTnum()/25./25.;
    }
};
#endif
