#include "Calculator.hh"
#include "CalculatorFactory.hh"
#include <string>
using namespace std;
int main()
{
  int a = 1;
  int b = 2;
  string operators = "-";
  Calculator* calculator;
  calculator = CalculatorFactory::createCalculator(operators,a,b);
  calculator->getresult();
  //calculator->surprise();
}
  
