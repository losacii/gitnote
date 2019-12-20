#include "main.h"

int main(int argc, char* argv[])
{
  logn("hello cpp!!!")
  printf("CLOCKS_PER_SEC: %ld\n\n", CLOCKS_PER_SEC);

  for (int i = 0; i < 5; i++) {
    printf("...delay 50 milli-seconds >> "); fflush(stdout);
    delay(50);
    printf("now time is: %ld\n", clock());
  }
  return 0;
}
