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
        Lines = fin.readlines()
        LineCount = 0
        EntryCount = 0
        # ElfCount = 0

        #start a list of elves' lists, so we have a list of each of their individual inventories
        elves = [[]]
        for line in Lines:
            LineCount += 1
            if line.isspace():
                elves.append([])
                # ElfCount += 1
            else:
                elves[-1].append(int(line))
                EntryCount += 1
        return elves
            


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
