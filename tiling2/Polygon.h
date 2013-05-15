#ifndef Polygon_H
#define Polygon_H
#include "In.h"
#include <cmath>
using namespace std;
class Polygon : public In
{
  public:
    virtual ~Polygon(){};
    virtual int n() const = 0;
    virtual double area() const
    {
      //length of side = 1;
      return n()*1/4./tan(angle()/2.);
    }
    double angle() const
    {
      return 2*M_PI/n();
    }
};
#endif
