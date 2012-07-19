// i/o port
#define PIC1_COMMAND 0x20
#define PIC1_DATA 0x21
#define PIC2_COMMAND 0xA0
#define PIC2_DATA 0xA1

// commands
#define PIC_EIO 0x20



void init_pic();
void pic_eoi(unsigned char irq);
