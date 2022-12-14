#import packages
import os
import pathlib
import sys
import csv

# Utility Functions
def parse_input(fileName: str = ""):
    """
    MSH code reviewed 12/14 10:14 PM
    """
    if fileName.isspace():
        fileName = os.path.join(
            pathlib.Path(__file__).parent.absolute(),
            'puzzle.input',
        )

    with open(file=fileName, mode='r') as fin:
        #Start reading the file line by line
        assignments = []
        csvFile = csv.reader(fin)
        for assignment in csvFile:
            items = []
            for item in assignment:
                newitem = item.split("-")
                items.append(newitem)
            assignments.append(items)

    return assignments

def process_data(assignments):
    
    output = assignments

    return output

def display_output(output):
    print(assignments)
    return

# Main function:
if __name__ == "__main__":
    # Read input
    fileName = sys.argv[1]
    assignments = parse_input(fileName)

    # Process Data
    output = process_data(assignments)

    # Report
    display_output(output)

