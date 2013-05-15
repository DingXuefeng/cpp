#ifndef Shape_H
#define Shape_H
#include <cmath>
class Shape
{
  public:
    Shape(double length):m_length(length){};
    virtual int check();
    virtual bool outside() = 0;
    virtual bool scan(double x,double y,double phi) = 0;
    virtual int n() = 0;
    virtual double unitDelta()
    {
      return 2*M_PI/n();
    }
    virtual double R()
    {
      return 0.5/sin(unitDelta()/2)*m_length;
    }
    virtual double r()
    {
      return 0.5/tan(unitDelta()/2)*m_length;
    }
    double length(){return m_length;}
  private:
    double m_length;
};
#endif
