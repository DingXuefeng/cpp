#ifndef Animal_H
#define Animal_H
class Animal
{
  public:
    virtual void doSomething()
    {
      sayhello();
    };
    virtual void sayhello(){} = 0;
};
#endif


