#!/usr/bin/python
from fuse import FUSE, Operations, FuseOSError
from errno import ENOENT

import cramfs

class CramFSFuse(Operations):
    def __init__(self, filename):
        self.fs = file(filename, "r")

    def getattr(self, path, fh=None):
        inode = cramfs.get_inode(path, self.fs)
        if inode == None:
            raise FuseOSError(ENOENT)
        return dict(st_mode = inode.mode, st_uid = inode.uid, st_gid = inode.gid, st_size = inode.size)

    def readdir(self, path, fh):
        return cramfs.readdir(path, self.fs)

    def read(self, path, size, offset, fh):
        return cramfs.read(path, offset, size, self.fs)

if __name__ == '__main__':
    fuse = FUSE(CramFSFuse("fs.cramfs"), 'mount', foreground=True)


