extern interrupt_handler0
extern keyboard_interrupt
extern interrupt_handler49

interrupt0:
    pushad
    call interrupt_handler0
    popad
    iret

interrupt33:
    pushad
    call keyboard_interrupt
    popad
    iret

interrupt49:
    pushad
    call interrupt_handler49
    popad
    iret
