import csv
from error_simulation import to_bitarray, message
from error_identifier import fletcher_checksum
from utils import to_int, to_string, get_params

if __name__ == "__main__":
    row = [
        'original_msg',
        'result_msg',
        'c1',
        'c2',
        'c1_n',
        'c2_n',
        'corrupted?',
        'correct'
    ]
    rows = []
    for i in range(0, 999):
        msg = 'AAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaBBBBBBBBBBBBBBBBBBBb'
        # Add error
        result_msg, original_msg, real_msg = message(msg)
        m, c1, c2 = get_params(result_msg)
        # Calculate new Cs
        c1_n, c2_n = fletcher_checksum(m)
        if to_string(original_msg) == to_string(result_msg):
            correct = True
        else:
            correct = False
        # Make row
        rows.append([
            to_string(original_msg),
            to_string(result_msg),
            to_int(c1),
            to_int(c2),
            to_int(c1_n),
            to_int(c2_n),
            False if (to_int(c1_n) != to_int(c1) and to_int(c2_n) != to_int(c2)) else True,
            correct
        ])
    
    with open('fletcher.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(rows)

    writeFile.close()
