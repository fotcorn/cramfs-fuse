import zlib
from binascii import hexlify,unhexlify

text = "this is file1"

print hexlify(zlib.compress(text))
print "adler: " + hex(zlib.adler32(text))

#789c 2bc9c82c5600a2b4cc9c544300   220004a6
#78da2bc9c82c5600a2b4cc9c54432e0026b004b0
#78da2bc9c82c5600a2b4cc9c54232e0026b204b1


print zlib.decompress(unhexlify("78da2bc9c82c5600a2b4cc9c54232e0026b204b1"))
