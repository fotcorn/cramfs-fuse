"""__NATIVE__
#include "io.h"
"""

def inb():
    """__NATIVE__
    PmReturn_t retval;
    pPmObj_t port, data;
    int int_port, int_data;

    if (NATIVE_GET_NUM_ARGS() != 1)
    {
        PM_RAISE(retval, PM_RET_EX_TYPE);
        return retval;
    }
    port = NATIVE_GET_LOCAL(0);
    if (OBJ_GET_TYPE(port) != OBJ_TYPE_INT)
    {
        PM_RAISE(retval, PM_RET_EX_TYPE);
        return retval;
    }
    int_port = ((pPmInt_t)port)->val;
    int_data = inb(int_port);

    retval = int_new(int_data, &data);
    NATIVE_SET_TOS(data);

    return retval;
    """

