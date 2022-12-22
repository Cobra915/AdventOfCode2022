import pathlib
import os
import csv

# Utility Functions
def parse_input(fileName: str = ""):
        if fileName.isspace():
            fileName = os.path.join(
                pathlib.Path(__file__).parent.absolute(),
                'puzzle.input',
            )

        with open(file=fileName, mode='r') as fin:
            message = fin.read()
            
            return message
