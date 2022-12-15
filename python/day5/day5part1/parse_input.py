import pathlib
import os
import csv

# Utility Functions
def parse_input(fileName: str = ""):
    """
    TODO
    """
    if fileName.isspace():
        fileName = os.path.join(
            pathlib.Path(__file__).parent.absolute(),
            'puzzle.input',
        )

    data = []
    with open(file=fileName, mode='r') as fin:
        # TODO
        pass

    
    return data