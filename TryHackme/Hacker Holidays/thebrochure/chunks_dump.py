
import struct
with open('thebrochure.png','rb') as f:
    data = f.read()
pos = 8
while pos < len(data):
    length = struct.unpack('>I', data[pos:pos+4])[0]
    ctype = data[pos+4:pos+8].decode('ascii', 'replace')
    print(ctype, length)
    pos += 8 + length + 4
