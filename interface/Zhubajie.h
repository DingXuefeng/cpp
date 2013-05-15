#include "Pig.h"
#include "Change.h"
#include <string>
#include <iostream>
using namespace std;
class Zhubajie : public Pig, public Change
{
  public:
    string becomeWhat;
  private:
  void change()
  {
    if(becomeWhat=="")
      becomeBird();
    else
      cout<<"I'm a "<<becomeWhat<<" now."<<endl;
  }
};
