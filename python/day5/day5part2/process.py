import re

def process_data(instructions):

    matrix = [
        [],
        ['B', 'P', 'N', 'Q', 'H', 'D', 'R', 'T'],
        ['W', 'G', 'B', 'J', 'T', 'V'],
        ['N', 'R','H', 'D', 'S', 'V', 'M', 'Q'],
        ['P', 'Z', 'N', 'M', 'C',],
        ['D', 'Z', 'B',],
        ['V', 'C', 'W', 'Z'],
        ['G', 'Z', 'N', 'C', 'V', 'Q', 'L', 'S'],
        ['L', 'G', 'J', 'M', 'D', 'N', 'V'],
        ['T', 'P', 'M', 'F', 'Z', 'C', 'G']
    ]

    '''
    matrix = [
        [],
        ['Z', 'N'],
        ['M', 'C', 'D'],
        ['P']
	]

    '''

    linecount = 0

    pattern = "move (?P<x>\d+) from (?P<Source>\d+) to (?P<Destination>\d+)"
    for line in instructions:
        #print(line)
        linecount += 1
        match = re.match(pattern, line)
        x = int(match.group('x'))
        s = int(match.group('Source'))
        d = int(match.group('Destination'))
        focus = matrix[s][-x:]
        #print(f"Moving {focus} from {s} to {d}")
        del matrix[s][-x:]
        matrix[d] = matrix[d] + focus
        #print(linecount)
        #print(matrix[d])
        
        """
        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
        """

    return matrix

