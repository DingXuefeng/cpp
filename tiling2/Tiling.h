#ifndef Tiling_H
#define Tiling_H
#include "Bn.h"
#include <vector>
#include <cmath>
#include "node.h"
using namespace std;
class Tiling : public Bn
{
  public:
    Tiling():m_origin(),\
	     m_initTheta(90),m_l(28.001){};
    virtual ~Tiling(){clear();};
  public:
    void l(double l) {m_l = l;}
    virtual void initOrigin(double initTheta,\
	double initep1,double initep2)
    {
      m_initTheta = initTheta;
      m_origin = (m_ep1*initep1)+(m_e2*initep2);
    }
    int PMT();
    void print();
  public:
    bool inside(node* point) const;
    virtual double unitLength() const
    {
      return 0.254/sqrt(3)*2;
    }
  private:
    static const node m_e1;
    static const node m_e2;
    static const node m_ep1;
    static const node m_ep2;
    node m_origin;
    void clear()
    {
      for(vector<node*>::size_type ix = 0;ix!=m_putted.size();ix++)
	delete m_putted[ix];
      m_putted.clear();
    }
    bool m_inside(node* point) const;
    double m_initTheta;
    double m_l;
  protected:
    vector<node*> m_putted;
  public:
    double r() const
    {
      return m_l/2/tan(unitDelta()/2.);
    }
    double initTheta() const{return m_initTheta;}
    double unitDelta() const
    {
      return 2*M_PI/n();
    }
#ifdef DEBUG
#define DEBUG
    void push(node* p)
    {
      m_putted.push_back(p);
    }
#endif
};
#endif
