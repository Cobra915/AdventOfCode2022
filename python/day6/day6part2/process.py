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

    
    stx_letter_count = 4
    stx_min = 0

    for letter in range(3, len(message)):
        focus = message[stx_min:stx_letter_count]
        if isUniqueChars(focus) == True:
            stx_index = focus
            stx_marker_point = stx_letter_count
            break
            
       
        stx_letter_count += 1
        stx_min += 1
    
    msg_letter_count = stx_marker_point + 14
    msg_min = stx_marker_point

    for letter in range(stx_marker_point, len(message)):
        focus = message[msg_min:msg_letter_count]
        if isUniqueChars(focus) == True:
            msg_index = focus
            msg_marker_point = msg_letter_count
            break

        if len(focus) != 14:
            break

        msg_letter_count += 1
        msg_min += 1


    return stx_marker_point, stx_index, msg_marker_point, msg_index

