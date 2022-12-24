# Main function:
if __name__ == "__main__":

    import sys
    import parse_input as extract
    # from .process import process_data
    import process as transform
    import display_output as load
    import re
    from collections import Counter

    # Read input
    fileName = sys.argv[1]
    data = extract.parse_input(fileName)

    # Process Data
    output1 = transform.process_data(data)[0]
    output2 = transform.process_data(data)[1]
    output3 = transform.process_data(data)[2]
    output4 = transform.process_data(data)[3]

    # Report
    load.display_output(output1, output2, output3, output4)


