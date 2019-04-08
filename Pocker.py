#!/usr/bin/python2.7

import sys
import os
from unshare import unshare

def run():
    i = 2
    string_cmd = ""
    while i<len(sys.argv):
        string_cmd = string_cmd + str(sys.argv[i]) + " "
        i +=1

    print("running " + string_cmd )
    os.chroot("/ubuntu_xenial_1604")
    os.chdir("/")
    os.system("mount -t proc proc /proc")
    unshare(131072)
    unshare(1073741824)
    unshare(67108864)
    os.system(str(string_cmd))

if __name__ == '__main__':
    if sys.argv[1] == "run":
        run()
    else :
        print("Whaaaat!!")