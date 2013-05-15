#ifndef Calculator_H
#define Calculator_H
class Calculator
{
  public: Calculator(int a,int b):m_a(a),m_b(b){}; //new Calculator(a,b);
    virtual void getresult(){};
    void set(int a,int b){m_a=a;m_b=b;}
  protected:
    int m_a,m_b;
};
#endif
