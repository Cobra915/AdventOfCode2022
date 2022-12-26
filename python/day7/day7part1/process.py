import build
import pprint

def find_small_directories(folder: dict):
    running_list = []
    # If small
    if folder["size"] < 100000:
        # add to running list
        running_list.append(folder["size"])
    # recurse
    for subfolder in folder["subfolders"].values():
       running_list += find_small_directories(subfolder)
    # done
    return running_list
    
def fibonacci_iterative(n: int) -> int:
    first: int = 0
    second: int = 1
    if n == 0:
        return first
    elif n == 1: 
        return second

    # iterate
    for _ in range(n-2):
        # F(n) = F(n-1) + F(n-2)
        next: int = first + second
        # leapfrog forward
        first = second
        second = next

    return next
    
def fibonacci_recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1: 
        return 1

    # recurse
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    