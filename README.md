# human_readable_names
A package for getting human readable strings to use as identifiers, etc.
A single class, ```Namer```, is exposed.

### Initialize your ```Namer```

```Namer``` is initialized with the following optional parameters:

- ```default_format_string```: the [python-style format string](https://docs.python.org/3.4/library/string.html#formatspec) to use during iteration.
    
    Valid keyword items for format_string:
    - ```name```
    - ```number``` (the sequential number of the given name; is set to 0 at every call to r

    Default: ```"{name}"```.

- ```default_random```: whether to pick the names at random from the underlying list. 

    Default = ```False```
- ```first_number```: the first number to use for the built-in sequential numbering.
- ```source_file```: the source file to pick the names from (one per row). __The module has a built-in default source
with 300+ names.__
- ```sort_source```: whether to sort the names found in the source file. 
    
    Default: ```True```
- ```transformation```: a function to apply to the names pulled from the source before formatting. The user is responsible for
providing a function that returns a string. Collisions will be filtered away.
You can break stuff with this! 

    Default: ```lambda n:n  #(no-op)```
 

### Interact with your ```Namer```
The most basic usage of ```Namer``` is as an
infinite iterable that generates names (when no name from the source is left, the list is
rolled over and from then on an epoch index is added to the names).

Instead of iterating (or using ```next``` directly), you can use the method  **```give_name```**.
This also allows you, if you want, to override the initialized behavior temporarily and on the fly: you can change formatting and pick randomness.

The ```Namer``` can be reset with the **```reset```** method. Once the ```Namer```
is reset, the uniqueness of the names is no more guaranteed! When resetting, you have the opportunity to pass the following parameters:

- ```source_file```: same as when initializing.
    
- ```epoch```: the epoch to start with. Default: ```0``` (no epoch index displayed)


### Usage example

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

TODOs:
- [ ] Allow to have a generic text stream as source
- [ ] Allow to filter the built-in names by category

Contributions to the default name source txt are **more than welcome**!