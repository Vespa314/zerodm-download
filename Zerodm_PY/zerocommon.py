# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:28:48 2014

@author: Vespa
"""
import re
import os
def GetRE(content,regexp):
    return re.findall(regexp, content)

def changecoder(item):
    try:
        item.decode('gbk','ignore')
        k=item
    except:
        k = item.decode('utf8','ignore').encode('gbk','ignore');
    k = k.replace(",","")
    return k
    
def GetAnimateList():
    if not os.path.exists("./database.dat"):
        print "database.dat not exist!";
        return None;
    f = open("database.dat","r");
    animateList = {};
    for line in f:
        info = line.strip("\n").split("::");
        animateList[info[0]] = info[1].decode('utf8','ignore').encode('gbk','ignore');
    f.close();
    return animateList;