#include "screen.h"

#include <string.h>

void kmain( void* mbd, unsigned int magic )
{
    putch('A');
    putch('B');
    putch('\n');
    putch('A');
    putint(4);
    putint(strlen("test"));

    putch('\n');

    print("test");
    print("pyos 0.001");
}
