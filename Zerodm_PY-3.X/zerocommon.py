# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:28:48 2014

@author: Vespa
"""
import re
import os
def GetRE(content,regexp):
    return re.findall(regexp, content)
    
def GetAnimateList():
    if not os.path.exists("./database.dat"):
        print("database.dat not exist!");
        return None;
    f = open("database.dat","r");
    animateList = {};
    for line in f:
        info = line.strip("\n").split("::");
        if animateList.get( int(info[0]) ) != None:
            print("Item %s(%s) is repeat;"%(info[0],info[1]));
            f.close();
            return None;
        else:
            animateList[int(info[0])] = info[1];
    f.close();
    return animateList;