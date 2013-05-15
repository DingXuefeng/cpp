#ifndef Fill_H
#define Fill_H
#include <iostream>
#include <vector>
#include "Tiling.h"
using namespace std;
class Fill
{
  public:
    Fill() :
      m_methodlist(),m_methodNlist(),m_methodArealist(){};
    ~Fill()
    {
      for(vector<Tiling*>::size_type ix=0;ix!=m_methodlist.size();++ix)
      {
	delete m_methodlist[ix];
      }
    }
    virtual void tiling() = 0;
    virtual void addMethod(Tiling* tiling,int num,double length)
    {
      m_methodlist.push_back(tiling);
      m_methodNlist.push_back(num);
      m_methodArealist.push_back(tiling->area()*length*length); //area() returns area with length =1
    }
    virtual int getNum()
    {
      int totalNum = 0;
      for(vector<Tiling*>::size_type ix=0;ix!=m_methodlist.size();++ix)
      {
	totalNum += m_methodlist[ix]->PMTnum();
      }
      return totalNum;
    }
    virtual double getCoverage()
    {
      double totalArea(0.);
      double coverArea(0.);
      for(vector<Tiling*>::size_type ix=0;ix!=m_methodlist.size();++ix)
      {
	totalArea += m_methodArealist[ix];
	coverArea += m_methodArealist[ix]*m_methodlist[ix]->coverage();
      }
      return coverArea/totalArea;
    }
    void showResult()
    {
      for(vector<Tiling*>::size_type ix=0;ix!=m_methodlist.size();++ix)
      {
	cout<<"Method "<<ix<<" :"<<endl;
	cout<<"Coverage: "<<m_methodlist[ix]->coverage()<<endl;
	cout<<"Number of it: "<<m_methodNlist[ix]<<endl;
	cout<<"Area of it: "<<m_methodArealist[ix]<<endl;
      }
      cout<<"Total number of PMT: "<<getNum()<<endl;
      cout<<"Total coverage: "<<getCoverage()<<endl;
    }

  private:
    vector<Tiling*> m_methodlist;
    vector<int> m_methodNlist;
    vector<double> m_methodArealist;
};
#endif
