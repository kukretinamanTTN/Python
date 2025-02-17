import sys, os, datetime

# parsing all the options, storing them in a dictionary and returning it
def parser_op(args):
    
    #dictionary storing options
    options = {
        "name":None,
        "atime":None,
        "type":'f',
        "maxdepth":1,
        'search_dir':'.'
    }
    
    if '-name' in args:
        options["name"] = args[args.index('-name')+1]

    if '-atime' in args:
        options["atime"] = int(args[args.index('-atime')+1])

    if '-type' in args:
        options["type"] = args[args.index('-type')+1]

    if '-maxdepth' in args:
        options["maxdepth"] = args[args.index('-maxdepth')+1]

    if 'find.py' in args:
        options["search_dir"] = args[args.index('find.py')+1]

    return options

# function to match the file_paths
def matcher(file_path, options):

    # filename match condition
    file_name = os.path.basename(file_path)
    if options['name'] not in file_name: 
        return False
    
    # if dir_name = file_name
    is_file = os.path.isfile(file_path)
    if options['type']=='f' and not is_file or options['type']=='d' and is_file:
        return False
    
    # atime condition
    if options['atime'] >= 0:
        last_access = datetime.datetime.fromtimestamp(os.path.getatime(file_path))
        days_since_access = (datetime.datetime.now() - last_access).days
        if days_since_access>options['atime']:
            return False

    return True

# recursively traversing and printing the paths if they match
def traverse(curr_dir, curr_depth, options):
    if curr_depth <= int(options['maxdepth']):
        try:
            for entry in os.listdir(curr_dir):
                entry_path = os.path.join(curr_dir, entry)
                
                if matcher(entry_path, options):
                    print(entry_path)

                if os.path.isdir(entry_path):
                    traverse(entry_path, curr_depth+1, options)
        except (PermissionError, OSError):
            pass



if __name__ == '__main__':
    options = parser_op(sys.argv)
    traverse(options['search_dir'], 1, options)