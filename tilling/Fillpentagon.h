#ifndef Fillpentagon_H
#define Fillpentagon_H
#include "Tiling.h"
#include <cmath>
/*
#include "Pentagon.h"
#include "Hexagon.h"
*/
class Fillpentagon : public Tiling
{
  public:
    double area()
    {
      return (0.5*0.5*tan(54./180*M_PI)*1.)*5;
    }
    int PMTnum()
    {
      /*
      double x,y,phi;
      const double height = sqrt(3);
      const double wedth = 0.5;
      const int num1 = 100;
      const int num2 = 100;
      const int num3 = 100;
      double maxx(0),maxy(0),maxphi(0);
      int maxnum(0);
      Hexagon unit(1);
      for(int i = 0;i<=num1;i++) //y
      {
	int num2t = int(i*1./num1*num2)+1;
	for(int j = 0;j<=num2t;j+) //x
	  for(int k = 0;k<num3;k++) //phi
	  {
	    y = -height*i/num1;
	    x = -wedth*j/num2t;
	    phi = 2*M_PI/5*k/num3;
	    if(Pentagon::get().check(x,y,phi,&unit)>maxnum)
	    {
	      maxx = x;
	      maxy = y;
	      maxphi = phi;
	      maxnum = num;
	    }
	  }
      }
      cout<<"Max:"<<endl;
      cout<<"x: "<<maxx<<endl;
      cout<<"y: "<<maxy<<endl;
      cout<<"phi: "<<maxphi<<endl;
      cout<<"num: "<<maxnum<<endl;
      return maxnum;
      */
      return 1;
    }
    double coverage()
    {
      return 0.58;//PMTnum()*m_unitArea/area()/25/25;
    }
};
#endif
