#import packages
import os
import pathlib
import sys
import string

# Utility Functions
# For part two, we need to read the rucksacks in the same way as last time, except we don't need to split them into compartments. This time, while keeping each one intact.
def parse_input(fileName: str = ""):
    if fileName.isspace():
        fileName = os.path.join(
            pathlib.Path(__file__).parent.absolute(),
            'puzzle.input',
        )

    # This is probably inelegant but we essentially need to read the file line by line, stripping off those pesky '\n' and then define two empty lists: One to contain our list of rucksacks per group and another temporary list to facilitate the creation of the aphorementioned list. We initiate a for loop considering each sack in our master list, addign each one to a temporary list and increasing our loop counter. When the counter reaches 3, we'll append the list of three sacks to the elf_groups list and reset our temp list and the counter, starting the loop over again.
    with open(file=fileName, mode='r') as fin:
        sacks = [line.rstrip() for line in fin]
        elf_groups=[]
        Rucksacks = []
        RuckSackCount = 0
        for sack in sacks:
            Rucksacks.append(sack)
            RuckSackCount += 1
            if RuckSackCount == 3:
                elf_groups.append(Rucksacks)
                Rucksacks = []
                RuckSackCount = 0
    print(f"There were {len(sacks)} elves with rucksacks")
    return elf_groups

def process_data(elf_groups):
    # Similarly to part 1, we'll take the contents of each rucksack, examine each item in the first rucksack and search the second compartment for that same item if we find a matching item we'll then search the third rucksack for that same item. If that item is found in the third sack, append the item to groupmatch.
    groupmatch = []
    for sack in elf_groups:
        for letter in sack[0]:
            if letter in sack[1] and letter in sack[2]:
                groupmatch.append(letter)
                break

    return groupmatch


def match_item(groupmatch):
    # Now that we have a list of matching items per group, we'll quickly create a dictionary that containing all ascii letters and assigns the appropriate priority. We'll then go item by item through the list of matches and append the priorities to a new list. Once the list is complete, we'll sum it, returning the final_sum.
    item_priority_nums = []
    itemcount = 0
    d = dict(zip(string.ascii_letters, range(1, 53)))
    for item in groupmatch:
        item_priority_nums.append(d[groupmatch[itemcount]])
        itemcount += 1

    final_sum = sum(item_priority_nums)
    return final_sum


def display_output(output):
    print(f" There were {len(elf_groups)} elf groups")
    print(f"The final sum is {output}")
    return

# Main function:
if __name__ == "__main__":
    # Read input
    fileName = sys.argv[1]
    elf_groups = parse_input(fileName)

    # Process Data
    groupmatch = process_data(elf_groups)

    output = match_item(groupmatch)

    # Report
    display_output(output)