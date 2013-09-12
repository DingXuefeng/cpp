#include "Angle.h"
#include <cmath>
#ifdef DEBUG
#include <iostream>
using std::cout;
using std::endl;
#endif
void Angle::read(double x1,double y1,double z1,double x2,double y2,double z2,double R)
{
  m_x1=x1;
  m_y1=y1;
  m_z1=z1;
  if(sqrt(pow(x1,2)+pow(y1,2))>=R)
  {
    cout<<"P1 must be inside cylinder"<<endl;
    cout<<sqrt(pow(x1,2)+pow(y1,2)+pow(z1,2))<<">="<<R<<endl;
    throw -1;
  }
  m_x2=x2;
  m_y2=y2;
  m_z2=z2;
  if(sqrt(pow(x2,2)+pow(y2,2))<=R)
  {
    cout<<"P2 must be outside cylinder"<<endl;
    cout<<sqrt(pow(x2,2)+pow(y2,2)+pow(z2,2))<<"<="<<R<<endl;
    throw -2;
  }
  m_R=R;
}
double Angle::theta()
{
  //get \vec k
  double kx,ky,kz;
  kx=m_x2-m_x1;
  ky=m_y2-m_y1;
  kz=m_z2-m_z1;
  //get a,b,c
  double a,b,c;
  a=pow(kx,2)+pow(ky,2);
  b=2*(kx*m_x1+ky*m_y1);
  c=pow(m_x1,2)+pow(m_y1,2)-pow(m_R,2);
  //get \Delta
  double delta;
  delta=pow(b,2)-4*a*c;
#ifdef DEBUG
  if(a==0)
  {
    cout<<"Warning! a=0"<<endl;
    throw a;
  }
  if(delta<0)
  {
    cout<<"Warning! no intersection point"<<endl;
    throw delta;
  }
#endif
  //get lambda
  double lambda1,lambda2;
  lambda1=(-b+sqrt(delta))/(2*a);
  lambda2=(-b-sqrt(delta))/(2*a);
  double lambda;
  lambda=lambda1;
  //get \vec P3
  double x3,y3,z3;
  x3=m_x1+lambda*kx;
  y3=m_y1+lambda*ky;
  z3=m_z1+lambda*kz;
#ifdef DEBUG
  cout<<"P=("<<x3<<","<<y3<<","<<z3<<")"<<endl;
#endif
  //get \vec P3O'
  double vec1x,vec1y,vec1z;
  vec1x=0-x3;
  vec1y=0-y3;
  vec1z=0;
  //get \vec P3P2
  double vec2x,vec2y,vec2z;
  vec2x=m_x1-x3;
  vec2y=m_y1-y3;
  vec2z=m_z1-z3;
  //get theta
  double theta;
  double dot;
  dot=vec1x*vec2x+vec1y*vec2y+vec1z*vec2z;
  double vec1l,vec2l;
  vec1l=sqrt(pow(vec1x,2)+pow(vec1y,2)+pow(vec1z,2));
  vec2l=sqrt(pow(vec2x,2)+pow(vec2y,2)+pow(vec2z,2));
  theta=acos(dot/(vec1l*vec2l));
  return theta/M_PI*180;
}
  

  


