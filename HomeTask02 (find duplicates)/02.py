import sys
import os
import hashlib
import collections


def hash_file(filename):
    with open(filename, "rb") as f:
        res = hashlib.sha1()
        while True:
            data = f.read(2**18)
            if not data:
                break
            res.update(data)
    return res.hexdigest()        


if __name__ == '__main__':
    if len(sys.argv) != 2:
            print('usage: ./02.py dirname')
            sys.exit(1)    
     
    dirname = sys.argv[1]
    equal = collections.defaultdict(list)
    
    for top, _, files in os.walk(dirname):
        for nm in files:
            p = os.path.join(top, nm)
            if nm[0] != '.' and nm[0] != '~' and not os.path.islink(nm):
                equal[hash_file(p)].append(p) 
    
    print(*[':'.join(val) for val in equal.values() if len(val) > 1], sep='\n')

