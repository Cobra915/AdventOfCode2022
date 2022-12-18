def display_output(output):

    display = ""

    for column in range(1, len(output)):
        display = display + output[column][-1]

    print(display)
    return