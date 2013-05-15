#ifndef Hexagon_H
#define Hexagon_H
#include "Polygon.h"
class Hexagon : public Polygon
{
  private:
    int n() const {return 6;}
};
#endif
