from bitarray import bitarray
from utils import MOD_BITARRAY, to_int, from_int_to_bitarray


def fletcher_checksum(block):
    c1 = 0
    c2 = 0
    for bite in block:
        c1 += bite
        c2 += c1

    c1 = c1 % to_int(MOD_BITARRAY)
    c2 = c2 % to_int(MOD_BITARRAY)

    c1_bitarray = from_int_to_bitarray(c1, MOD_BITARRAY.length())
    c2_bitarray = from_int_to_bitarray(c2, MOD_BITARRAY.length())

    return (c1_bitarray, c2_bitarray)
