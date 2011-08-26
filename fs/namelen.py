
#namelen1 = "830A0000"
#namelen2 = "030C0000"

"000004C0

namelen1 = "00000A83"
namelen2 = "00000C03"

namelen1 = int(namelen1, 16)
namelen2 = int(namelen2, 16)


print namelen1 & 0x3F
print namelen2 & 0x3F

#class NamelenOffset(Structure):
#    _fields_ = [("namelen", c_int, 6),
#        ("offset", c_int, 26)]


