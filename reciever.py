import socket, pickle
import sys
import bitarray


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
        print(unpickeled)


if __name__ == "__main__":
  main()

