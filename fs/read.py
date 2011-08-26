"""

blocksize: 4096 bytes




"""


from struct import unpack
from binascii import hexlify,unhexlify
import zlib

CRAMFS_SUPERBLOCK = "IIII16s16s16s"
CRAMFS_INODE =      "HH3ssI"

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

    # mode & uid
    inodedata = Inode()
    inodedata.mode = inode[0]
    inodedata.uid = inode[1]
    
    # size & gid
    inodedata.size = int(hexlify(inode[2][::-1]), 16)
    #print inode[2]
    
    # namelen & offset
    namelenoffset = inode[4]
    inodedata.namelen = namelenoffset & 0x3F       # first 6 bits
    inodedata.offset =  (namelenoffset >> 6) * 4 # last 26 bits

    # name
    if inodedata.name != 0:
        inodedata.name = filesystem.read(inodedata.namelen * 4).replace("\x00", "")
    
    return inodedata

fs = file("fs.cramfs", "r")


superblock = fs.read(64)
superblock = unpack(CRAMFS_SUPERBLOCK, superblock)

print inode_parse(64, fs) # 108
print inode_parse(76, fs) # 24
print inode_parse(100, fs) # 24
print inode_parse(124, fs)
print inode_parse(148, fs)


fs.seek(184)
fs.read(4) # read block pointer
print zlib.decompress(fs.read(20))

fs.seek(208)
fs.read(4) # read block pointer
print zlib.decompress(fs.read(20))


