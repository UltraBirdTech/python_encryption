def hex_dump(data):
    print('===================')
    for v in data:
        value = '0x%x' % v
        print(value)
    print( '' )

target = '01234567'.upper()
key = 'GuessKey'
hex_dump(map(ord, target))

def xor(K,C):
    P = []
    for i in range(len(C)):
        v = C[i]^K[i % len(K)]
        P.append( v )
    return P

enc = xor( map(ord, key), map(ord, target) )
hex_dump(enc)

calc_key = xor( enc, map(ord, target) )

target='##### FLAG{CTF_FINDPLANETEXT} ####'.upper()
print(target)

enc = xor( map(ord, key), map(ord, target) )
hex_dump(enc)

enc = xor(calc_key ,enc )
for v in calc_key:
    print(chr(v))

