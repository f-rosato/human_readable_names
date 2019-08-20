import os.path as osp
from random import randint

THISDIR = osp.dirname(osp.realpath(__file__))
DEFAULT_SOURCE = osp.join(THISDIR, 'human_readable_names.txt')


class Namer:
    def __init__(self,
                 default_format_string='{name}',
                 default_random=False,
                 first_number=1,
                 source_file=DEFAULT_SOURCE,
                 sort_source=True,
                 epoch_format_string='_({})',
                 transformation=lambda name: name):

        """
        Namer is a class for generating human readable names. Its basic usage is as an
        infinite iterable that generates names (when no name is left, the list is
        rolled over and an epoch index is added to the names).

        :param default_format_string: the python-style format string to use during iteration. Default = '{name}'

        Valid items for format_string:
        - name
        - number (the sequential number of the given name; is set to 0 at every call to reset())

        :param default_random: whether to pick the names at random from the underlying list. Default = False
        :param first_number: the first number to use for the built-in sequential numbering.
        :param source_file: the source file to pick the names from (one per row). The module has a built-in source
        with 300+ names.
        :param sort_source: whether to sort the names found in the source file. Default = True
        :param transformation: a function to apply to the names pulled from the source. Default = lambda n:n (no-op)
        """

        self.dfs = default_format_string
        self.dr = default_random
        self.first_number = first_number - 1
        self.last_source = None
        self.names_list = None
        self.counter = None
        self.transformation_fn = transformation
        self.epoch = None
        self.epoch_format = epoch_format_string
        self.sort = sort_source
        self.reset(source_file, 0)

    def __iter__(self):
        return self

    def __next__(self):
        return self.give_name(self.dfs, random=self.dr)

    def reset(self, source_file=DEFAULT_SOURCE, epoch=0):
        self.last_source = source_file
        self.counter = self.first_number
        self.epoch = epoch
    
        if epoch:
            epoch_string = self.epoch_format.format(epoch)
        else:
            epoch_string = ''
    
        with open(source_file, 'r') as names_file:
            self.names_list = list(set([self.transformation_fn(name) + epoch_string for name in names_file.read().splitlines()]))
            # list-set for uniqueness
        if not self.names_list:
            raise ValueError('Empty source')

        if self.sort:
            self.names_list = sorted(self.names_list)

    def remaining(self):
        """Returns the number of remaining names before an epoch rollover is performed."""
        return len(self.names_list)

    def give_name(self, format_string='{name}', random: bool = False):
    
        """
        Returns a string containing a human readable name. Just like iterating, but the formatting and random picking
        can be overridden on the fly.

        Optional arguments:
        :param format_string: a python-style item format string (see below for valid items). Default = '{name}'
        :param random: specifies whether to return the next available name in alphabetical order or a random one.
        default = False
    
        Valid items for format_string:
        - name
        - number (the sequential number of the given name; is set to 0 at every call to reset())
        """
    
        self.counter += 1
    
        if random:
            idx = randint(0, len(self.names_list) - 1)
        else:
            idx = 0
    
        try:
            name = self.names_list.pop(idx)
        except IndexError:
            self.reset(self.last_source, self.epoch + 1)
            name = self.names_list.pop(idx)
    
        f_name = format_string.format(name=name,
                                      number=self.counter)
    
        return f_name


if __name__ == '__main__':

    from random import seed
    seed(0)

    n = Namer()
    for _ in range(3):
        print(n.give_name())
    for _ in range(3):
        print(n.give_name('{name}_{number}'))
    for _ in range(3):
        print(n.give_name('{number}_{name}_test', True))

    print(next(n))

    counter = 0
    for name in n:
        counter += 1
        if counter > 5:
            break
        else:
            print(name)

    n.reset()
    print(next(n))
