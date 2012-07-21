[BITS 32]
global init_kernel

%define BASE_OF_SECTION 0x00100000

init_kernel:
    cli
    ; init gdt
    lgdt [ gdtr ]

    ; reload selectors
    jmp   0x08:reload_selectors ; 0x08 points at the new code selector

init_idtr:
    lidt [ idtr ]
    ret

; init idt

;mov eax, interrupt1
;mov [idt+49*8], ax
;mov eax, gdt_codesel
;mov word [idt+49*8+2], ax
;mov byte [idt+49*8+4], 0h
;mov byte [idt+49*8+5], 08Eh
;mov eax, interrupt1
;shr eax,16
;mov [idt+49*8+6], ax

reload_selectors:
   mov ax, 0x10 ; data selector
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
    dw (BASE_OF_SECTION + interrupt0 - $$) & 0ffffh ; offset 1
    dw 08h ; second selector (code)
    db 0 ; zero (unused)
    db 08Eh ; type and attributes: ; present: 1 ; DPL: 00 ; Storage segment: 0 ; type: 0xE (32bit interrupt gate); 0
    dw (BASE_OF_SECTION + interrupt0 - $$) >> 16 ; offset 2

    resd 32*2 ; zero out interrupts 1- 32

    dw (BASE_OF_SECTION + interrupt33 - $$) & 0ffffh ; offset 1
    dw 08h ; second selector (code)
    db 0 ; zero (unused)
    db 08Eh  ; type and attributes: ; present: 1 ; DPL: 00 ; Storage segment: 0 ; type: 0xE (32bit interrupt gate); 0
    dw (BASE_OF_SECTION + interrupt33 - $$) >> 16 ; offset 2

    resd 15*2 ; zero out interrupts 1- 32

    dw (BASE_OF_SECTION + interrupt49 - $$) & 0ffffh ; offset 1
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
    dw 0ffffh      ; limit: 65k
    dw 0           ; base: 0
    db 0           ; base: 0
    db 09ah        ; access bytes: code
    db 0cfh        ; flags (1100) : limit(0xFF)
    db 0h          ; base: 0
gdt_datasel:
    dw 0ffffh      ; limit: 65k
    dw 0h          ; base: 0
    db 0h          ; base: 0
    db 092h        ; access bytes: data
    db 0cfh        ; flags (1100) : limit(0xFF)
    db 0           ; base: 0
gdt_end:


%include "src/interrupts.asm"

