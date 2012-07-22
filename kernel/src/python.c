#include <pm.h>

#define HEAP_SIZE 0x2000

extern unsigned char usrlib_img[];


void call_python() {
    uint8_t heap[HEAP_SIZE];
    pm_init(heap, HEAP_SIZE, MEMSPACE_PROG, usrlib_img);
    pm_run((uint8_t *)"main");
}
