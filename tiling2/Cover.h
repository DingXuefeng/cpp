#ifndef Cover_H
#define Cover_H
#include <cmath>
#include "Bn.h"
using namespace std;
class Cover : public Bn
{
  public:
    virtual double totalArea(double l) const
    {
      return n()*1./4*pow(l,2)/tan(M_PI/n());
    }
    virtual double PMTOptSurfarea() const
    {
      return M_PI*pow(PMTSurfr(),2);
    }
  private:
    virtual double PMTSurfr() const
    {
      return 0.25;
    }
};
#endif
