#!/usr/bin/python

import sys
import argparse
import os
import time
import subprocess
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
    subprocess.run("git clone --depth 1 --quiet https://github.com/"+pkgName, shell=True);

# def detectLanguage(repolang):
#     pkgFiles = str(os.listdir(reponame));

#     langswitch = {
            
#     }
#     switch(os.listdir(reponame)) 
#     {
#         case ".c" in pkgFiles:
#             print("Language is: C");
#             break;

#         case ".cpp" in pkgFiles:
#             print("Language is: C++");
#             break;

#         case ".rs" in pkgFiles:
#             print("Language is: Rust");
#             break;

#         case ".py" in pkgFiles:
#             print("Language is: Python");
#             break;
        
#         default:
#             print("Language couldn't be detected")
#     }

def pkgInstall():
    repoarray = pkgName.split("/");
    username = repoarray[0];
    reponame = repoarray[1];

    pkgFiles = str(os.listdir(reponame));
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
        subprocess.run("autoreconf -i", shell=True);
        subprocess.run("./configure", shell=True);

    if "Makefile" in pkgFiles:
        subprocess.run("make --silent", shell=True);
        fs = open("Makefile", "r");
        makefileContent = fs.read();

        if "build" in makefileContent:
            subprocess.run("make --silent build", shell=True);

        if "install" in makefileContent:
            subprocess.run("make --silent install", shell=True);

    
    if "install.sh" in pkgFiles:
        subprocess.run("./install.sh", shell=True);


pkgCloneT = Thread(target = pkgClone)
pkgCloneT.start();
while pkgCloneT.is_alive():
    for i in progressbar(range(100), "Cloning Repository: ", 40):
        time.sleep(0.004); 
    # subprocess.run("clear");
pkgCloneT.join();

# detectLanguage();

pkgInstallT = Thread(target = pkgInstall)
pkgInstallT.start();
while pkgInstallT.is_alive():
    for i in progressbar(range(100), "Installing: ", 40):
        time.sleep(0.004);
    # subprocess.run("clear");
pkgInstallT.join();

