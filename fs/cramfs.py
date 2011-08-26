from struct import unpack
from binascii import hexlify,unhexlify
import zlib

CRAMFS_SUPERBLOCK = "IIII16s16s16s"
CRAMFS_INODE =      "HH3sBI"

class Inode:
    name = ""
    uid  = 0
    gid = 0
    orginalsize = 0
    mode = 0
    namelen = 0
    offset = 0
    def __str__(self):
        return self.__dict__.__str__()

def __inode_parse(offset, filesystem):
    filesystem.seek(offset)
    inode = filesystem.read(12)
    inode = unpack(CRAMFS_INODE, inode)

    # mode & uid
    inodedata = Inode()
    inodedata.mode = inode[0]
    inodedata.uid = inode[1]
    
    # size & gid
    inodedata.orginalsize = int(hexlify(inode[2][::-1]), 16)
    inodedata.gid =  inode[3]
    
    # namelen & offset
    namelenoffset = inode[4]
    inodedata.namelen = namelenoffset & 0x3F       # first 6 bits
    inodedata.offset =  (namelenoffset >> 6) * 4 # last 26 bits

    # name
    if inodedata.name != 0:
        inodedata.name = filesystem.read(inodedata.namelen * 4).replace("\x00", "")
    return inodedata

def __uncompress_block(offset, filesystem):
    fs.seek(offset)
    endofblock = unpack("I", fs.read(4))[0] # read block pointer
    data = fs.read(endofblock - offset - 4)
    return zlib.decompress(data)

def __readdir(offset, size, filesystem):
    # returns {'file1.txt' : <obj class Inode>, 'file2.txt' : <obj class Inode>}
    pass

def get_inode(path, filesystem):
    inode = inode_parse(64, filesystem)

    subdirs = path[1:].split("/")[:-1]
    for i in range(len(subdirs)):
        inode = readdir(inode.offset, inode.size, filesystem)[subdirs[i]]
    return inode

def readdir(path, filesystem):
    inode = get_inode(path, filesystem)
    return __readdir(inode.offset, inode.size)

fs = file("fs.cramfs", "r")

get_inode("/file1/folder/test/file.txt",fs)#.__dict__
#print get_inode("/file2.txt",fs)#.__dict__

"""
superblock = fs.read(64)
superblock = unpack(CRAMFS_SUPERBLOCK, superblock)

print inode_parse(64, fs)
print inode_parse(76, fs)
print inode_parse(100, fs)

print uncompress_block(124, fs)
print uncompress_block(148, fs)"""



