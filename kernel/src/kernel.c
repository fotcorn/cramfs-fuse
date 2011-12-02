void kmain( void* mbd, unsigned int magic )
{
   unsigned char *videoram = (unsigned char *) 0xb8000;
   videoram[0] = 65; /* character 'A' */
   videoram[1] = 0x07; /* light grey (7) on black (0). */
}
