#import packages
import os
import pathlib
import sys

# Utility Functions
def parse_input(fileName: str = ""):
    if fileName.isspace():
        fileName = os.path.join(
            pathlib.Path(__file__).parent.absolute(),
            'puzzle.input',
        )

    # Parse data from file
    with open(file=fileName, mode='r') as fin:
        data = fin.read()

    # Now that we have the data we output that data
    return data

def process_data(data):
    # Process
    output = data

    return output

def display_output(output):
    
    return


# Main function:
if __name__ == "__main__":
    # Read input
    fileName = sys.argv[1]
    data = parse_input(fileName)

    # Process Data
    output = process_data(data)

    # Report
    display_output(output)

