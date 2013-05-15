#ifndef Pentagon_H
#define Pentagon_H
#include "Polygon.h"
class Pentagon : public Polygon
{
  private:
    int n() const {return 5;}
};
#endif
