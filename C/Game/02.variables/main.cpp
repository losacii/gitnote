#include <iostream>

int main()
{
    int kittens = 100;
    
    for (int i=0; i<5; i++)
    {
        kittens += 1;
    }

    std::cout << "kitten count: " << kittens << std::endl;
    return 0;
}

/*
   g++ main.cpp -o main.out
*/

