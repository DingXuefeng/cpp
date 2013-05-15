#ifndef Sub_H
#define Sub_H
#include "Calculator.hh"
#include <iostream>
using namespace std;
class Sub : public Calculator 
{
  public:
    Sub(int a,int b):Calculator(a,b){};
    //new Sub(a,b);
    void getresult()
    {
      cout<<m_a-m_b<<endl;
      surprise();
    }
    void surprise()
    {
      cout<<"Surprise!"<<endl;
    }
};
#endif
