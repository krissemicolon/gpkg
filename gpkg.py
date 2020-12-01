#!/usr/bin/python

import sys
import getopt
import os
import time
from threading import Thread

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it);
    def show(j):
        x = int(size*j/count);
        file.write("%s[%s%s] %i/%i\r" % (prefix, "≈"*x, "~"*(size-x), j, count));
        file.flush();  
    show(0);
    for i, item in enumerate(it):
        yield item
        show(i+1);
    file.write("\n");
    file.flush();

pkgName = str(sys.argv[1]);
def pkgClone():
    os.system("git clone --quiet https://github.com/"+pkgName+" >> /dev/null");

def pkgInstall():
    repoarray = pkgName.split("/");
    username = repoarray[0];
    reponame = repoarray[1];

    pkgFiles = str(os.listdir(reponame))
    os.chdir(reponame);

    # switch (pkgFiles) {
    #     ".c" in pkgFiles:
    #         print("Repository in C");

    #     ".rs" in pkgFiles:
    #         print("Repository in Rust");

    #     ".py" in pkgFiles:
    #         print("Repository in Python");
    # }

    if "configure" in pkgFiles:
        os.system("autoreconf -i >> /dev/null");
        os.system("./configure >> /dev/null");

    if "Makefile" in pkgFiles:
        os.system("make --silent >> /dev/null");
        fs = open("Makefile", "r");
        makefileContent = fs.read();

        if "build" in makefileContent:
            os.system("make --silent build >> /dev/null");

        if "install" in makefileContent:
            os.system("make --silent install >> /dev/null");

    
    if "install.sh" in pkgFiles:
        os.system("./install.sh >> /dev/null");


pkgCloneT = Thread(target = pkgClone)
pkgCloneT.start();
while pkgCloneT.is_alive():
    for i in progressbar(range(100), "Cloning Repository: ", 40):
        time.sleep(0.004); 
    os.system("clear");
pkgCloneT.join();

pkgInstallT = Thread(target = pkgInstall)
pkgInstallT.start();
while pkgInstallT.is_alive():
    for i in progressbar(range(100), "Installing: ", 40):
        time.sleep(0.004);
    os.system("clear");
pkgInstallT.join();

