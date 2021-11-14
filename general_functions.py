from pathlib import Path
import os

base_folder = 'data'
base_file_name = 'aoc_data_{}.txt'

def get_location(day):

    p = Path(os.path.join(base_folder, base_file_name.format(day)))
    if p.exists():
        return p
    else:
        raise ValueError('file: {} not found.'.format(p))


def read_data(day):

    p = get_location(day)

    with open(p) as f:
        content = f.readlines()

    data = [c.strip('\n').strip('\t') for c in content]

    return data

