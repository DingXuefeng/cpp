#define DEBUG
#include "Tiling.h"
#include "Pentagon.h"
#include "Polygon.h"
#include "node.h"
#include "TRandom3.h"
#include <ctime>
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
  Tiling mytile;
  Polygon* board = new Pentagon();
  mytile.setIn(board);
  mytile.l(28.001);
  mytile.initOrigin(0,0,0);
  TRandom3 random(time(NULL));
  const int MAX = 10;
  node* point;
  double x,y;
  mytile.inside(new node(-1,0));
  double max = MAX/mytile.unitLength();
  for(int i =0;i<2000000;i++)
  {
    double r = mytile.r()-2+random.Rndm()*7;
    double theta = (random.Rndm()-0.5)*2*M_PI;
    x = r*cos(theta);
    y = r*sin(theta);
    point = new node(x,y);
    if(mytile.inside(point))
      mytile.push(point);
    else
      delete point;
  }
  mytile.print();
}
