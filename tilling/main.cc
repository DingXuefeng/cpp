#include "Fill.h"
#include "FillC60.h"
int main()
{
  Fill* fill = new FillC60();
  fill->tiling();
  fill->showResult();
}
