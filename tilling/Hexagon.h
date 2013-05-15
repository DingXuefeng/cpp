#ifndef Hexagon_H
#define Hexagon_H
#include "Shape.h"
class Hexagon : public Shape
{
  public:
    Hexagon(double length):Shape(length){};
    bool scan(double x,double y,double phi)
    {
      //true = inside
      double distance = sqrt(pow(x,2)+pow(y,2));
      if(distance>R())
	return false; //outside
      else if(distance<r())
	return true; //inside
      else
      {
	double theta;
	theta = y>0?acos(x):(2*M_PI-acos(x));
	double delta = theta-phi;
	delta = delta-int(delta/unitDelta())*unitDelta();
	return distance<r()/cos(delta);
      }
    }
    bool outside()
    {
      throw("Error");
      return true;
    }
    bool scan()
    {
      throw("Error");
      return true;
    }
    int n()
    {
      return 6;
    }
};
#endif
