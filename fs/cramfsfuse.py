#!/usr/bin/python
from fuse import FUSE, Operations

import cramfs

class CramFSFuse(Operations):
    def __init__(self, filename):
        self.fs = file(filename, "r")


    def getattr(self, path, fh=None):
        inode = cramfs.get_inode(path, self.fs)
        return dict(st_mode = inode.mode, st_uid = inode.uid, st_gid = inode.gid)


if __name__ == '__main__':
    fuse = FUSE(CramFSFuse("fs.cramfs"), 'mount', foreground=True)


