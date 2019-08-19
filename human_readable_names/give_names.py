from collections import deque
import os.path as osp

THISDIR = osp.dirname(osp.realpath(__file__))

with open(osp.join(THISDIR, 'human_readable_names.txt'), 'r') as names_file:
    names_list = deque(sorted([name for name in names_file.read().splitlines()]))


def give_name(numbered: bool=False):

    give_name.counter += 1

    if numbered:
        return names_list.popleft() + '_' + str(give_name.counter)
    else:
        return names_list.popleft()


give_name.counter = 0
