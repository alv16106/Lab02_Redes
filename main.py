from error_simulation import to_bitarray, to_string


if __name__ == "__main__":
    while True:
        message = input("Mensaje: ")
        # Do something
        list, error_list = to_bitarray(message)
        print(to_string(list))
