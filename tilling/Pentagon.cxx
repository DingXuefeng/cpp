#include <cmath>
#include "Pentagon.h"
Pentagon::Pentagon(double length):Shape(length){};
int Pentagon::check(double dx,double dy,double dphi,Shape* unit)
{
  const int MAX = 100;
  int total(0);
  for(int x = -MAX;x<MAX;x++)
    for(int y = -MAX;y<MAX;y++)
    {
      total += check(x+dx,y+dy,dphi,Shape* unit);
    }
  return total;
}
bool Pentagon::check(double x,double y,double phi,Shape* unit)
{
  return unit->scan(x,y,phi);
}
int Pentagon::n()
{
  return 5;
}
};
