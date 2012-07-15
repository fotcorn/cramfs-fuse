#include "screen.h"

void interrupt_handler0() {
	print("divide by zero");
}

void interrupt_handler49() {
	print("interrupt 49 called!");
}
