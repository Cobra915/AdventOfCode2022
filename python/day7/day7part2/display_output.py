def display_output(output1, output2, output3, output4):

    #stx_marker_point, stx_index, msg_marker_point, msg_index

    display1 = output1
    display2 = output2
    display3 = output3
    display4 = output4

    print(f"The start-of-packet index is: {display2}")
    print(f"The first start-of-packet marker comes after character {display1}")


    print(f"The start-of-message index is: {display4}")
    print(f"The first start-of-message marker comes after character {display3}")
    

    return