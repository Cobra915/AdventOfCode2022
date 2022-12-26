# Main function:
if __name__ == "__main__":

    import sys
    import parse_input as extract
    # from .process import process_data
    import process as transform
    import display_output as load
    import build as build

    # Read input
    fileName = sys.argv[1]
    file = extract.parse_input(fileName)
    data = extract.process_commands(file)
    # Process Data
    File_Tree = build.build_file_tree(data)

    #   if "--process-size" in sys.argv[1:]:
    #       result = transform.process_file_size(File_Tree)
    #   if "--process-location" in sys.argv[1:]:
    #       transform.process_absolute_path(File_Tree)
    #   if "--help" in sys.argv[1:]:
    #       print(
    #           "--process.size"
    #           "--process-location"
    #       )
    R_List = transform.find_small_directories(File_Tree)

    Mem_For_Delete = sum(R_List)

    # Report
    load.display_output(File_Tree, Mem_For_Delete)


