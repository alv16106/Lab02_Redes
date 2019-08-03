from bitarray import bitarray

MOD_BITARRAY = bitarray()
MOD_BITARRAY.extend([True] * 8)


def get_params(list):
    new_list = list.tolist()
    new_c2 = new_list[len(new_list) - MOD_BITARRAY.length():]

    new_list = new_list[:len(new_list) - MOD_BITARRAY.length()]
    new_c1 = new_list[len(new_list) - MOD_BITARRAY.length():]

    new_list = new_list[:len(new_list) - MOD_BITARRAY.length()]
    new_msg = new_list

    list = bitarray()
    list.extend(new_msg)

    c1 = bitarray()
    c1.extend(new_c1)

    c2 = bitarray()
    c2.extend(new_c2)

    return list, c1, c2


def to_string(list):
    msg = list.tobytes().decode('unicode_escape')
    return msg


def to_int(list):
    return int(list.to01(), 2)


def from_int_to_bitarray(i, size):
    array = [False] * size
    b = bitfield(i, size)

    for x in range(0, len(b)):
        array[x] = True if b[x] == 1 else False

    list = bitarray(0)
    list.extend(array)

    return list


def bitfield(n, size):

    b = [int(digit) for digit in bin(n)[2:]]  # [2:] to chop off the "0b" part 

    for c in range(0, size - len(b)):
        b.insert(0, 0)
    return b
