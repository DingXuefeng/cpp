#ifndef Change_H
#define Change_H
#include <iostream>
using namespace std;
class Change
{
  public:
    virtual void change() = 0;
    virtual void becomeBird()
    {
      cout<<"I'm a bird now"<<endl;
    }
};
#endif
