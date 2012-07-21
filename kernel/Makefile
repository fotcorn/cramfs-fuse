# compiler
CC=i586-elf-gcc
LD=i586-elf-ld
CFLAGS=-c -m32 -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I src/libc
NASMLFAGS=-f elf

LDFLAGS=-melf_i386 -T src/linker.ld

# files
C_SOURCES=$(wildcard src/*.c)
C_HEADERS=$(wildcard src/*.h)
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
	$(LD) $(LDFLAGS) -o $(KERNEL_BIN) $(ASM_OBJECTS) $(C_OBJECTS) /home/corn/projekte/gcccross/install/i586-elf/lib/libc.a
	
obj/%.o: src/%.c $(C_HEADERS)
	$(CC) $(CFLAGS) -o $@ $<

obj/%.o: src/%.asm
	nasm $(NASMLFAGS) -o $@ $<

clean:
	rm -rf obj
	mkdir obj