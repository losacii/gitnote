#include <iostream>
#include <stdio.h>
#include <time.h>

#include "common.h"

void putstr(const char* message)
{
    std::cout << message << std::endl;
}


void delay(int milli_seconds)
{
  long interv = milli_seconds * CLOCKS_PER_SEC / 1000;

  clock_t then = clock();

  // check time elapsed
  while (clock() - then < interv)
    ;
}
