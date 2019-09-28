#include <iostream>

#define log(x)  std::cout << x;
#define logn(x) std::cout << x << std::endl;

#include <stdio.h>
#include <time.h>

void delay(int milli_seconds)
{
  long interv = milli_seconds * CLOCKS_PER_SEC / 1000;

  clock_t then = clock();

  // check time elapsed
  while (clock() - then < interv)
    ;
}


