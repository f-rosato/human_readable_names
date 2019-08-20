# human_readable_names
A package for getting human readable strings to use as identifiers, etc.

example:
```
>>> from human_readable_names import give_name
>>> for n in range(10):
...     print(give_name())
Advantage
Antigua
Apollo
Appaloosa
Aquaman
Aristotle
Aruba
Athena
Aurora
Avalanche
>>> for n in range(10):
...     print(give_name({name}_{number}))
Axe_11
Baccarat_12
Backgammon_13
Backhander_14
Baja_15
Bald_Eagle_16
Bali_17
Barracuda_18
Batman_19
Bayonet_20
```

Contributions to the default name source txt are more than welcome!