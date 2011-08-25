from binascii import hexlify,unhexlify
from struct import unpack

CRAMFS_SUPERBLOCK = "IIII16s16s16s"
CRAMFS_INODE =      "HH3sBI"

def inode_print(inode):
    print "mode: " + str(inode[0])
    print "uid: " + str(inode[1])
    print "size: " + str(inode[2])
    print "gid: " + str(inode[3])
    print "namelen/offset: " + str(inode[4])
    print "------------------------------------------------------"
    
#C0040000

fs = file("fs.cramfs")


superblock = fs.read(64)
superblock = unpack(CRAMFS_SUPERBLOCK, superblock)

rootinode = fs.read(12)
rootinode = unpack(CRAMFS_INODE, rootinode)

for i in range(0,2):
    inode = fs.read(12)
    inode = unpack(CRAMFS_INODE, inode)
    inode_print(inode)






