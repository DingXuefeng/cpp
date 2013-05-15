#ifndef ProcessManager_H
#define ProcessManager_H
#include "Putting.h"
#include "Hexagon.h"
#include "Pentagon.h"
class Polygon;
class ProcessManager
{
  public:
    ProcessManager():m_putting(new Putting()){};
    ~ProcessManager()
    {
      delete m_putting;
    }
    void init()
    {
      if(!m_putting)
	m_putting = new Putting();
      m_putting->setBoard(m_polygon,m_lOfSide);
    }
    int run()
    {
      m_n = m_putting->put(m_initTheta,\
	  m_initep1,m_initep2);
      return m_n;
    }
    void setPolygon(int n,double lOfSide)
    {
      switch(n)
      {
	case 5:
	  m_polygon = new Pentagon();
	  break;
	case 6:
	  m_polygon = new Hexagon();
	  break;
	default:
	  throw n;
      }
      m_lOfSide = lOfSide;
    }
    void set(double initTheta = 0,\
	double initep1 = 0,\
	double initep2 = 0)
    {
      m_initTheta = initTheta;
      m_initep1 = initep1;
      m_initep2 = initep2;
    }
    void print()
    {
      m_putting->print();
    }
  private:
    double m_initep1,m_initep2;
    Putting* m_putting;
    int m_n;
    double m_lOfSide;
    double m_initTheta;
    Polygon* m_polygon;
};
#endif
