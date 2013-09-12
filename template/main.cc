#include <iostream>
template <typename T> 
inline const T& maximum(const T& x,const T& y)
{
  if(y>x)
    return y;
  else
    return x;
}
int main()
{
  using namespace std;
  cout<<maximum<int>(3,7)<<endl;
  cout<<maximum(3,7)<<endl;
  cout<<maximum(3.0,7.5)<<endl;
  cout<<maximum<double>(3.0,7.5)<<endl;
  //cout<<maximum(3,7.5)<<endl;
}
