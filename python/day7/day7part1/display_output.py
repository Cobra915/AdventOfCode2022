import pprint
import json

def display_output(File_Tree, Mem_For_Delete):

    # with open('convert.txt', 'w') as convert_file:
    #    for key, nested in sorted(File_Tree.items()):
    #        print(key, file=convert_file)
    #        for subkey, value in sorted(nested.items()):
    #            print('   {}: {}'.format(subkey, value), file=convert_file)
    #        print(file=convert_file)
    

    # print(f"The filesystem was written to {convert_file}")
    
    print(f"Total Memory to be deleted: {Mem_For_Delete}")

    return