from bitarray import bitarray
import random

ERROR_RATE = 0.5

def to_bitarray(msg, with_error=True):
    bitarray_msg = bitarray()
    bitarray_msg.frombytes(msg.encode('UTF-8'))
    
    list = bitarray_msg.tolist()
    error_list = [0] * len(list)

    for i in range(0, len(list)):
        if random.randint(0, 101) < ERROR_RATE * 10:
            error_list[i] = not list[i]
        else:
            error_list[i] = list[i]

    return error_list, list


def to_string(list):
    msg = bitarray(list).tobytes().decode('ascii')
    return msg

