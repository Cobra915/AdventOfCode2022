import re
from collections import Counter

def isUniqueChars(focus):

    # Counting frequency
    freq = Counter(focus)

    if len(freq) == len(focus):
        return True
    else:
        return False

def process_data(message):

    letter_count = 4
    min = 0
    for letter in range(3, len(message)):
        focus = message[min:letter_count]
        if isUniqueChars(focus) == True:
            stx_index = focus
            stx_marker_point = letter_count
            print(f"The start-of-packet index is {stx_index}")
            break
       
        letter_count += 1
        min += 1

    return stx_marker_point

