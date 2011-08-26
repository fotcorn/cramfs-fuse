#!/usr/bin/python
from fuse import FUSE, Operations


class CramFSFuse(Operations):
    def __init__(self, filename):
        


if __name__ == '__main__':
    fuse = FUSE(CramFSFuse("fs.cramfs"), 'mount', foreground=True)


