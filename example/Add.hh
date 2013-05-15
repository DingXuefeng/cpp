#ifndef Add_H
#define Add_H
#include "Calculator.hh"
#include <iostream>
using namespace std;
class Add : public Calculator
{
  public:
    Add(int a,int b):Calculator(a,b){};
    void getresult()
    {
      cout<<m_a+m_b<<endl;
    }
};
#endif
