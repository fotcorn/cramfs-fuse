from struct import unpack
from binascii import hexlify,unhexlify
import zlib

CRAMFS_SUPERBLOCK = "IIII16s16s16s"
CRAMFS_INODE =      "HH3sBI"
BLOCKSIZE = 4096

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
    inodedata.namelen = (namelenoffset & 0x3F) * 4 # first 6 bits
    inodedata.offset =  (namelenoffset >> 6) * 4   # last 26 bits

    # name
    if inodedata.name != 0:
        inodedata.name = filesystem.read(inodedata.namelen).replace("\x00", "")
    return inodedata

def __uncompress_file(offset, orginalsize, filesystem):
    # read block headers
    nblocks = (orginalsize - 1) / BLOCKSIZE + 1
    filesystem.seek(offset) # seek to block headers
    
    startofblock = offset + nblocks * 4 # start of first block after block headers
    blocks = list() # [ blocksize1, blocksize2, ...]
    for i in range(nblocks):
        endofblock = unpack("I", filesystem.read(4))[0]
        blocks.append(endofblock - startofblock)
        startofblock = endofblock

    ret = ""
    for blocksize in blocks:
        data = filesystem.read(blocksize)
        ret = ret + zlib.decompress(data)
    return ret

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
    filedata = __uncompress_file(inode.offset, inode.size, filesystem)
    return filedata[fileoffset:fileoffset + size]




