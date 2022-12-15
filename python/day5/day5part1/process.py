import csv

def is_subset(outer, inner):
    # a <= b <= B <= A
    return outer[0] <= inner[0] <= inner[-1] <= outer[-1]

def is_overlap(left,right):
    return is_subset(left,right) or is_subset(right,left)

def process_data(assignments):
    # Running sum of all lists that are totally contained
    eclipse_count = 0
    for assignment in assignments:
        eclipse_count += is_overlap(assignment[0],assignment[1])

    return eclipse_count

"""
def takes4(a,b,c,d):
    print(a,b,c,d)

l = [1,2,3,4]

d = {"b":1, "c":2, "a":3, "d":4}

takes4(l[0],l[1],l[2],l[3])

takes4(*l)  # takes4(l[0],l[1],l[2],l[3])
takes4(**d) # takes4(a=3,b=1,c=2,d=4)
"""