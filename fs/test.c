#include <stdio.h>
#include <stdlib.h>

struct cramfs_inode {
	unsigned int namelen:6;
	unsigned int offset:26;
};


int main()
{

    //unsigned int val = 0x830A0000;
    struct cramfs_inode *inode = malloc(4);
    inode->namelen = 3;
    inode->offset = 40;
    printf("%i\n", inode->namelen);
    printf("%i\n", inode->offset);
    printf("%i\n", *(unsigned int*)inode);
    printf("%u\n", inode->namelen);
    printf("%u\n", inode->offset);
    printf("%u\n", *(unsigned int*)inode);
    /*struct cramfs_inode *cramfs = malloc(sizeof(struct cramfs_inode));
    cramfs->namelen = 3;
    
    char* data = (char *)cramfs;

    printf("%X", data[1]);*/

}
