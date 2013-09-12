#include <functional>
#include <vector> 
#include <algorithm>
#include <iostream>

using namespace std;

class out_times_x 
{
public:
  out_times_x(const int& k) : multiplier(k) { }
  void operator()(const int& x) { cout << x * multiplier << " " << endl; }
  
private:
  int multiplier;
};

int main ()
{
  int sequence[5] = {1,2,3,4,5};  
  vector<int>  v(sequence+0, sequence+5);
  
  out_times_x f2(2);
  f2(3);
  
  for_each(v.begin(),v.end(),f2);   // Apply function
  system("sleep 1");
  return 0;
}
