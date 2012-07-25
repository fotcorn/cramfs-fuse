# compiler
CC=i586-elf-gcc
LD=i586-elf-ld
CFLAGS=-c -m32 -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I ../../pymite/src/vm -I ../../pymite/src/platform/pyos -I src
NASMLFAGS=-f elf

LDFLAGS=-melf_i386 -T src/linker.ld

PMIMGCREATOR=../../pymite/src/tools/pmImgCreator.py
PMIMGCREATOR_FLAGS=-f ../../pymite/src/platform/pyos/pmfeatures.py -c -u

# files
C_SOURCES=$(wildcard src/*.c)
C_HEADERS=$(wildcard src/*.h)
C_OBJECTS=$(patsubst src/%.c, build/%.o, $(C_SOURCES)) $(patsubst build/%.c, build/%.o, $(PYTHON_C_SOURCES))

ASM_SOURCES=src/kernel_asm.asm src/loader.asm 
ASM_OBJECTS=build/kernel_asm.o build/loader.o

PYTHON_SOURCES=$(wildcard src/python/*.py)
PYTHON_C_SOURCES=build/python_img.c build/python_nat.c

KERNEL_BIN=build/kernel.bin
ISO=cd.iso

all: $(ISO)

$(ISO): $(KERNEL_BIN)
	cp $(KERNEL_BIN) iso
	grub-mkrescue -o $(ISO) iso

$(KERNEL_BIN): $(ASM_OBJECTS) $(C_OBJECTS)
	$(LD) $(LDFLAGS) -o $(KERNEL_BIN) $(ASM_OBJECTS) $(C_OBJECTS) ../../pymite/src/vm/libpmvm_pyos.a ../../pymite/src/platform/pyos/plat.o ../../gcccross/install/i586-elf/lib/libc.a
	
build/%.o: src/%.c $(C_HEADERS) python_image
	$(CC) $(CFLAGS) -o $@ $<

build/%.o: src/%.asm
	nasm $(NASMLFAGS) -o $@ $<

python_image: $(PYTHON_SOURCES)
	../../pymite/src/tools/pmImgCreator.py -f ../../pymite/src/platform/pyos/pmfeatures.py -c -u -o build/python_img.c --native-file=build/python_nat.c $(PYTHON_SOURCES)

clean:
	rm -rf build
	mkdir build
	mkdir build/python
	