#include "Angle.h"
#include <cmath>
#include <iostream>
using namespace std;
int main()
{
  double ACUx,ACUy,ACUz,PMTx,PMTy,PMTz,R;
  cin>>ACUx>>ACUy>>ACUz>>PMTx>>PMTy>>PMTz>>R;
  Angle a;
  a.read(ACUx,ACUy,ACUz,PMTx,PMTy,PMTz,R);
  cout<<"ACU=("<<ACUx<<","<<ACUy<<","<<ACUz<<")"<<endl;
  cout<<"PMT=("<<PMTx<<","<<PMTy<<","<<PMTz<<")"<<endl;
  cout<<"theta="<<a.theta()<<endl;
}
