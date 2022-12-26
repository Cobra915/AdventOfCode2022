import pprint

commands = [{'Command': 'cd /', 'Output': []},
    {'Command': 'ls', 'Output': ['dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']},
    {'Command': 'ls', 'Output': ['dir e', '29116 f', '2557 g', '62596 h.lst']},
    {'Command': 'cd e', 'Output': []},
    {'Command': 'ls', 'Output': ['584 i']},
    {'Command': 'cd ..', 'Output': []},
    {'Command': 'cd ..', 'Output': []},
    {'Command': 'cd d', 'Output': [], 'Output': ['4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']}]


def create_folder(name: str, parent: dict = None) -> dict:
    """
    Create a folder with the given <name>, and optionally link to a <parent> folder
    """
    return {
        "parent": parent,
        "name": name,
        "subfolders": [],
        "localfiles": [],
        "size": None,
    }

def add_child(parent: dict, name: str) -> dict:
    """
    Start: only have the parent folder
    -------
    foo = {
        "parent": whocares,
        "name": "COLIN",
        "subfolders": {}
    }
    """
    # Step 1: create a new folder, with a reference to the parent
    newfolder = create_folder(name)
    newfolder["parent"] = parent
    """
    After Step 1:
    -------------
     foo = {
        "parent": whocares,
        "name": "COLIN",
        "subfolders": {}
    }
    child = {
        "parent": foo,
        "name": "MITCH",
        "subfolders": {}
    }

    """
    # Step 2: add that new folder to the parent's children
    parent["subfolders"][name] = newfolder
    """
    foo = {
        "parent": whocares,
        "name": "COLIN",
        "subfolders": {"MITCH":child}
    }
    child = {
        "parent": foo,
        "name": "MITCH",
        "subfolders": {}
    }

    """
    return newfolder

def add_child(parent: dict, name: str) -> dict:
    parent["subfolders"][name] = create_folder(name, parent)
    return parent["subfolders"][name]

"""
test = create_folder(name="/")
print(test["parent"])
sub = create_folder(name="a",parent=test)
print(sub["parent"])
print(sub["parent"] == test)
"""
d = {}
d['new'] = 1
d['new2'] = 2
d['new2'] = 4
d["subdict"] ={"a":4}
d["subdict"]["new"] = 12

d["subdict"]["parent"] = d

pprint.pprint(d)
pprint.pprint(d == d["subdict"]["parent"])
pprint.pprint(id(d))
