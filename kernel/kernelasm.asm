; * kernelasm.asm : FritzOS C++ Kernel Assembly Routines and Second Stage Loader
;   Copyright (C) 2002 Tom Fritz
;
; * This program is a part of the FritzOS kernel, and may be freely
; * copied under the terms of the GNU General Public License (GPL),
; * version 2, or at your option any later version.
;   
;   For more info, look at the COPYING file.
;

; Tell NASM that this is 32-bit PMode code
[BITS 32]

; This is loaded first, so let NASM know that there is a C++ Kernel

	EXTERN start			; The FritzOS C++ Kernel main function.

; This tells NASM that in the C++ kernel there is a function called 'start_textmode'

	EXTERN start_textmode		; We need this so we can print messages.

; This tells NASM that in the C++ kernel there is a function called 'LoadingGDTMsg'

	EXTERN LoadingGDTMsg		; We need this so the user knows the GDT is being loaded.

; This tells NASM that in the C++ kernel there is a function called 'CheckVid'

	EXTERN CheckVid		; We need this to check if a video or color card is installed.

; This tells NASM to tell GCC that the memcpy function is defined here.

	GLOBAL memcpy

; This tells NASM to tell GCC that the memset function is defined here.

	GLOBAL memset

; Registers Value Getting Functions For The C++ Kernel:
GLOBAL geteax
GLOBAL getebx
GLOBAL getecx
GLOBAL getedx
GLOBAL getcs
GLOBAL getds
GLOBAL getes
GLOBAL getfs
GLOBAL getgs
GLOBAL getss
GLOBAL getebp
GLOBAL getesp
GLOBAL geteflags

; We don't make StartA20 a GLOBAL variable to be used in the FritzOS C Kernel because, we don't
; want to change anything like that in the C Kernel right now. 

; This is where the FritzOS Assembly Kernel starts; we get here from boot.asm
AsmStart:
	; Start Textmode functions:
	call start_textmode

	; First, test for the correct video card, from the C++ kernel:
	call CheckVid

	; Load the GDT; this is needed to set up where all the code and data goes:
	; Print a message that says the GDT is being loaded:
	call LoadingGDTMsg
	lgdt [ GDTR ]		; enter pmode

	; Jump, or go, to the the FritzOS C Kernel
	jmp start	; Jump, or go to, the FritzOS C Kernel

	jmp $		; If the kernel wasn't loaded, freeze, but this shouldn't happen

; End of asmstart

; memcpy: Memory Copy Funciton for the FritzOS C Kernel.
; It's defined here because it's in assembly language.

; This is what the C definition code would look like:
; extern void* memcpy( void* to, const void* from, size_t count );

memcpy:
	push ebp
	mov ebp, esp
	mov esi, [ebp + 8]	; First Argument: src pointer
	mov edi, [ebp +12]	; Second Argument: dest pointer
	mov ecx, [ebp + 16]	; Third Argument: string size in bytes
	mov eax, edi		; Return Value: Save Now, before EDI changes
	cld			; Make sure direction flag set correctly
	rep movsb		; Block-Copy from src to dest
	pop ebp			; Restore Caller's stack frame
	ret

; End of memcpy

; memset: Memory Set Funciton for the FritzOS C Kernel.
; It's defined here because it's in assembly language.

; This is what the C definition code would look like:
; extern void* memset( void* buf, int ch, size_t cont );

memset:
	push ebp
	mov ebp, esp
	mov edi, [ebp + 8]		; First Argument: buffer pointer
	mov edi, [ebp +12]		; Second Argument: value to write
	mov eax, [ebp + 16]		; Third Argument: string size in bytes
	push edi			; Return Value: Save Now, before EDI changes
	cld				; Make sure direction flag set correctly
	rep stosb
	pop eax				; Recover return value
	pop ebp				; Restore Caller's stack frame
	ret

; End of memset

;*************************************************************************************************************
; GDTR

; Make a new GDT for the IDT
; Global Descriptor Table: This tells the computer where all the segments ( now selectors ) are.
GDTR
    dw gdt_end-1
      dd gdt
gdt
nullsel equ $-gdt
gdt0
          dd 0
          dd 0
CodeSel equ $-gdt
          dw 0ffffh
          dw 0
          db 0
          db 09ah
          db 0cfh
          db 0h
DataSel equ $-gdt
        dw 0ffffh
        dw 0h
        db 0h
        db 092h
        db 0cfh
        db 0
gdt_end

; End of GDTR

; For Getting The Register Values, For The C++ Kernel:
geteax:					; unsigned long geteax();
	ret

getebx:					; unsigned long getebx();
	mov eax, ebx
	ret

getecx:					; unsigned long getecx();
	mov eax, ecx
	ret

getedx:					; unsigned long getedx();
	mov eax, edx
	ret

getcs:					; unsigned int getcs();
	mov ax, cs
	ret

getds:					; unsigned int getds();
	mov ax, ds
	ret

getes:					; unsigned int getes();
	mov ax, es
	ret

getfs:					; unsigned int getfs();
	mov ax, fs
	ret

getgs:					; unsigned int getgs();
	mov ax, gs
	ret

getss:					; unsigned int getss();
	mov ax, fs
	ret

getedi:					; unsigned long getedi();
	mov eax, edi
	ret

getesi:					; unsigned long getesi();
	mov eax, esi
	ret

getebp:					; unsigned long getebp();
	mov eax, ebp
	ret

getesp:					; unsigned long getesp();
	mov eax, esp
	ret

geteflags:				; unsigned long geteflags();
	pushfd
	pop eax
	ret

; End of kernelasm.asm
