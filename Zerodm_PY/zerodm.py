# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:40:28 2014

@author: Vespa
"""

import urllib2
import time
import sys
from zerocommon import *


def FindAnimate(dblist,inputname):
    idx = sorted(dblist);
    bestid = [];
    for id in idx:
        if len(re.findall(inputname,dblist[id]))>0:
            bestid.append(id);
    return bestid;
    
def ShowAnimateFound(name,idlist,dblist):
    if len(idlist) == 0:
        print name," Not Found!!";
        return 0;
    if len(idlist) == 1:
        if name == dblist[idlist[0]]:
            return 1;
        else:
            print "\nDownload :",dblist[idlist[0]],"?[Y/N]";
            result = raw_input("");
            if result.lower() == "y":
                return 1;
            else:
                return 0;
    
    print "\nAnimate Found Are List Below,Selece The Index You Want:\n";
    for (i,id) in zip(range(1,len(idlist)+1),idlist):
        print "[%d]:%s"%(i,dblist[id]);
    print "[Q]:quit\n";
    
    while True:
        result = raw_input("Input:");
        if result.lower() == "q":
            return 0;
        if not result.isdigit():
            print "Input a Number";
        elif not int(result) in range(1,len(idlist)+1):
            print "Out of Range!!";
        else:
            return int(result);

def ShowEpsInfo(EPS_Idx):
    url = "http://dmxz.zerodm.net/xiazai/"+str(EPS_Idx)+".html";
    content = urllib2.urlopen(url).read();
    eps_regexp = r"<a\s*href=['\"].+?xunlei.+?['\"].*?>(.*?)</a>";
    eps_list = GetRE(content,eps_regexp);
    for (eps,epsinfo) in zip(range(1,len(eps_list)+1),eps_list):
        m_str = "[%d]:%s"%(eps,epsinfo);
        print m_str.ljust(20),;
        if not (eps % 4):
            print "\n",
        
def main(argv):
    if len(argv) == 1:
        pass###############################
    dblist = GetAnimateList();
    idlist = FindAnimate(dblist,argv[1]);
    choice = ShowAnimateFound(argv[1],idlist,dblist)-1;
    if choice != -1:
        print "Getting Info.......";
        ShowEpsInfo(idlist[choice]);
        

if __name__ == '__main__':
    main(sys.argv);