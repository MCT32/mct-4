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
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 0000 nz nc NOP
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 0000 nz  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 0000  z nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 0000  z  c
    CO|MI,  RO|II|CE,   IO|AI,  0,      0,      0, 0, 0, # 0001 nz nc LDI
    CO|MI,  RO|II|CE,   IO|AI,  0,      0,      0, 0, 0, # 0001 nz  c
    CO|MI,  RO|II|CE,   IO|AI,  0,      0,      0, 0, 0, # 0001  z nc
    CO|MI,  RO|II|CE,   IO|AI,  0,      0,      0, 0, 0, # 0001  z  c
    CO|MI,  RO|II|CE,   IO|MI,  RO|AI,  0,      0, 0, 0, # 0010 nz nc LDA
    CO|MI,  RO|II|CE,   IO|MI,  RO|AI,  0,      0, 0, 0, # 0010 nz  c
    CO|MI,  RO|II|CE,   IO|MI,  RO|AI,  0,      0, 0, 0, # 0010  z nc
    CO|MI,  RO|II|CE,   IO|MI,  RO|AI,  0,      0, 0, 0, # 0010  z  c
    CO|MI,  RO|II|CE,   IO|MI,  AO|RI,  0,      0, 0, 0, # 0011 nz nc STA
    CO|MI,  RO|II|CE,   IO|MI,  AO|RI,  0,      0, 0, 0, # 0011 nz  c
    CO|MI,  RO|II|CE,   IO|MI,  AO|RI,  0,      0, 0, 0, # 0011  z nc
    CO|MI,  RO|II|CE,   IO|MI,  AO|RI,  0,      0, 0, 0, # 0011  z  c
    CO|MI,  RO|II|CE,   AO|BI,  0,      0,      0, 0, 0, # 0100 nz nc TAB
    CO|MI,  RO|II|CE,   AO|BI,  0,      0,      0, 0, 0, # 0100 nz  c
    CO|MI,  RO|II|CE,   AO|BI,  0,      0,      0, 0, 0, # 0100  z nc
    CO|MI,  RO|II|CE,   AO|BI,  0,      0,      0, 0, 0, # 0100  z  c
    CO|MI,  RO|II|CE,   SO|AI,  0,      0,      0, 0, 0, # 0101 nz nc ADD
    CO|MI,  RO|II|CE,   SO|AI,  0,      0,      0, 0, 0, # 0101 nz  c
    CO|MI,  RO|II|CE,   SO|AI,  0,      0,      0, 0, 0, # 0101  z nc
    CO|MI,  RO|II|CE,   SO|AI,  0,      0,      0, 0, 0, # 0101  z  c
    CO|MI,  RO|II|CE,   SO|AI|AS, 0,    0,      0, 0, 0, # 0110 nz nc SUB
    CO|MI,  RO|II|CE,   SO|AI|AS, 0,    0,      0, 0, 0, # 0110 nz  c
    CO|MI,  RO|II|CE,   SO|AI|AS, 0,    0,      0, 0, 0, # 0110  z nc
    CO|MI,  RO|II|CE,   SO|AI|AS, 0,    0,      0, 0, 0, # 0110  z  c
    CO|MI,  RO|II|CE,   AO|OI,  0,      0,      0, 0, 0, # 0111 nz nc OUT
    CO|MI,  RO|II|CE,   AO|OI,  0,      0,      0, 0, 0, # 0111 nz  c
    CO|MI,  RO|II|CE,   AO|OI,  0,      0,      0, 0, 0, # 0111  z nc
    CO|MI,  RO|II|CE,   AO|OI,  0,      0,      0, 0, 0, # 0111  z  c
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1000 nz nc JMP
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1000 nz  c
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1000  z nc
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1000  z  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1001 nz nc JZ
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1001 nz  c
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1001  z nc
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1001  z  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1010 nz nc JC
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1010 nz  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1010  z nc
    CO|MI,  RO|II|CE,   IO|CI,  0,      0,      0, 0, 0, # 1010  z  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1011 nz nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1011 nz  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1011  z nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1011  z  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1100 nz nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1100 nz  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1100  z nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1100  z  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1101 nz nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1101 nz  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1101  z nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1101  z  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1110 nz nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1110 nz  c
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1110  z nc
    CO|MI,  RO|II|CE,   0,      0,      0,      0, 0, 0, # 1110  z  c
    CO|MI,  RO|II|CE,   HLT,    0,      0,      0, 0, 0, # 1111 nz nc HLT
    CO|MI,  RO|II|CE,   HLT,    0,      0,      0, 0, 0, # 1111 nz  c
    CO|MI,  RO|II|CE,   HLT,    0,      0,      0, 0, 0, # 1111  z nc
    CO|MI,  RO|II|CE,   HLT,    0,      0,      0, 0, 0, # 1111  z  c
]

file = open('microcode.bin', 'wb')

for i in code:
    file.write(i.to_bytes(2, 'big'))

file.close