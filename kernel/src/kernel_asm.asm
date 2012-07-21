[BITS 32]
global init_kernel

%define BASE_OF_SECTION 0x100000 ; see linker.ld

init_kernel:
    cli
    ; init gdt
    lgdt [ gdtr ]

    ; reload selectors
    jmp   0x08:reload_selectors ; 0x08 points at the new code selector

    ; init idt
init_idtr:
    lidt [ idtr ]

    ; init fpu
    ;mov edx, cr0
    ;or edx, 0b100010
    ;and edx, !0b100
    ;mov cr0, edx
     ; MP = 1 bit1
     ; EM = 0 bit 2
     ; NE = 1 bit 5
    fninit

    ret

reload_selectors:
   mov ax, 010h ; data selector
   mov ds, ax
   mov es, ax
   mov fs, ax
   mov gs, ax
   mov ss, ax
   jmp init_idtr

; IDT
idtr:
    dw idt_end-idt-1
    dd idt
idt:
    dw (BASE_OF_SECTION + interrupt0 - $$) & 0xFFFF ; offset 1
    dw 08h ; second selector (code)
    db 0 ; zero (unused)
    db 08Eh ; type and attributes: ; present: 1 ; DPL: 00 ; Storage segment: 0 ; type: 0xE (32bit interrupt gate); 0
    dw (BASE_OF_SECTION + interrupt0 - $$) >> 16 ; offset 2

    resd 32*2 ; zero out interrupts 1- 32

    dw (BASE_OF_SECTION + interrupt33 - $$) & 0xFFFF ; offset 1
    dw 08h ; second selector (code)
    db 0 ; zero (unused)
    db 08Eh  ; type and attributes: ; present: 1 ; DPL: 00 ; Storage segment: 0 ; type: 0xE (32bit interrupt gate); 0
    dw (BASE_OF_SECTION + interrupt33 - $$) >> 16 ; offset 2

    resd 15*2 ; zero out interrupts 1- 32

    dw (BASE_OF_SECTION + interrupt49 - $$) & 0xFFFF ; offset 1
    dw 08h ; second selector (code)
    db 0 ; zero (unused)
    db 08Eh  ; type and attributes: ; present: 1 ; DPL: 00 ; Storage segment: 0 ; type: 0xE (32bit interrupt gate); 0
    dw (BASE_OF_SECTION + interrupt49 - $$) >> 16 ; offset 2
idt_end:



; GDT (http://wiki.osdev.org/GDT)
gdtr:
    dw gdt_end-gdt-1 ; length of gdt
    dd gdt           ; memory location of gdt

gdt:
; nullseg
    dd 0
    dd 0
gdt_codesel:
    dw 0xffff      ; limit: 65k
    dw 0           ; base: 0
    db 0           ; base: 0
    db 0x9A        ; access bytes: code
    db 0xCF        ; flags (1100) : limit(0xFF)
    db 0          ; base: 0
gdt_datasel:
    dw 0xffff      ; limit: 65k
    dw 0           ; base: 0
    db 0           ; base: 0
    db 0x92        ; access bytes: data
    db 0xCF        ; flags (1100) : limit(0xFF)
    db 0           ; base: 0
gdt_end:


%include "src/interrupts.asm"

