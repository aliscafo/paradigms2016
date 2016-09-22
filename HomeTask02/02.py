import sys
import os
import hashlib
import collections

def hash_file(filename):
    with open(filename, "rb") as f:
        res = hashlib.sha1()
        while True:
            data = f.read(2**10)
            if not data:
                break
            res.update(data)
    return res.hexdigest()        


if __name__ == '__main__':
    dirname = sys.argv[1]
    equal = collections.defaultdict(list)
    for top, dirs, files in os.walk(dirname):
        for nm in files:
            if nm[0] != '.' and nm[0] != '~':
                equal[hash_file(os.path.join(top, nm))].append(os.path.join(top, nm)) 
    
    print(*([':'.join(equal[key]) for key in equal if len(equal[key]) > 1]), sep='\n')        