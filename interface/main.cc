#include "Animal.h"
#include "Change.h"
#include "Zhubajie.h"
#include "Walle.h"
#include <vector>
using namespace std;
int main()
{
  Zhubajie* bajie = new Zhubajie();
  Animal* p = bajie;
  bajie->becomeWhat = "fish";
  vector<Change*> changeDisplay;
  changeDisplay.push_back(bajie);
  changeDisplay.push_back(new Walle());
  changeDisplay[0]->change();
  changeDisplay[1]->change();
}
