#ifndef Human_H
#define Human_H
#include "Animal.hh"
#include <iostream>
using namespace std;
class Human : public Animal
{
  public:
    virtual void sayhello()
    {
      cout<<"I'm a human, hi!"<<endl;
    };
};
#endif


