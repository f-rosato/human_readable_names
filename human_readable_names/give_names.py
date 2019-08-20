import os.path as osp
from random import randint

THISDIR = osp.dirname(osp.realpath(__file__))
DEFAULT_SOURCE = osp.join(THISDIR, 'human_readable_names.txt')


def reset(source_file=DEFAULT_SOURCE, epoch=0):
    """Resets the name list and the counter."""

    reset.last_source = source_file
    give_name.counter = 0

    if epoch:
        epoch_string = '_({})'.format(epoch)
    else:
        epoch_string = ''

    with open(source_file, 'r') as names_file:
        globals()['names_list'] = sorted(list(set([name + epoch_string for name in names_file.read().splitlines()])))

    if not globals()['names_list']:
        raise ValueError('Empty source')


reset.last_source = None


def remaining():
    """Returns the number of remaining names before an epoch rollover is performed."""
    return len(globals()['names_list'])


def give_name(format_string='{name}', random: bool = False):

    """
    Returns a string containing a human readable name.
    Optional arguments:
    :param format_string: a python-style item format string (see below for valid items). Default = '{name}'
    :param random: specifies whether to return the next available name in alphabetical order or a random one.
    default = False

    Valid items for format_string:
    - name
    - number (the sequential number of the given name; is set to 0 at every call to reset())
    """

    give_name.counter += 1

    if random:
        idx = randint(0, len(globals()['names_list']) - 1)
    else:
        idx = 0

    try:
        name = globals()['names_list'].pop(idx)
    except IndexError:
        give_name.epoch += 1
        reset(reset.last_source, give_name.epoch)
        name = globals()['names_list'].pop(idx)

    f_name = format_string.format(name=name,
                                  number=give_name.counter)

    return f_name


give_name.counter = 0
give_name.epoch = 0


reset()  # has to be executed at module load
