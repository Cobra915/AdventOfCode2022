def calculate_size(pwd: dict):
    pwd["size"] = 0
    for file in pwd["localfiles"].values():
        pwd["size"] += file["Size"]
    for subfolder in pwd["subfolders"].values():
        pwd["size"] += calculate_size(subfolder)
    return pwd["size"]

def create_folder(name: str, parent: dict = None) -> dict:
    """
    Create a folder with the given <name>, and optionally link to a <parent> folder
    """
    return {
        "parent": parent,
        "name": name,
        "subfolders": {},
        "localfiles": {},
        "size": None,
    }

def add_child(parent: dict, name: str) -> dict:
    parent["subfolders"][name] = create_folder(name, parent)
    return parent["subfolders"][name]

def build_file_tree(command_history):
    """
    Traverse command history to build out a hierarchy of files in a tree.
    """
    cnt = 0
    dircnt = 0
    # Create the root of the filesystem
    root = create_folder("/")
    # Assume our command history starts with the current folder being root
    pwd = root
    # For each command in the history
    for command in command_history:
        cmd = command['Command'].split()
        # Identify cmd case of cd, for changing directories 
        if cmd[0] == 'cd': 
            # if arg = '/', set pwd to root
            if cmd[1] == '/':
                pwd = root
            # arg = '..' to move back a dir
            elif cmd[1] == '..':
                pwd = pwd['parent']
            # arg to move to child dir
            else: 
                # if file is not in our tree
                if cmd[1] not in pwd["subfolders"]:
                    # Create it
                    add_child(parent=pwd, name=cmd[1])
                # Change pwd to arg
                pwd = pwd["subfolders"][cmd[1]]
        # If we are listing outputs
        if cmd[0] == "ls":
            # go through every item in the 'Output'
            for item in command['Output']:
                file_spec, file_name  = item.split()
                # If a directory
                if file_spec == "dir":
                    # file is not in our tree
                    if file_name not in pwd["subfolders"]:
                        # create it
                        add_child(parent=pwd, name=file_name)
                # If a file
                else:
                    size = int(file_spec)
                    if '.' in file_name:
                        name, ext = file_name.split('.')
                    else: 
                        name = file_name
                        ext = None
                    pwd["localfiles"][file_name] = {
                        "Name": name,
                        "Size" : size,
                        "Type" : ext,
                        "Folder": pwd,
                    }

    calculate_size(root)

    return root
