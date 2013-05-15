#ifndef MyHuman_H
#define MyHuman_H
#include "Human.hh"
#include <iostream>
using namespace std;
class MyHuman : public Human 
{
  public:
    virtual void sayhello()
    {
      cout<<"I'm another kind of human, hi!"<<endl;
    };
};
#endif


