import zlib
from binascii import hexlify,unhexlify

text = "this is file1"

print hexlify(zlib.compress(text))

print zlib.adler32(text)
print zlib.decompress(unhexlify("789c2bc9c82c5600a2b4cc9c544300220004a6"))

print zlib.decompress(unhexlify("789c2bc9c82c5600a2b4cc9c544300220004a6"))


print unhexlify("d000000078da2bc9c82c5600a2b4")
# 2

# d000000078da2bc9c82c5600a2b4
# 789c        2bc9c82c5600a2b4cc9c5443 00220004a6
