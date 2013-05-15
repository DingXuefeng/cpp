#include <iostream>
#include <string>
using namespace std;
class Man : public Human
{
  public:
    void sayhello(string name)
    {
      cout<<"I'm "<<name<<",";
      cout<<"Let's have a fight"<<endl;
    }

    void play()
    {
      cout<<"I'm playing"<<endl;
    }
};
