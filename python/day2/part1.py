#import packages
import os
import pathlib
import sys
import csv

# Utility Functions
def parse_input(fileName: str = ""):
    if fileName.isspace():
        fileName = os.path.join(
            pathlib.Path(__file__).parent.absolute(),
            'puzzle.input',
        )

    # Parse data from file. We need to read the file row by row, determining the opponent input and guide response and storing that as a variable
    with open(file=fileName, mode='r') as fin:
            #Start reading the file line by line
        rounds = []
        csvFile = csv.reader(fin, delimiter= " ")
        for round in csvFile:
            rounds.append(round)
    return rounds

def process_data(rounds):
    # Process data - this is where we will probably calculate the score per round
    outcome_point_map = {
        "AX" : 3,
        'AY' : 6,
        'AZ' : 0,
        'BX' : 0,
        'BY' : 3,
        'BZ' : 6,
        'CX' : 6,
        'CY' : 0,
        'CZ' : 3
    }
    
    shape_point_map = {
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    }
    
    roundcount = 0
    wincount = 0
    drawcount = 0
    losscount = 0

    for round in rounds:
        my_choices.append(rounds[roundcount][1])
        outcomes.append(rounds[roundcount][0] + rounds[roundcount][1])

        points_list.append(shape_point_map.get(my_choices[roundcount]) + outcome_point_map.get(outcomes[roundcount]))

        if outcome_point_map.get(outcomes[roundcount]) == 6:
            wincount += 1

        elif outcome_point_map.get(outcomes[roundcount]) == 3:
            drawcount += 1

        else:
            losscount += 1
    
        roundcount += 1

    total_points = sum(points_list)

    print(f"There were {roundcount} rounds of Rock/Paper/Scissors in total")
    print(f"You won {wincount} rounds")
    print(f"You tied {drawcount} rounds")
    print(f"You lost {losscount} rounds")

    return total_points

def display_output(total_points):
    print(f"your total points are {total_points}")
    return


# Main function:
if __name__ == "__main__":
    # Read input
    my_choices = []
    outcomes = []
    points_list = []
    fileName = sys.argv[1]
    rounds = parse_input(fileName)

    # Process Data
    output = process_data(rounds)

    # Report
    display_output(output)

