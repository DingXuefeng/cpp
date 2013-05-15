#ifndef Putting_H
#define Putting_H
#include "Tiling.h"
#include "Polygon.h"
#include "Hexagon.h"
using namespace std;
class Putting
{
  public:
    Putting():
      m_tiling(new Tiling),
      m_unit(new Hexagon())
    {};
    ~Putting()
    {
      if(m_board) delete m_board;
      delete m_unit;
      delete m_tiling;
    }
    void setBoard(Polygon* polygon,double lOfSide)
    {
      m_board = polygon;
      m_lOfSide = lOfSide;
      m_tiling->setIn(polygon);
      m_tiling->l(m_lOfSide);
    }
    int put(double initTheta,\
	double initep1,double initep2)
    {
      //how many unit can be putting on it
      m_tiling->initOrigin(initTheta,\
	  initep1,initep2);
      return m_tiling->PMT();
    }
    void print()
    {
      m_tiling->print();
    }
  private:
    Tiling* m_tiling;
    Polygon* m_board;
    Polygon* m_unit;
    double m_lOfSide;
};
#endif
