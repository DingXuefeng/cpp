#include "ProcessManager.h"
using namespace std;
int main()
{
  ProcessManager* processManager = new ProcessManager();
  processManager->setPolygon(6,25.01);
  processManager->set(0,0,0);
  processManager->init();
  processManager->run();
  processManager->print();
  delete processManager;
}
