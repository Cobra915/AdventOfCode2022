# Main function:
if __name__ == "__main__":

    import sys
    import parse_input as extract
    # from .process import process_data
    import process as transform
    import display_output as load
    import re

    '''

        [T]     [Q]             [S]        
        [R]     [M]             [L] [V] [G]
        [D] [V] [V]             [Q] [N] [C]
        [H] [T] [S] [C]         [V] [D] [Z]
        [Q] [J] [D] [M]     [Z] [C] [M] [F]
        [N] [B] [H] [N] [B] [W] [N] [J] [M]
        [P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
        [B] [W] [N] [P] [D] [V] [G] [L] [T]
         1   2   3   4   5   6   7   8   9 

        move 5 from 4 to 9

     Code must be able to do the following:
        set starting matrix, list of lists
        for every in instructions
        parse instruction and identify components, "Move [x] from [source] to [destination]", use regex to extract x, s, and d from the fixed raw text
        where x = number of crates, s = source given minus 1 (for indexing) and d = destionation minus 1 for indexing

        index source list and get identities of crates to remove, focus = MATRIX[SOURCENUMBER][-x:]
        store those values as a temporary list, focus = Matrix[s][-x:]
        Remove those values from the end of source list, del matrix[s][-x:]
        append the values to the end of the destination list matrix[d] = matrix[d] + focus
        proceed to the next line and list of instructions

     '''

    # Read input
    fileName = sys.argv[1]
    data = extract.parse_input(fileName)

    # Process Data
    output = transform.process_data(data)

    # Report
    load.display_output(output)


