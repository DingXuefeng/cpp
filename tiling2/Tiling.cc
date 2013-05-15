#include "Tiling.h"
#include "node.h"
#include <vector>
#include <cmath>
#include <fstream>
//#include <iostream>
#include "TFile.h"
#include "TTree.h"
using namespace std;
const node Tiling::m_e1(1.0,0);
const node Tiling::m_e2(0.5,sqrt(3)/2);
const node Tiling::m_ep1(m_e1+m_e2);
const node Tiling::m_ep2(m_e2*2-m_e1);
bool Tiling::m_inside(node* point) const
{
  if(point->distance()<r())
    return true;
  else
  {
    double theta;
    theta = acos(point->x()/point->distance());
    theta = point->y()>0?theta:2*M_PI-theta;
    double delta = theta-(initTheta()/180*M_PI-2*unitDelta());
    delta = abs(delta-int(delta/unitDelta())*unitDelta()-unitDelta()/2.);
#ifdef DEBUG
    cout<<"x : "<<x<<" y : "<<y<<endl;
    cout<<"theta: "<<theta/M_PI*180<<endl;
    cout<<"delta: "<<delta/M_PI*180<<endl;
    cout<<"r() "<<r()<<endl;
    cout<<"unitDelta() "<<unitDelta()/M_PI*180<<endl;
    cout<<"distance "<<point->distance()<<endl;
    cout<<"distance*cos(delta) "<<point->distance()*cos(delta)<<endl;
#endif
    if(point->distance()*cos(delta)>r())
      return false;
    return true;
  }
}
bool Tiling::inside(node* p) const
{
  node* checkpoint = new node();
  for(int i = 0;i<6;i++)
  {
    checkpoint->x(p->x()+cos(i*60./180*M_PI));
    checkpoint->y(p->y()+sin(i*60./180*M_PI));
    if(!m_inside(checkpoint))
    {
      delete checkpoint;
      return false;
    }
  }
  delete checkpoint;
  return true;
}
int Tiling::PMT()
{
  const int MAX = 100;
  int n = 0;
  node* checkP;
  clear();
  for(int ia = -MAX;ia<MAX;++ia)
    for(int ib = -MAX;ib<MAX;++ib)
    {
      checkP = new node((m_ep1*ia)+(m_ep2*ib)+m_origin);
      if(inside(checkP))
      {
	++n;
	m_putted.push_back(checkP);
      }
      else
	delete checkP;
    }
  return n;
}
void Tiling::print()
{
  /*
  cout<<"r of inner circle: "<<m_r<<endl;
  cout<<"r of outer circle: "<<m_r/cos(unitDelta()/2)<<endl;
  cout<<"length of side: "<<m_r*tan(unitDelta()/2)*2<<endl;
  cout<<"//-------------------------------"<<endl;
  */
  if(m_putted.size()==0)
    PMT();
  ofstream data("data.txt");
  data<<" l "<<m_l*unitLength()<<endl;
  data<<" n "<<n()<<endl;
  data<<" theta "<<initTheta()<<endl;
  TFile output("out.root","RECREATE");
  TTree tree("tree","tree");
  double x,y;
  tree.Branch("x",&x,"x/D");
  tree.Branch("y",&y,"y/D");
  node point(0,0);
  for(vector<node*>::size_type ix = 0;ix!=m_putted.size();ix++)
  {
      //cout<<"m_putted["<<ix<<"]== ";
      //m_putted[ix]->print();
      point = (*m_putted[ix])*unitLength();
      x = point.x();
      y = point.y();
      data<<x<<" "<<y<<endl;
      tree.Fill();
  }
  tree.Write();
  output.Close();
  data.close();
  //cout<<"--------------------------------//"<<endl;
  cout<<"total PMT number: "<<m_putted.size()<<endl;
  cout<<"length of side: "<<m_l<<endl;
}

