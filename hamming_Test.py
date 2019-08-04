import csv
from hamming import encode, decode
from error_simulation import to_bitarray, hamming_message
from utils import to_int, to_string, get_params

if __name__ == "__main__":
    row = [
        'original_msg',
        'result_msg',
        'repaired',
        'correct'
    ]
    rows = []
    for i in range(0, 999):
        m = 'dsadAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaBBBBBBBBBBBBBBBBBBBb'
        # Add error
        result_msg, original_msg, real_msg = hamming_message(m)

        if to_string(real_msg) == to_string(result_msg):
            correct = True
        else:
            correct = False
        # Make row
        rows.append([
            to_string(original_msg),
            to_string(result_msg),
            False if decode(result_msg) != original_msg else True,
            correct
        ])

    with open('hamming.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(rows)

    writeFile.close()
