#ifndef node_H
#define node_H
#include <cmath>
#include <iostream>
using namespace std;
class node
{
  public:
    node():m_x(0),m_y(0){};
    node(double x,double y):m_x(x),m_y(y){};
    void x(double x){m_x = x;}
    void y(double y){m_y = y;}
    double x() const {return m_x;}
    double y() const {return m_y;}
    double distance() const {return sqrt(pow(m_x,2)+pow(m_y,2));}
    void print() const 
    {
      //cout<<"x: "<<m_x<<" y: "<<m_y<<" distance: "<<distance()<<endl;
      cout<<m_x<<" "<<m_y<<endl;
    }
    bool operator==(const node &r) const
    {
      return (abs(m_x-r.x())<1e-3)&&(abs(m_y-r.y())<1e-3);
    }  
    node operator*(const double n) const
    {
      return node(m_x*n,m_y*n);
    }  
    node operator+(const node &r) const
    {
      return node(m_x+r.x(),m_y+r.y());
    }  
    node operator-(const node &r) const
    {
      return node(m_x-r.x(),m_y-r.y());
    }  

  private:
    double m_x,m_y;
};
#endif
