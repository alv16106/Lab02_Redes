import socket
import bitarray
import pickle
import sys
from error_simulation import message, hamming_message
from utils import to_string, to_int, get_params


def main():
    algorithm = sys.argv[1]

    msg = input("Mensaje: ")
    # result_msg: the message with noise and with the 16bits of fletcher mods
    # original_msg: is the message with noise only (only for debugging)
    # real_msg: is the message without noise (only for debuggin)
    if (algorithm == 'hamming'):
        result_msg, original_msg, real_msg = hamming_message(msg)
    else:
        result_msg, original_msg, real_msg = message(msg)

    info = result_msg
    pickeld = pickle.dumps(info)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))
    sock.send(pickeld)
    # Receive up to 4096 bytes from a peer
    sock.recv(1024)
    # Close the socket connection, no more data transmission
    sock.close()


if __name__ == "__main__":
    main()
