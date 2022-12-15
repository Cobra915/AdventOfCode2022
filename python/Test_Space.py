import os
import pathlib
import sys
import csv
import string

feed = [['2-4', '6-8'], ['2-3', '4-5'], ['5-7', '7-9'], ['2-8', '3-7'], ['6-6', '4-6'], ['2-6', '4-8']]

        
def process_data(feed):
    items = []
    assignments = []
    for assignment in assignments:
        print(f"assignment: {assignment}")
        for item in assignment:
            print(f"item: {item}")
            print(f"Item Type: {type(item)}")
            newitem = item.split("-")
            items.append(newitem)
            assignments.append(items)
    print(assignments)
    return assignments


def display_output(output):
    print(assignments)
    return

# Main function:
if __name__ == "__main__":
    # Read input

    # Process Data
    output = process_data(assignments)

    # Report
    display_output(output)
