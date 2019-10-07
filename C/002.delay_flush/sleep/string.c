#include <stdio.h>
#include <unistd.h> 

int main(void)
{
  for(int i=0; i<8; i++)
  {
    sleep(1);
    printf("%d\n", i);
  }
}
