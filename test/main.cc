#include <iostream>
using namespace std;
int main()
{
  double a;
#ifdef A
  a=1;
#else
  a=2;
#endif
  cout<<a<<endl;
}
