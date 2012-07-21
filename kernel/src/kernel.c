#include "screen.h"
#include "pic.h"

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void kmain( void* mbd, unsigned int magic )
{
	init_pic();

    putch('A');
    putch('B');
    putch('\n');
    putch('A');
    putint(4);
    putint(strlen("test"));

    putch('\n');

    print("test");
    print("pyos 0.001");

    putint(54321);
    /*
    print("Calling interrupt 49");
    asm("int $49");
    int a = 5 / 0;
    */

    printf("hello printf!");
    //printf("hello int: %d", 25);

    while (1) {}
}
