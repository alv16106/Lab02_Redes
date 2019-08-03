from bitarray import bitarray
import random

from error_identifier import fletcher_checksum

ERROR_RATE = 0.01


def to_bitarray(bitarray_msg, with_error=True):
    list = bitarray_msg.tolist()
    error_list = [0] * len(list)
    alters = 0

    if with_error:
        for i in range(0, len(list)):
            if random.randint(0, 99) < ERROR_RATE * 100:
                error_list[i] = not list[i]
                alters += 1
            else:
                error_list[i] = list[i]
    else:
        error_list = list

    print("Porcentaje de errores: ", alters/len(list))

    err_bitarray = bitarray()
    err_bitarray.extend(error_list)

    list_bitarray = bitarray()
    list_bitarray.extend(list)

    return err_bitarray, list_bitarray


def message(msg, with_error=True):
    bitarray_msg = bitarray()
    original_msg = bitarray_msg
    bitarray_msg.frombytes(msg.encode('unicode_escape'))

    c1, c2 = fletcher_checksum(bitarray_msg.tolist())

    bitarray_msg.extend(c1)
    bitarray_msg.extend(c2)

    result_msg, real_msg = to_bitarray(bitarray_msg, with_error)

    return result_msg, original_msg, real_msg
