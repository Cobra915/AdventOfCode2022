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
            

    # Now that we have the data we output that data
    print(f"We read {LineCount} lines from {fileName} containing {EntryCount} entries from {len(elves)} elves")
    return elves

def process_data(data):
    # Process
    output = []
    for elf in data:
        # Begin running sum with 0 initial value
        elf_total = 0
        # For each entry in the elfs bag
        for entry in elf:
            # Add the entry to the running sum
            elf_total += entry
        # After completing running sum, add that elf's total as an entry to our output
        output.append(elf_total)
    output = sorted(output, reverse=True)

    return output[0]

def display_output(output):
    print(f"The elf carrying the most calories is carrying {output} calories")
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

