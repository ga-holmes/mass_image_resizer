# get the path to the a file
def get_path(filepath=''):

    if not '/' in filepath:
        return ''

    last_oc = filepath.rindex('/')
    return filepath[:last_oc+1]


# get the file from the path
def get_filename_from_path(filepath=''):

    if not '/' in filepath:
        return ''

    last_oc = filepath.rindex('/')
    return filepath[last_oc+1:]


# returns the file extension
def check_extension(filename):

    if '.' in filename:
        n_file = filename.rindex('.')

        return filename[n_file+1:]

    return ''

# Remove characters that aren't allowed in a filename
def fix_filename(filename: str):
    bad_chars = ['*', '/', '\\', ':', '\"', '<', '>', '|', '?']
    for c in bad_chars:
        filename = filename.replace(c, '')

    if check_extension(filename) != 'pdf':
        filename = filename + '.pdf'

    return filename


# get user defined file name or default
def get_file_name():

    fname = input("Enter output file name: ")

    # return default
    if not fname:
        return 'out.pdf'

    fname = fix_filename(fname)

    return fname
