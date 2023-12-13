import os

def decode_line(encoded_line):
    numb_list = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbs = ''
    i = 0
    while i < len(encoded_line):
        if encoded_line[i].isdigit():
            while i < len(encoded_line) and encoded_line[i].isdigit():
                numbs += encoded_line[i]
                i += 1
        else:
            alpha_start_indices = [0 for _ in range(len(encoded_line))]
            alpha_str = ''
            while i < len(encoded_line) and encoded_line[i].isalpha():
                alpha_str += encoded_line[i]
                i += 1
            for j in range(1, len(numb_list)):
                index = alpha_str.find(numb_list[j])
                while index != -1:
                    alpha_start_indices[index] = j
                    index = alpha_str.find(numb_list[j], index + 1)
            for integer in alpha_start_indices:
                if integer != 0:
                    numbs += str(integer)
    return numbs[0] + numbs[-1]
    
def get_calibration_value(calibration_document):
    calibration_value = 0

    with open(calibration_document, 'r') as file:
        for line in file:
            val = int(decode_line(line.strip()))
            calibration_value += val

    return calibration_value

# Tests

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

# print(decode_line('jcb82eightwond'))
print(get_calibration_value(puzzle_input))
