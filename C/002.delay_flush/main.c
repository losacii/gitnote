#include <stdio.h>
#include <time.h>

void delay(int milli_seconds);

int main(void)
{
  for (int i = 0; i < 5; i++) {
    printf("(Sleep 1 second...)"); fflush(stdout);
    delay(1000);
    printf("---> now time is: %ld\n", clock());
  }
}

void delay(int milli_seconds)
{
  long interv = milli_seconds * CLOCKS_PER_SEC / 1000;

  clock_t then = clock();

  // check time elapsed
  while (clock() - then < interv)
    ;
}

