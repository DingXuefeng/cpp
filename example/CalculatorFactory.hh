#ifndef CalculatorFactory_H
#define CalculatorFactory_H
#include "Calculator.hh"
#include "Add.hh"
#include "Sub.hh"
#include <string>
using namespace std;
class CalculatorFactory
{
  public:
    static Calculator* createCalculator(string operators,int a,int b)
    {
      Calculator* calculator;
      if(operators=="+")
	calculator = new Add(a,b);
      else if(operators=="-")
	calculator = new Sub(a,b);
      return calculator;
    }
};
#endif
