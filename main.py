from error_simulation import to_bitarray, message
from utils import to_string, MOD_BITARRAY, from_int_to_bitarray, to_int, get_params

if __name__ == "__main__":
    while True:
        msg = input("Mensaje: ")
        # Do something
        result_msg, original_msg, real_msg = message(msg)

        m, c1, c2 = get_params(result_msg)

        print("C1: ", to_int(c1))
        print("C2: ", to_int(c2))
        print("MENSAJE: ", to_string(m))
