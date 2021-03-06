#include <iostream>
#include <stdio.h>
#include <time.h>

#define log(x)  std::cout << x;
#define logn(x) std::cout << x << std::endl;

void delay(int milli_seconds)
{
  long interv = milli_seconds * CLOCKS_PER_SEC / 1000;

  clock_t then = clock();

  // check time elapsed
  while (clock() - then < interv)
    ;
}


/* 
 * log(x)
 * logn(x)
 * delay(milli_seconds)
 */
