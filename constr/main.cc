#include <iostream>
using namespace std;
class a
{
  public:
    a(double a){cout<<"Hi!"<<endl;};
};
int main()
{
  a* b;
  b=new a;
}
