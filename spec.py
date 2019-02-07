import os
import sys
import pwd
import grp
import getopt
from stat import *

def usage():
    print('''
::~:~:~:~:::~~~~~~:~::::::::::~:::,:,,,,,,,:,,,,,,,,,,,,,,,,,,,,,,...,,,,.,,,.,.
::::::::::~~::~:~::::~::~::::::~:::,::=+????I?I=+,.:,,,,,..,,,,.,....,..,,,.,,,.
:,:::::::~::~:~:::::::::::::::::::~+???+I?IIIIIIIII??==:,,,,,,.,..,,,,.,....,,,.
:::::::~::::::~~:::::::::::::::::~=+,++I?I?II?IIIIIIII?I7II=,,,,,,,,,,..,,...,,.
:::::::~:::~~::::::::::::~::~:~:~?=I=?~??II7777I7I7II??IIIII+,,,,,,,,,,,,,,,,,,.
:::~:::::::::~:~::::::~::::~~~:+II+:I7II77777777777777I?I77I+:,,,,,,,,,,,,,,,,,.
::::::~:~:~::::::::~~::::~:~~=?II?IIII777777777777777777I7777I,,,,,,,,,,.,,..,,.
:::::::::::::::::::::::::~:~+II7+IIII7777777777777777777777777I,,,,,,.,.,..,,,,.
:::::::::~::::::::~:~::~::~I7II7?+?II77777777777777777777777777I::,,,,,,,,,,,,,.
:::::::::~:::~:::::~~~~~:~?II+??=+?III77777777777777777777777777?::,,,,,,,,,,,,.
::::::::::::::::::::~~~~=?I?+:I~~=??I7777777777777777777777777777~:,,,,,,,,,,,,.
:::::::::::::::::::::~:~~+?????::=?I77777777777777777777I7777777777~:,,,,,,,,,,.
::::::::::::::::::::::::=I?III?,:???+I77777777?II77777777?77777777777=,,,,,,,,,.
::::::::~::::::::::::~:~??=II?=:~~,...,?I+~::,..~==?77I77?II7I7I777II7?:,,,,,,,.
::::::::::::::::::::::=?~++7I?::,:+?+,,..=I~,:,:IIII+II777=III7II77II=?I,,,,,,,.
:::::::::::~:::::::~~+=+~,=II~.:,,.,..,=,I7II::~.+~.=I?I7I?I??II7IIII+II?:,,,,,.
::::::::::::::::::::+?=++:I~:?~:,:+~~~++?I77III??I777I77I?I+I++IIIIII??+I?:,,,,.
:::::::::~~::::::::~:+:=+==:~+:,=??I?II?I7777777I777777II?II:~+I?=I~II7++==,,,,.
::::::::::::::,::::~~=~I=~????,,:?IIII==II7777I7777777II?:?,??II??:~??+?+=~=,,,.
::::::::::::::::::~:~:+~~~:+==..,+?II=~..+=:IIII777777II?+I:~=+==?,~~+~~~::,,,,.
::::::::::::::::::~==~~,,::=::..,=+==?,......=I7II777II?~+I???+,~:~~,~,:~,:,,,,.
:::::::::~::::::::,~:,,,,,=:~:,.,,:....,,.,...,~+IIIII7II==???I+,~=~~~:=:,,:,,,.
::::::~:~:~:::::::,,,,,.,=:~I:~:,:,...........,,.::??I=~II=I+~=.::.:,.,,~,:,,,,.
::::~~~:~:~::::::,,,:,,,,=:,,~,.,...............,,:,~?,=??II7?,~:,,..,.,,.,,,,,.
::::::::~::::::::::,,:,~:~=~:,,,,...................:~==??=I?I?,:..,,.,.,,,,,,,.
::::~:~::::~:::::::,,,,,~,::,:~,,...~==::,,:,..,,...,~??++I=?I?=.....,,.,,,,,,,.
::::::::::~::::::,:,,:~,,,::??,~~,,:~+:??=?++==~?=,:++=II?IIIII:,....,,,..,,,,,.
~:::~:~~:::~:::::,:,,,,,,::+?+:+I?=+?I=+??IIIIIIII?~?+II7III7I?:+..,,,.,,,,,,,,.
:::::::::~::~::::::::,,,::=?+=??+=??IIIIII=?I7777II??I7777?II7II=,..,,,,,,,.,,,.
:~:::::::::~~:~::::::,::=I~=:????7?7II?:?~I?7I77?I77?II7I7I?III??:,,,,,,,,,,,,,.
::~::::::~:~::::,,::::::=+=~:+==I77?I?7???I?I7IIIII77?II777II7?II=:,,,,,,,,,,,,.
:::::::::::::::::::,::,:~=::=:~==?I??=?=~?=+I?II?II7IIIIIIII=???,.~,,,,,,,,.,,,.
::::::::::::::::::,,,...,,:=?=++==?I?=+==+=I+??I?IIIII?IIII?,I:I:..,,,,,,,,,,,,.
::,::::::::::::,.............=~+=?=+,+=:=?+?I++7I??II?????I,??.,......,,,,,,,,,.
::::::::::::::..............,=~+===,+~,?~~:+++?==+?+?+==~:,,=,............,,,,,.
:,::::,::::::.................~=:===~,?~++====~~:?++?+:.,:=,,...............,,,.
:,:,::::,,::,.................+=+:::~:~:.:=,~+:,,,.,..........................,.
,,,,::::,,:,................III?+=~~=,,,....,,.,.............................,,.
,,:,,:,:::,...............~7IIII???+~~~~,..........................,,,...,..:~~,
,,,:,,,:,...............,I7?77II7II???+.........................,:::,....,~~,,:,
,,,::,:,....,..,,...,..~77I7777777III~........................,,:,,,,.,~==,.,~~,
,,,:,,:..........,,,.:I7777777I7777I:..................,.....,,,..,,.:~=,.,~,,:,
,,,:,:.,.........,..I777777777777II..,................,......,,.,,.,:=~,~=,,,~:.
,,,,,,.,..,.,...,.,777777777777II:,.,.........,,,...,,.....,,,..,,,:::~=~======.
,,,,,.........,,,I777777777777II.,.,.........,,,,,,,,....,,,,,..,,,:...,:~:::~..
,,,,......,..,,:7777777 77777I..,,..,..,,..,,,,,,,,,,...,,,,.....,,..::~:~,.,~~.
:::,,,..,....,,7777777777777?.,,,.,.....,.,,.,,,,,,..,,,..,.....,,.,::,,,::~=~:,
::,..........,,7777777777II..,,,,,........,..,,,,,..,,,,.......,,..,.~,,::~::==,
::,,,.........,I7777777I7..,...,,,,,,.....,,,,,,....,,.,......,...:,..,:~~~~~::.
,,............,~7777777,.,,,,,,,,,,.,....,,,,,,.,,.............,:,...,,:~==~:~=,
.,.,...........,777I,I..,,,,,,,,,,,,,,.,..,,..,,,,,..,.......,,,,...,,::~~~~:::,
...............,?7?+,.,,,..,,,,,,,,,,,,.,,..,,,,,,..........,,,...,,,:~~=~=====:
..................I....,,,,,,,,,,,,,,,,...,,.,,,,,..........,....,,,~~:~~~=++++,
.............,:.+~...,,....,,,,,,,,,,,....,.,,,.,,,.......,.,..,,,:~==:~::~=?+:.
........,IIII=II~....,.....,,,,,,,,............................,,,~~~::~::~=~,,.
.......II?III,,+......,,,...,.,,,...............................::~~~~~=~~:,,,,.
.....,?I?IIIIII...,,,,,,...,,,...............................,.,:~~+=:,,,,,..,,.
....,,I+IIIIII.......,..........,.............................,::,:=,,,,,,::,::,
..,,,II=IIIII:.,....,,.,........,,,..........,,,,...........,,::~:,.,:~~~~=~:~:,
,,,,,II~+III?,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,~=~~~~=~~~~====+++:
Karl Marx (1818-1883)
''')
    
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
    return(type, oct(mode)[2:], owner, group, dst, src)

while len(paths):
    path = paths.pop()
    for root, dirs, files in os.walk(path):
        print("%s %s %s %s \"%s\" \"%s\"" % get_info(root, known_type='d'))
        for file in files:
            fpath = root + '/' + file
            print("%s %s %s %s \"%s\" \"%s\"" % get_info(fpath))

