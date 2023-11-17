HLT = 0b0000000000000001
CI =  0b0000000000000010
CO =  0b0000000000000100
CE =  0b0000000000001000
II =  0b0000000000010000
IO =  0b0000000000100000
RI =  0b0000000001000000
RO =  0b0000000010000000
MI =  0b0000000100000000
AI =  0b0000001000000000
AO =  0b0000010000000000
BI =  0b0000100000000000
SO =  0b0001000000000000
AS =  0b0010000000000000
OI =  0b0100000000000000

code = [
    CO|MI,  RO|II|CE,   0,  0,  0, # 0000 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0000 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0000  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0000  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0001 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0001 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0001  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0001  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0010 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0010 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0010  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0010  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0011 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0011 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0011  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0011  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0100 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0100 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0100  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0100  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0101 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0101 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0101  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0101  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0110 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0110 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0110  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0110  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0111 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0111 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 0111  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 0111  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1000 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1000 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1000  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1000  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1001 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1001 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1001  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1001  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1010 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1010 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1010  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1010  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1011 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1011 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1011  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1011  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1100 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1100 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1100  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1100  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1101 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1101 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1101  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1101  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1110 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1110 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1110  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1110  c  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1111 nc nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1111 nc  z
    CO|MI,  RO|II|CE,   0,  0,  0, # 1111  c nz
    CO|MI,  RO|II|CE,   0,  0,  0, # 1111  c  z
]

file = open('microcode.bin', 'wb')

for i in code:
    file.write(i.to_bytes(2, 'big'))

file.close