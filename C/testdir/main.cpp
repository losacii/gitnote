#include "common.cpp"

int main()
{
    /* Say Hello! */
    logn("Hello World!");  

    /* put string */
    putstr("test put string");

    /* delay function */
    delay(600);

    /* for loop */
    for (int i=0; i<20; i++) 
    {
        log("~ ~ ");
        delay(5); 
        fflush(stdout);
    }
    log('\n');

    /* sizeof - data length */
    std::cout << "length of char: " << sizeof(char) << std::endl;
    std::cout << "length of int: " << sizeof(int) << std::endl;
    std::cout << "length of long: " << sizeof(long) << std::endl;
    std::cout << "length of float: " << sizeof(float) << std::endl;
    std::cout << "length of double: " << sizeof(double) << std::endl;
    std::cout << "length of bool: " << sizeof(bool) << std::endl;


    // A pointer is just a memory address!
    int var = 8;
    int* ptr = &var;

    // A pointer is just a memory address!
    logn(ptr); 

    // get the value with pointer: * for dereference
    logn(*ptr); 

    // This is some kind of hack action.
    logn(*(ptr + 1)); 
    logn(*(ptr + 2)); 
    logn(*(ptr + 3)); 

}
