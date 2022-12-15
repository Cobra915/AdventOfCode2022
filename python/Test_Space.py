import string

Rucksacks_Cmp_List = [
    ['vJrwpWtwJgWr', 'hcsFMMfFFhFp'], 
    ['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'], 
    ['PmmdzqPrV', 'vPwwTWBwg'], 
    ['wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'], 
    ['ttgJtRGJ', 'QctTZtZT'], 
    ['CrZsJsPPZsGz', 'wwsLwLmpwMDw']
    ]


def process_data(Rucksacks_Cmp_List):
    # Process the contents of each rucksack and compare them character by character
    d = dict(zip(string.ascii_letters, range(1, 53)))
    itemmatch = []
    for sack in Rucksacks_Cmp_List:
#        for n in range(0, len(sack[0])):
#            # if Rucksacks_Cmp_List[sackcount][0][n] == Rucksacks_Cmp_List[sackcount][1][n]:
#            if sack[0][n] == sack[1][n]:
#                itemmatch.append(sack[0][n])
#                print(sack[0][n])
        for letter in sack[0]:
            if letter in sack[1]:
                itemmatch.append(letter)
                break
    
    priority_list = []
    for letter in itemmatch:
        priority_list.append(d.get(letter))

    final_sum = sum(priority_list)
    print(final_sum)

    return final_sum


    
                
#    print(itemmatch)
#    return itemmatch


# Process Data
itemmatch = process_data(Rucksacks_Cmp_List)