#ifndef BsurfArea_H
#define BsurfArea_H
#include "IsurfArea.h"
#include "Polygon.h"
#include <string>
using namespace std;
class BsurfArea
{
  public:
    void setIsurfArea(Polygon* polygon)
    {
      m_IsurfAreap = polygon;
    }
    double surfArea() const
    {
      return m_IsurfAreap->surfArea();
    }
  private:
    IsurfArea* m_IsurfAreap;
};
#endif
