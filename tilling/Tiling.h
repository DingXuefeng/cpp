#ifndef Tiling_H
#define Tiling_H
#include <cmath>
class Tiling
{
  public:
    virtual ~Tiling(){};
    //Tiling():m_unitArea((0.5*sqrt(3)/4*1*1)*6){};
    virtual double area() = 0;
    virtual int PMTnum() = 0; 
    virtual double coverage() = 0;
    const double m_unitArea =(0.5*sqrt(3)/4*1*1)*6;
};
#endif
