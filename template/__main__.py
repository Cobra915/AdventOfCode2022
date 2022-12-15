# Main function:
if __name__ == "__main__":

    import sys
    import parse_input as extract
    # from .process import process_data
    import process as transform
    import display_output as load

    # Read input
    fileName = sys.argv[1]
    data = extract.parse_input(fileName)

    # Process Data
    output = transform.process_data(data)

    # Report
    load.display_output(output)


