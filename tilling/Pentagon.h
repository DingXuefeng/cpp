#ifndef Pentagon_H
#define Pentagon_H
#include "Shape.h"
class Pentagon : public Shape
{
  public:
    Pentagon(double length):Shape(length){};
    int check(double dx,double dy,double dphi,Shape* unit);
    bool check(double distance,double phi,Shape* unit);
    int n();
};
#endif
