from pathlib import Path
import os

base_folder = 'data'
base_file_name = 'aoc_data_{}.txt'
base_testfile_name = 'aoc_data_{}_test.txt'


def get_location(day, test):
    if test:
        p = Path(os.path.join(base_folder, base_testfile_name.format(day)))
    else:
        p = Path(os.path.join(base_folder, base_file_name.format(day)))

    if p.exists():
        return p
    else:
        raise ValueError('file: {} not found.'.format(p))


def read_data(day, test=True):
    p = get_location(day, test)

    with open(p) as f:
        content = f.readlines()

    data = [c.strip('\n').strip('\t') for c in content]

    return data
