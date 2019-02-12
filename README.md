# spec.py
This tool can generate file lists to use with EPM or alternatively do the whole thing for you. Here's an example run:
```
(gcc4)  esp@calcifer ~/epm/gdb-6.8 $ cat header
%product GDB 6.8
%copyright The GNU Project
%vendor SGUG
%license /usr/people/esp/epm/gdb-6.8/LICENSE
%readme /usr/people/esp/epm/gdb-6.8/README
%description The GNU debugger
%version 6.8-01 2019020701
(gcc4)  esp@calcifer ~/epm/gdb-6.8 $ python3 ~/spec.py/spec.py -h header -t -p gdb -e /opt/local/gdb
/usr/people/esp/epm/gdb-6.8/gdb-6.8-01-irix-6.5-mips.tardist
(gcc4)  esp@calcifer ~/epm/gdb-6.8 $ ls -l *tardist
-rw-r--r--    1 esp      user      28021760 Feb 12 04:25 gdb-6.8-01-irix-6.5-mips.tardist
```
Run it without arguments to get an usage message.