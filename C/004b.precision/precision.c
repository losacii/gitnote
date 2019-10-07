#include <stdio.h>

int main(void)
{
  printf( "result a: %f\n",    1.0f / 10.0f );
  printf( "result b: %.16f\n", 1.0f / 10.0f );
  printf( "result b: %.50f\n", 1.0f / 10.0f );
}


/*

:!clang precision.c && ./a.out
result a: 0.100000
result b: 0.1000000014901161
result b: 0.10000000149011611938476562500000000000000000000000

*/
