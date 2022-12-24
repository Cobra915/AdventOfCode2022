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
            inputs = [line.strip() for line in fin]
            return inputs

def process_commands(inputs):

    commands = []

    for line in inputs:
        if '$' in line:
            commands.append({
                "Command": line.split("$")[1].strip(), 
                "Output" : [],
            })
        else:
            commands[-1]['Output'].append(line)

    return commands

        
