def read(file):
    fl = open(file, "r")
    fl.seek(0)
def write(file, content = None):
    fl = open(file, "w")
    fl.write(content)
    fl.seek(0)

def append(file, content = None):
    fl = open(file, "a")
    fl.write(content)
    size = len(file)
    fl.seek(size)

import os
def delete(file):
    os.remove(file)

def file_manager(file_name, operation, content=None):
    dict_func_for_files = {
        "read" : read,
        "write" : write,
        "append" : append,
        "delete" : delete
    }
    if operation in dict_func_for_files.keys():
        return dict_func_for_files[operation](file_name)
