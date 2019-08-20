# human_readable_names
A package for getting human readable strings to use as identifiers, etc.
A single class, ```Namer```, is exposed.

The names are drawn by default from a built-in list.
 
Its most basic usage is as an
infinite iterable that generates names (when no name is left, the list is
rolled over and an epoch index is added to the names).

```Namer``` is initialized with optional parameters for defining the base
formatting and whether to pick the names at random.
Notably, the formatting can include a sequential number (not to be confused
with the epoch number, which is added automatically when the list is rolled over
to ensure uniqueness).
The user can also provide her own source for names, customize the first
number for sequential numbering, specify whether to sort the source,
customize the epoch number formatting.

For slightly more advanced customization, you can also specify a function to apply to all
the names (typical example: lambda n: n.upper(). The user is responsible for
providing a function that returns a string. Collisions will be filtered away
You can break stuff with this!).

The initialized behavior can be overridden on the fly by using the
 ```give_name``` method instead of iterating.

The ```Namer``` can be reset with the ```reset``` method. Once the ```Namer```
is reset, the uniqueness of the names is no more guaranteed!

Example of usage:

```
>>>from random import seed  # just for repeatability
>>>from human_readable_names import Namer
>>>seed(0)
>>>n = Namer()
>>>for _ in range(3):
...    print(n.give_name())
Advantage
Antigua
Apollo

>>>for _ in range(3):
...    print(n.give_name('{name}_{number}'))
Appaloosa_4
Aquaman_5
Aristotle_6

>>>for _ in range(3):
...    print(n.give_name('{number}_{name}_test', random=True))
7_Predator_test
8_Runabout_test
9_Blizzard_test

>>>print(next(n))
Aruba

>>>counter = 0
>>>for name in n:
...    counter += 1
...    if counter > 5:
...        break
...    else:
...        print(name)
Athena
Aurora
Avalanche
Axe
Baccarat

>>>n.reset()
>>>print(next(n))
Advantage
```

Contributions to the default name source txt are **more than welcome**!