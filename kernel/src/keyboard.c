#include "screen.h"
#include "pic.h"

void keyboard_interrupt() {
	print("key pressed");
	pic_eoi(0x1);
}
