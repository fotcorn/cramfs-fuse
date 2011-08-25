from binascii import hexlify,unhexlify
import os, sys
from stat import *

mode = "41ED"
mode = int(mode, 16)

print S_ISREG(mode)

print hex(os.stat("test").st_mode)
