import zlib

with open('thebrochure.png', 'rb') as f:
    data = f.read()

# crude IDAT extraction — concatenate all IDAT chunk payloads
import struct
pos = 8
idat = b''
while pos < len(data):
    length = struct.unpack('>I', data[pos:pos+4])[0]
    ctype = data[pos+4:pos+8]
    if ctype == b'IDAT':
        idat += data[pos+8:pos+8+length]
    pos += 8 + length + 4

d = zlib.decompressobj()
out = d.decompress(idat)
print("Decompressed size:", len(out))
print("Expected size (w*h*4 +h for filter bytes):", 726*934*4 + 934)
print("Unused/trailing compressed bytes:", len(d.unused_data))
if d.unused_data:
    print(d.unused_data[:200])
