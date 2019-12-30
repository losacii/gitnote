from sys import argv
from os import path, system, chdir

if len(argv) > 1:
    fpath = argv[1]
    fdir = path.dirname(fpath)

    command = f"cd {fdir}"
    system(command)
    chdir(fdir)
else:
    print("None argument")
