#include <stdio.h>

int main(void)
{
  float x, y;
  printf("Input first integer: ");
  scanf("%f", &x);
  printf("Input second integer: ");
  scanf("%f", &y);
  printf("\n%.3f * %.3f + %.3f * %.3f --> %.3f\n", x, x, y, y, x * x + y * y);
}
