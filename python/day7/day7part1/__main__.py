# Main function:
if __name__ == "__main__":

    import sys
    import parse_input as extract
    # from .process import process_data
    import process as transform
    import display_output as load

    '''
    - / (dir)
        - a (dir)
            - e (dir)
            - i (file, size=584)
            - f (file, size=29116)
            - g (file, size=2557)
            - h.lst (file, size=62596)
        - b.txt (file, size=14848514)
        - c.dat (file, size=8504156)
        - d (dir)
            - j (file, size=4060174)
            - d.log (file, size=8033020)
            - d.ext (file, size=5626152)
            - k (file, size=7214296)
    '''
    '''
    filesystem = {
            '/' : {
                'a' : {
                    'e' : {'Type' : 'dir'},
                    'i' : {'Type' : 'file', 'Size' : 584},
                    'f' : {'Type' : 'file', 'Size' : 29116},
                    'g' : {'Type' : 'file', 'Size' : 2557},
                    'h.lst' : {'Type' : 'file', 'Size' : 62596}
                    },
                'b.txt' : {'Type' : 'file', 'Size' : 14848514},
                'c.dat' : {'Type' : 'file', 'Size' : 14848514},
                'd' : {
                    'j' : {'Type' : 'file', 'Size' : 4060174},
                    'd.log' : {'Type' : 'file', 'Size' : 8033020},
                    'd.ext' : {'Type' : 'file', 'Size' : 5626152},
                    'k' : {'Type' : 'file', 'Size' : 7214296}
                    }
                }
            }
    '''

    # Read input
    fileName = sys.argv[1]
    file = extract.parse_input(fileName)
    data = extract.process_commands(file)
    print(data)
    # Process Data
    output = transform.process_data(data)

    # Report
    load.display_output(output)


