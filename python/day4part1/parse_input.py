import pathlib
import os
import csv

fuck_you = "darron"

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
                # [mapping(each) for each in list]
                # [output for each in list]
                newitem = [int(each) for each in item.split("-")]
                items.append(newitem)
        
            assignments.append(items)

    return assignments