#ifndef FillC60_H
#define FillC60_H
#include "Fill.h"
#include "Fillpentagon.h"
#include "Fillhexagon.h"
class FillC60 : public Fill
{
  public:
    void tiling()
    {
      addMethod(new Fillpentagon(),12,25); //C60 has 12 pentagon
      addMethod(new Fillhexagon(),20,25); //C60 has 20 hexagon
    }
};
#endif
