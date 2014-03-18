# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:40:28 2014

@author: Vespa
"""

#import urllib2
#import time
import sys
from zerocommon import *

def FindAnimate(dblist,inputname):
    idx = sorted(dblist);
    bestid = [];
    for id in idx:
        if sum(map(lambda x:x in dblist[id],list(inputname))) == len(inputname):
            bestid.append(id);
    return bestid;
    
    

def main(argv):
    dblist = GetAnimateList();
    idlist = FindAnimate(dblist,argv[1]);
    for id in idlist:
        print dblist[id];
        

if __name__ == '__main__':
    main(sys.argv);