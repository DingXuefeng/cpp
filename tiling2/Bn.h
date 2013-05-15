#ifndef Bn_H
#define Bn_H
#include "In.h"
#include "Polygon.h"
#include <string>
using namespace std;
class Bn
{
  public:
    void setIn(Polygon* polygon)
    {
      m_Inp = polygon;
    }
    double n() const
    {
      return m_Inp->n();
    }
  private:
    In* m_Inp;
};
#endif
