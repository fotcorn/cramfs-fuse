# compiler
CC=i586-elf-gcc
LD=i586-elf-ld
CFLAGS=-c -m32 -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I ../../pymite/src/vm -I ../../pymite/src/platform/pyos
NASMLFAGS=-f elf

LDFLAGS=-melf_i386 -T src/linker.ld

PMIMGCREATOR=../../pymite/src/tools/pmImgCreator.py
PMIMGCREATOR_FLAGS=-f ../../pymite/src/platform/pyos/pmfeatures.py -c -u

# files
C_SOURCES=$(wildcard src/*.c)
C_HEADERS=$(wildcard src/*.h)
C_OBJECTS=$(patsubst src/%.c, obj/%.o, $(C_SOURCES))

ASM_SOURCES=src/kernel_asm.asm src/loader.asm 
ASM_OBJECTS=obj/kernel_asm.o obj/loader.o

PYTHON_SOURCES=$(wildcard src/python/*.py)
PYTHON_C_SOURCES=$(patsubst src/python/%.py, obj/python/%.c, $(PYTHON_SOURCES))
PYTHON_OBJECTS=$(patsubst obj/python/%.c, obj/python/%.o, $(PYTHON_C_SOURCES))

KERNEL_BIN=obj/kernel.bin
ISO=cd.iso

all: $(ISO)

$(ISO): $(KERNEL_BIN)
	cp $(KERNEL_BIN) iso
	grub-mkrescue -o $(ISO) iso

$(KERNEL_BIN): $(ASM_OBJECTS) $(C_OBJECTS) $(PYTHON_OBJECTS) obj/python/main_nat.o
	$(LD) $(LDFLAGS) -o $(KERNEL_BIN) $(ASM_OBJECTS) $(C_OBJECTS) $(PYTHON_OBJECTS) ../../pymite/src/vm/libpmvm_pyos.a ../../pymite/src/platform/pyos/plat.o ../../gcccross/install/i586-elf/lib/libc.a obj/python/main_nat.o
	
obj/%.o: src/%.c $(C_HEADERS)
	$(CC) $(CFLAGS) -o $@ $<

obj/%.o: src/%.asm
	nasm $(NASMLFAGS) -o $@ $<

obj/python/%.c: src/python/%.py
	$(PMIMGCREATOR) $(PMIMGCREATOR_FLAGS) -o $@ $<

obj/python/%.o: src/python/%.c
	$(CC) $(CFLAGS) -o $@ $<

obj/python/main_nat.o:
	../../pymite/src/tools/pmImgCreator.py -f ../../pymite/src/platform/pyos/pmfeatures.py -c -u -o obj/python/main.c --native-file=obj/python/main_nat.c src/python/main.py
	$(CC) $(CFLAGS) -o obj/python/main_nat.o obj/python/main_nat.c

clean:
	rm -rf obj
	mkdir obj
	mkdir obj/python
	