nasm -f elf src/loader.asm -o obj/loader.o
nasm -f elf src/kernel.asm -o obj/kernel_asm.o
gcc -c -m32 -o obj/kernel.o src/kernel.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I src/libc
gcc -c -m32 -o obj/screen.o src/screen.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I src/libc
gcc -c -m32 -o obj/interrupts.o src/interrupts.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I src/libc
gcc -c -m32 -o obj/strlen.o src/libc/strlen.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs
gcc -c -m32 -o obj/io.o src/io.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs
gcc -c -m32 -o obj/pic.o src/pic.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs
gcc -c -m32 -o obj/keyboard.o src/keyboard.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs

ld -melf_i386 -T src/linker.ld -o obj/kernel.bin obj/loader.o obj/kernel_asm.o obj/interrupts.o obj/kernel.o obj/screen.o obj/strlen.o obj/io.o obj/pic.o obj/keyboard.o
cp obj/kernel.bin iso
grub-mkrescue -o cd.iso iso
#bochs
