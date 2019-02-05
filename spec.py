import os
import sys
import pwd
import grp
import getopt
from stat import *

def usage():
    print("Usage: %s (options) <paths>" % sys.argv[0])
    print(" -d<dir>     create destination paths relative to dir")
    print(" -u<uid>     force uid on all files")
    print(" -g<gid>     force gid on all files")
    sys.exit(0)

if len(sys.argv) < 2:
    usage()
    
paths = sys.argv[1:]

force_uid = None
force_gid = None
strip_prefix = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "u:g:d:", ["help", "output="])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    usage()

for o, a in opts:
    if o == '-g':
        force_gid = int(a)
    elif o == '-u':
        force_uid = int(a)
    elif o == '-d':
        strip_prefix = a

def get_info(path, known_type=''):
    src = path
    if strip_prefix:
        dst = os.path.relpath(path, strip_prefix)
    else:
        dst = path
    s = os.stat(root)
    mode = S_IMODE(s.st_mode)
    if force_uid is not None:
        owner = pwd.getpwuid(force_uid).pw_name
    else:
        owner = pwd.getpwuid(s.st_uid).pw_name
    if force_gid is not None:
        group = grp.getgrgid(force_gid).gr_name
    else:
        group = grp.getgrgid(s.st_gid).gr_name

    if known_type:
        type = known_type
    elif S_ISLNK(s.st_mode):
        type = 'l'
    else:
        type = 'f'
    return(type, oct(mode)[2:], owner, group, src, dst)

while len(paths):
    path = paths.pop()
    for root, dirs, files in os.walk(path):
        print("%s %s %s %s %s %s" % get_info(root, known_type='d'))
        for file in files:
            fpath = root + '/' + file
            print("%s %s %s %s %s %s" % get_info(fpath))

