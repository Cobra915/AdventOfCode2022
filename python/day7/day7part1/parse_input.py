import pathlib
import os


# Utility Functions
def parse_input(fileName: str = ""):
        if fileName.isspace():
            fileName = os.path.join(
                pathlib.Path(__file__).parent.absolute(),
                'puzzle.input',
            )

        with open(file=fileName, mode='r') as fin:
            inputs = [line.rstrip() for line in fin]
            return inputs

def process_commands(inputs):

    commands = []
    
    for line in inputs:
        
        if '$' in line == True:
            temp_dict = {"Command" : line.split("$")[1].strip(), "Output" : []}
            
            commands.append(temp_dict)
            continue

        if '$' in line == False:

            commands[-1]['Output'].append(line)
            continue

    return commands

        
