
#include <stdio.h>
#include <time.h>

void delay(int); // 0.001 seconds

int main(void)
{
  int count = 0;
  for(int i=1; ; i *= 2)
  {
    count++;
    printf("%6d: %d\n", count, i);
    delay(200);
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

/* Result:
     1: 1
     2: 2
     3: 4
     4: 8
     5: 16
     6: 32
     7: 64
     8: 128
     9: 256
    10: 512
    11: 1024
    12: 2048
    13: 4096
    14: 8192
    15: 16384
    16: 32768
    17: 65536
    18: 131072
    19: 262144
    20: 524288
    21: 1048576
    22: 2097152
    23: 4194304
    24: 8388608
    25: 16777216
    26: 33554432
    27: 67108864
    28: 134217728
    29: 268435456
    30: 536870912
    31: 1073741824
    32: -2147483648
    33: 0
    34: 0
    35: 0
    36: 0
    37: 0
    38: 0
    39: 0
    40: 0
*/
