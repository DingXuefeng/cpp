#include <iostream>
using namespace std;
class Child : public Human
{
  public:
    void sayhello()
    {
      cout<<"I want gift"<<endl;
    }

    void play()
    {
      cout<<"I'm playing"<<endl;
    }
};
