nasm -f elf src/loader.s -o obj/loader.o
gcc -m32 -o obj/kernel.o src/kernel.c -nostdlib -fno-builtin -nostartfiles -nodefaultlibs
ld -melf_i386 -T src/linker.ld -o obj/kernel.bin obj/loader.o obj/kernel.o
cp obj/kernel.bin iso
grub-mkrescue -o cd.iso iso
qemu --cdrom cd.iso
