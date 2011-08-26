from binascii import hexlify,unhexlify
from struct import unpack
import stat

CRAMFS_SUPERBLOCK = "IIII16s16s16s"
CRAMFS_INODE =      "HH3sB4s"

class Inode:
    name = ""
    uid  = 0
    gid = 0
    size = 0
    mode = 0
    namelen = 0
    offset = 0
    def __str__(self):
        return self.__dict__.__str__()
    


def inode_parse(offset, filesystem):
    filesystem.seek(offset)
    inode = filesystem.read(12)
    inode = unpack(CRAMFS_INODE, inode)

    inodedata = Inode()
    inodedata.uid = str(inode[1])
    inodedata.mode = inode[0]
    
    # reverse string, convert to hex, convert to int
    namelenoffset = int(hexlify(inode[4][::-1]), 16)
    inodedata.namelen = namelenoffset & 0x3F       # first 6 bits
    inodedata.offset =  namelenoffset >> 6 # last 26 bits
    if inodedata.name != 0:
        inodedata.name = filesystem.read(inodedata.namelen * 4).replace("\x00", "")
    
    #print "gid: " + str(inode[3])
    #print "size: " + str(inode[2])
    #print "namelen/offset: " + str(inode[4])
    return inodedata

fs = file("fs.cramfs", "r")


superblock = fs.read(64)
superblock = unpack(CRAMFS_SUPERBLOCK, superblock)

print inode_parse(64, fs)
print inode_parse(76, fs)
print inode_parse(148, fs)
