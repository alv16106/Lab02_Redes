from bitarray import bitarray
import numpy as np
import math


def strip_hamming(msg):
    """ This gets rid of all added bits """
    h = []
    for i in range(4):
        h.append(2 ** i - 1)
    m = np.delete(msg, h)
    return bitarray(m.tolist())


def get_matching_row(matrix, row):
    """Searches for a row in the parity-check matrix and returns its index.
        Returns -1 if not found."""
    print(row)
    try:
        return np.where(np.all(matrix == row, axis=1))[0][0]
    except IndexError:
        return -1


def encoding_matrix(r, n):
    """ r is the number of parity bits needed
    n is just total number of bits our message will have (n+r) """

    genmatrix = np.zeros((n - r, n), dtype=np.uint)

    # 2 sets, p for parity and d for original message
    p_positions = set([2 ** i - 1 for i in range(r)])
    d_positions = set(range(n)) - p_positions

    """ For each parity bit, determine its value
    (More like what goes in the multiplication matrix to get its value) """
    for p_item in p_positions:
        for d_index, d_item in enumerate(d_positions):
            if (p_item + 1) & (d_item + 1) != 0:
                genmatrix[d_index][p_item] = 1

    # fills in data bit columns of the generator matrix
    for d_index, d_item in enumerate(d_positions):
        genmatrix[d_index][d_item] = 1

    return genmatrix


def decoding_matrix(r, n):
    """ r is the number of parity bits recieved
    n is just total number of bits our message has """

    p_positions = set([2 ** i - 1 for i in range(r)])
    d_positions = set(range(n)) - p_positions

    checkmatrix = np.zeros((n, r), dtype=np.uint)

    for d_item in d_positions:
        for index in range(r):
            checkmatrix[d_item, index] = int(((d_item + 1) >> index) & 1)

    for p_index, p_item in enumerate(p_positions):
        checkmatrix[p_item][p_index] = 1

    return checkmatrix


def encode(msg):
    """ msg is the bitarray encoded message to encode """
    r = math.ceil(math.log2(len(msg))) + 1
    print(r)
    matrix = encoding_matrix(r, r + len(msg))
    return np.dot(msg.tolist(), matrix) % 2


def decode(msg):
    """ msg is the bitarray encoded message to decode """
    r = math.ceil(math.log2(len(msg)))
    matrix = decoding_matrix(r, len(msg))

    # Check parity lists
    result = get_matching_row(matrix, np.dot(msg.tolist(), matrix) % 2)
    if result != -1:
        # This means message is corrupted, try to fix
        msg[result] = (msg[result] + 1) % 2
        return strip_hamming(msg)
    else:
        return strip_hamming(msg)
