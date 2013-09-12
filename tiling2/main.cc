#include "ProcessManager.h"
using namespace std;
int main()
{
  ProcessManager* processManager = new ProcessManager();
  //processManager->setPolygon(5,25.41);
  //processManager->setPolygon(5,25.01);
  processManager->setPolygon(6,5.486);
  processManager->set(90,0,0);
  processManager->init();
  processManager->run();
  processManager->print();
  delete processManager;
}
