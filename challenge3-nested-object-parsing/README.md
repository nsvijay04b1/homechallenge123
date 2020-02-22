# Python code to retrieve value from a nested object

# Usage

```
nestedObject.py  object  key

```

# Python code
```
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

```


*  This program can accept object and key as command line parameters and return the value as well
```
[kube@eaasrt vijay]$ ./nestedObject.py  "{\"9\":{\"2\":{\"3\":\"200\"}}}" "9/2/3"
d     # this is the value for example 1 in challenge 3 , object={'a':{'b':{'c':'d'}}} , key = "a/b/c"
a     # this is the value for example 2 in challenge 3 , object={'x':{'y':{'z':'a'}}},  key =" x/y/z"
200   # this is  the value for command line parameters passed,  object={'9':{'2':{'3':'200'}}},  key ="9/2/3"
```
