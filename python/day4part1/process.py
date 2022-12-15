from typing import List

def is_subset(outer, inner):
    # a <= b <= A or b <= A <= B
    return outer[0] <= inner[0] <= inner[-1] <= outer[-1]

def is_intersect(left: List[int], right: List[int]):
    return left[0] <= right[0] <= left[1] or left[0] <= right[1] <= left[1]
    
def is_overlap(left: List[int], right: List[int]):
    return is_subset(left,right) or is_subset(right,left)

def does_intersect(left: List[int], right: List[int]):
    return is_intersect(left,right) or is_intersect(right,left)

def process_data(assignments: List[List[List[int]]]) -> int:
    # Running sum of all lists that are totally contained
    eclipse_count: int = 0
    assignment: List[List[int]]
    for assignment in assignments:
        eclipse_count += does_intersect(assignment[0],assignment[1])

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