import os
import sys
import pwd
import grp
from stat import *

if len(sys.argv) < 2:
    print("Usage: %s <paths>" % sys.argv[0])
    sys.exit(0)

paths = sys.argv[1:]
    
while len(paths):
    path = paths.pop()
    for root, dirs, files in os.walk(path):
        dst = root
        src = root
        s = os.stat(root)
        mode = S_IMODE(s.st_mode)
        owner = pwd.getpwuid(s.st_uid).pw_name
        group = grp.getgrgid(s.st_gid).gr_name
        print("d %s %s %s %s %s" % (oct(mode)[2:], owner, group, dst, src))
        for file in files:
            fpath = root + '/' + file
            s = os.stat(fpath)
            if S_ISLNK(s.st_mode):
                type = 'l'
            else:
                type = 'f'
            mode = S_IMODE(s.st_mode)
            owner = pwd.getpwuid(s.st_uid).pw_name
            group = grp.getgrgid(s.st_gid).gr_name
            dst = fpath
            src = fpath
            print("%s %s %s %s %s %s" % (type, oct(mode)[2:], owner, group, dst, src))

