import os
import sys

try:
    dirs = sys.argv[1]
except BaseException:
    dirs = "./"


def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        if dir.endswith(".py"):
            Filelist.append(dir)
        else:
            pass
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist


res = get_filelist(dirs, [])
print(res)
