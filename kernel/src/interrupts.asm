
interrupt0:
    pushad
    call interrupt_handler0
    popad
    iret

interrupt49:
    pushad
    call interrupt_handler49
    popad
    iret
