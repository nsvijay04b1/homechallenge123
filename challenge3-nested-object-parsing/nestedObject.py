#!/usr/bin/python
import sys
import json
from functools import reduce

def getkeyvalue(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("/"), dictionary)

object1={'a': {'b': {'c': 'd'}}}
key1="a/b/c"
print (getkeyvalue(object1, key1))

object2={'x': {'y': {'z': 'a'}}}
key2="x/y/z"
print (getkeyvalue(object2, key2))

object3=json.loads(sys.argv[1])
key3=sys.argv[2]
print (getkeyvalue(object3,key3))
