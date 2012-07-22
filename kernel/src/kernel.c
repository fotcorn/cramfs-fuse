#include "screen.h"
#include "pic.h"
#include "python.h"

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>


struct test{
	int a;
	short b;
	char c;
};

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

    printf("hello printf!\n");
    printf("hello int: %d\n", 25);

    call_python();

    while (1) {}
}
