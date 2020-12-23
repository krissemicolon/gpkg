#!/usr/bin/python

import sys
import os
import argparse
import multiprocessing

MAKEOPTS = "--silent -j" + str(multiprocessing.cpu_count());

try:
    pkgName = str(sys.argv[1]);
except:
    print("Usage: gpkg <username/repository>");
    exit(-1);

def pkgClone():
    os.system("git clone --depth 1 --quiet https://github.com/"+pkgName);

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

    if "configure" in pkgFiles:
        os.system("autoreconf -i");
        os.system("./configure");

    if "Makefile" in pkgFiles:
        os.system("make "+MAKEOPTS);
        fs = open("Makefile", "r");
        makefileContent = fs.read();

        if "build" in makefileContent:
            os.system("make build "+MAKEOPTS);

        if "install" in makefileContent:
            os.system("make install "+MAKEOPTS);

    
    if "install.sh" in pkgFiles:
        os.system("./install.sh");

    os.system("cd ..; rm -rf "+reponame);

pkgClone();
pkgInstall();

