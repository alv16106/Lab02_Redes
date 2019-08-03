import socket
import bitarray
import pickle


def main():
    info = bitarray.bitarray('1001101')
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
