import socket
import pickle
import sys
import bitarray

from utils import to_string, to_int, get_params
from error_identifier import fletcher_checksum


def main():
    HOST = sys.argv[1]
    PORT = sys.argv[2]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, int(PORT)))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                unpickeled = pickle.loads(data)

                # m: is the part of result_msg that its in fact a message
                # c1: is the part of result_msg that is the first mod
                # c2: is the part of result_msg that is the second mod
                m, c1, c2 = get_params(unpickeled)

                # c1_n: is the new c1, calculated for the message we recieve
                # c2_n: is the new c2, calculated for the message we recieve
                c1_n, c2_n = fletcher_checksum(m)

                print("C1: ", to_int(c1), to_int(c1_n))  # only for debugging
                print("C2: ", to_int(c2), to_int(c2_n))  # only for debugging
                
                # If they dont concide there is a corruption somewhere
                if (to_int(c1_n) != to_int(c1) and to_int(c2_n) != to_int(c2)):
                    print("ERROR, mensaje posiblemente corrupto")

                print("MENSAJE: ", to_string(m))  # prints message


if __name__ == "__main__":
    main()
