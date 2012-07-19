#include "keyboard.h"

#include "screen.h"
#include "pic.h"

void keyboard_interrupt() {
	pic_eoi(0x1);
	unsigned char scancode = inb(KEYBOARD_IO_PORT);
	putint(scancode);
}
