5.1 Easy

import os
import sys

def mk_dir(path):
    try:
        os.mkdir(path)
        print('Directory is made')
    except FileExistsError:
        print('Directory already exists')


def rm_dir(path):
    try:
        os.removedirs(path)
        print('Directory is removed')
    except FileExistsError:
        print('Directory is not here')

5.2 Easy

def list_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])

5.3 Easy

def create_file_copy():
    filename = sys.argv[0]

    with open(filename, 'rb') as f:
        name, extension = filename.split('.')
        with open(name + ' copy.' + extension, 'wb') as destination_f:
            destination_f.write(f.read())

if __name__ == "__main__":
    dir_path = 'dir_()'
    [mk_dir(dir_path.format(i)) for i in range(1, 10)]
    [rm_dir(dir_path,format(i)) for i in range(1, 10)]

    list_dir()
    create_file_copy()