#include <pm.h>

extern unsigned char usrlib_img[];

void call_python() {
    PmReturn_t retval;
    pm_init(MEMSPACE_PROG, usrlib_img);
    retval = pm_run((uint8_t *)"main");
}
