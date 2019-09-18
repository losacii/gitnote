#include <stdio.h>
#include <time.h>

void delay(int milli_seconds);

int main(void)
{
  printf("CLOCKS_PER_SEC: %ld\n\n", CLOCKS_PER_SEC);

  for (int i = 0; i < 5; i++) {
    printf("...delay 1000 milli-seconds >> "); fflush(stdout);
    delay(1000);
    printf("now time is: %ld\n", clock());
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

