#ifndef C60_H
#define C60_H
#include <cmath>
using namespace std;
class C60l
{
  public:
    static double l(double r)
    {
      return r/(1./4*sqrt(58+18*sqrt(5)));
    }
};
#endif
