#import packages
import os
import pathlib
import sys
import string

# Utility Functions
def parse_input(fileName: str = ""):
    if fileName.isspace():
        fileName = os.path.join(
            pathlib.Path(__file__).parent.absolute(),
            'puzzle.input',
        )

    # Parse data from file, reading line by line and trimming all '\n' that may have been brought in from the txt file.
    with open(file=fileName, mode='r') as fin:
        sacks = [line.rstrip() for line in fin]
        RuckSackCount = 0

        Rucksacks = []
        Rucksacks_Cmp_List = []
        for sack in sacks:
            Compartments = [sack[:len(sack)//2], sack[len(sack)//2:]]
            Rucksacks_Cmp_List.append(Compartments)
            RuckSackCount += 1

    return Rucksacks_Cmp_List

def process_data(Rucksacks_Cmp_List):
    # Take the contents of each rucksack, examine each item in the first compartment and search the second compartment for that item. If that item is found, append the item to itemmatch
    itemmatches = []
    for sack in Rucksacks_Cmp_List:
        for letter in sack[0]:
            if letter in sack[1]:
                itemmatches.append(letter)
                break

    return itemmatches


def match_item(itemmatches):
    # Now that we have a list of matching items per rucksack, we'll quickly create a dictionary that assigns the appropriate priority. We'll then go item by item through the list of matches and append the numbers to a new list and then sum it, returning the final_sum.
    item_priority_nums = []
    itemcount = 0
    d = dict(zip(string.ascii_letters, range(1, 53)))
    for item in itemmatches:
        item_priority_nums.append(d[itemmatches[itemcount]])
        itemcount += 1

    final_sum = sum(item_priority_nums)
    return final_sum


def display_output(output):
    print(f"the final sum is {output}")
    return

# Main function:
if __name__ == "__main__":
    # Read input
    fileName = sys.argv[1]
    Rucksacks_Cmp_List = parse_input(fileName)

    # Process Data
    itemmatches = process_data(Rucksacks_Cmp_List)

    output = match_item(itemmatches)

    # Report
    display_output(output)