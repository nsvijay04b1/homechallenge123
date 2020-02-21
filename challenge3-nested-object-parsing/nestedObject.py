!/usr/bin/python
from functools import reduce

def getkeyvalue(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("/"), dictionary)

object1={'a': {'b': {'c': 'd'}}}
key1="a/b/c"
print (getkeyvalue(object1, key1))

object2={'x': {'y': {'z': 'a'}}}
key2="x/y/z"
print (getkeyvalue(object2, key2))
