# Main function:
if __name__ == "__main__":

    import sys
    from parse_input import parse_input
    # from .process import process_data
    import process
    from display_output import *

    # Read input
    fileName = sys.argv[1]
    data = parse_input(fileName)

    # Process Data
    output = process.process_data(data)

    # Report
    display_output(output)


