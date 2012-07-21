# compiler
CC=gcc
CFLAGS=-c -m32 -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I src/libc
NASMLFAGS=-f elf

# files
C_SOURCES=$(wildcard src/*.c) $(wildcard src/libc/*.c)
C_HEADERS=$(wildcard src/*.h) $(wildcard src/libc/*.h)
C_OBJECTS=$(patsubst src/%.c, obj/%.o, $(C_SOURCES))

ASM_SOURCES=src/kernel_asm.asm src/loader.asm 
ASM_OBJECTS=obj/kernel_asm.o obj/loader.o

KERNEL_BIN=obj/kernel.bin
ISO=cd.iso

all: $(ISO)

$(ISO): $(KERNEL_BIN)
	cp $(KERNEL_BIN) iso
	grub-mkrescue -o $(ISO) iso

$(KERNEL_BIN): $(ASM_OBJECTS) $(C_OBJECTS)
	ld -melf_i386 -T src/linker.ld -o $(KERNEL_BIN) $(ASM_OBJECTS) $(C_OBJECTS)
	
obj/%.o: src/%.c $(C_HEADERS)
	$(CC) $(CFLAGS) -o $@ $<

obj/%.o: src/%.asm
	nasm $(NASMLFAGS) -o $@ $<

clean:
	rm -rf obj
	mkdir obj
	mkdir obj/libc