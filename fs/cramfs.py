from struct import unpack
from binascii import hexlify,unhexlify
import zlib

CRAMFS_SUPERBLOCK = "IIII16s16s16s"
CRAMFS_INODE =      "HH3sBI"

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

def __parse_inode(offset, filesystem):
    filesystem.seek(offset)
    inode = filesystem.read(12)
    inode = unpack(CRAMFS_INODE, inode)

    # mode & uid
    inodedata = Inode()
    inodedata.mode = inode[0]
    inodedata.uid = inode[1]
    
    # size & gid
    inodedata.size = int(hexlify(inode[2][::-1]), 16)
    inodedata.gid =  inode[3]
    
    # namelen & offset
    namelenoffset = inode[4]
    inodedata.namelen = (namelenoffset & 0x3F) * 4       # first 6 bits
    inodedata.offset =  (namelenoffset >> 6) * 4 # last 26 bits

    # name
    if inodedata.name != 0:
        inodedata.name = filesystem.read(inodedata.namelen).replace("\x00", "")
    return inodedata

def __uncompress_block(offset, filesystem):
    filesystem.seek(offset)
    endofblock = unpack("I", filesystem.read(4))[0] # read block pointer

    # blocksize = endofblock - offset - blockheader(4 bytes)
    data = filesystem.read(endofblock - offset - 4)
    return zlib.decompress(data)

def __readdir(offset, size, filesystem):
    # returns {'file1.txt' : <obj class Inode>, 'file2.txt' : <obj class Inode>}
    end = offset + size
    ret = dict()
    if size == 0:
        return ret
    while True:
        inode = __parse_inode(offset, filesystem)
        ret[inode.name] = inode
        offset = offset + 12 + inode.namelen
        if offset == end:
            break
    return ret

def get_inode(path, filesystem):
    inode = __parse_inode(64, filesystem)
    if path == "/":
        return inode
    pathparts = path[1:].split("/")
    
    for i in range(len(pathparts)):
        try:
            inode = __readdir(inode.offset, inode.size, filesystem)[pathparts[i]]
        except KeyError:
            return None
    return inode

def readdir(path, filesystem):
    inode = get_inode(path, filesystem)
    return __readdir(inode.offset, inode.size, filesystem)

def read(path, fileoffset, size, filesystem):
    inode = get_inode(path, filesystem)
    block = __uncompress_block(inode.offset, filesystem)
    return block[fileoffset:fileoffset + size]

#fs = file("fs.cramfs", "r")
#print read("/test/file1.txt", 0, 10, fs)
#print readdir("/test", fs)

#rootinode = __parse_inode(64, fs)
#print __readdir(rootinode.offset, rootinode.size, fs)
#get_inode("/file1/folder/test/file.txt",fs)#.__dict__

"""
superblock = fs.read(64)
superblock = unpack(CRAMFS_SUPERBLOCK, superblock)

print inode_parse(64, fs)
print inode_parse(76, fs)
print inode_parse(100, fs)

print uncompress_block(124, fs)
print uncompress_block(148, fs)"""



